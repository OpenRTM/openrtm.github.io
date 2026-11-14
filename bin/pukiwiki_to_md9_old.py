import re
import os

# --- 中央揃え・太文字変換 ---
def convert_center_with_bold(line):
    """
    PukiWikiの CENTER: 行を HTML の <div align="center"> に変換し、
    PukiWikiの太字 ''text'' と Markdownの太字 **text** を <strong> に変換する。
    """
    # CENTER: にマッチするかチェック
    match = re.match(r'^CENTER:\s*(.+)$', line)
    if match:
        content = match.group(1).strip()

        # ''text'' → <strong>text</strong>（PukiWikiの太字）
        content = re.sub(r"''(.+?)''", r'<strong>\1</strong>', content)

        # **text** → <strong>text</strong>（Markdownの太字）
        content = re.sub(r"\*\*(.+?)\*\*", r'<strong>\1</strong>', content)

        return f'<div align="center">{content}</div>'

    return line  # CENTER: 以外の行はそのまま


# --- リンク変換 ---
def convert_links(text):
    # [[ラベル>URL]] または [[ラベル:URL]] を Markdownリンクへ（mailto:も対象）
    text = re.sub(r'\[\[(.+?)[>:]((mailto:|https?:\/\/|\/)[^\]]+)\]\]', r'[\1](\2)', text)

    # [[https://example.com]] や [[/local/path]] → <URL>（labelなし）
    text = re.sub(r'\[\[((https?:\/\/|\/)[^\]]+)\]\]', r'<\1>', text)

    # [[mailto:test@test.com]] → <mailto:test@test.com>（labelなしメールアドレス）
    text = re.sub(r'\[\[(mailto:[^\]]+)\]\]', r'<\1>', text)

    return text


# --- リスト変換（ネスト対応） ---
def convert_nested_list(line):
    hyphen = re.match(r'^(-+)\s*(.*)', line)
    plus = re.match(r'^(\++)\s*(.*)', line)
    if hyphen:
        indent = '  ' * (len(hyphen.group(1)) - 1)
        return f"{indent}- {convert_links(hyphen.group(2))}"
    elif plus:
        indent = '  ' * (len(plus.group(1)) - 1)
        return f"{indent}1. {convert_links(plus.group(2))}"
    else:
        return convert_links(line)


# --- 表変換 ---(html)
def convert_pukiwiki_table_to_html(lines):
    #tablesをhtmlにする
    output = []
    table_rows = []
    in_table = False

    for line in lines:
        if line.strip().startswith('|'):
            table_rows.append(line.strip())
            in_table = True
        else:
            if in_table:
                output.extend(render_html_table(table_rows))
                table_rows = []
                in_table = False
            output.append(line)

    if in_table:
        output.extend(render_html_table(table_rows))

    return output

def convert_markdown_links_to_html(text):
    """
    Markdown形式のリンク [label](url) を HTML形式の <a href="url">label</a> に変換する
    """
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)


#table内のリンクをhtmlにする
def render_html_table(rows):
    html = ['<table class="table-alt">']
    for i, row in enumerate(rows):
        cells = [cell.strip() for cell in row.strip('|').split('|')]
        html.append('  <tr>')
        for cell in cells:
            # MarkdownリンクをHTMLリンクに変換
            converted = convert_markdown_links_to_html(cell)
            tag = 'th' if i == 0 else 'td'
            html.append(f'    <{tag}>{converted}</{tag}>')
        html.append('  </tr>')
    html.append('</table>')
    return html

# --- 画像変換（#ref）---
def convert_ref_image(match):
    src = match.group(1).strip()
    param_str = match.group(2) or ""
    params = [p.strip() for p in param_str.split(',') if p.strip()]

    # デフォルト値
    align = None
    #width = "100%"
    width = "100"
    margin = None
    link = src
    float_align = None  # HTMLの align 属性用

    for p in params:
        if p in ['left', 'right', 'center']:
            align = p
            float_align = p  # <img align="">
        elif p == 'around':
            pass  # 無視する（styleやalign指定に活かす）
        elif re.match(r'^\d+%$', p):
            width = p
        elif p.startswith('margin='):
            margin = p.split('=')[1]
        elif p.startswith('url='):
            link = p.split('=', 1)[1]

    # スタイル生成
    style = f'width="{width};'
    if margin:
        style += f' margin:{margin}px;'
    style += '"'

    img_tag = f'<img src="{src}" {style}'
    if float_align in ['left', 'right']:
        img_tag += f' align="{float_align}"'
    img_tag += '>'

    # 最終HTML生成
    div_align = align if align in ['left', 'right', 'center'] else 'center'
    return f'<div align="{div_align}"><a href="{link}">{img_tag}</a></div>'

def convert_ref_image_old(match):
    src = match.group(1).strip()
    param_str = match.group(2) or ""
    params = [p.strip() for p in param_str.split(',') if p.strip()]
    align, width, margin = "center", "100%", None
    link = src  # デフォルトリンク先

    for p in params:
        if re.match(r'^\d+%$', p) or re.match(r'^\d+px$', p):
            width = p
        elif p in ['left', 'center', 'right']:
            align = p
        elif p.startswith('margin='):
            margin = p.split('=')[1]
        elif p.startswith('url='):
            link = p.split('=', 1)[1]

    style = f'style="width:{width};' + (f' margin:{margin}px;"' if margin else '"')
    return f'<div align="{align}"><a href="{link}"><img src="{src}" {style}></a></div>'


# --- 動画変換（固定サイズiframe＋<nowiki>は削除）---
def convert_nowiki_video_block(text):
    """
    <nowiki> [video:URL width:XXX] </nowiki> を固定サイズiframeに変換。
    <nowiki>と</nowiki>は削除。
    """

    def replacer(match):
        url = match.group(1).strip()

        yt_match = re.search(r'(?:v=|youtu\.be/)([\w\-]+)', url)
        if not yt_match:
            return f'<!-- Invalid YouTube URL: {url} -->'

        video_id = yt_match.group(1)
        embed_url = f"https://www.youtube.com/embed/{video_id}"

        # ここで固定サイズ
        iframe_html = f'<iframe width="560" height="315" src="{embed_url}" frameborder="0" allowfullscreen></iframe>'
        return f'\n{iframe_html}\n'
        #return f'<!-- <nowiki> -->\n{iframe_html}\n<!-- </nowiki> -->'

    pattern = r'<nowiki>\s*\[video:(https?://[^\s\]]+)(?:\s+width:\d+)?\]\s*</nowiki>'
    return re.sub(pattern, replacer, text, flags=re.IGNORECASE)



# --- メイン変換関数 ---
def pukiwiki_to_markdown(text):

    # 最初に動画ブロック変換
    text = convert_nowiki_video_block(text)

    lines = text.split('\n')
    output = []
    in_code_block = False  # 整形済みブロック中かどうか

    for i, line in enumerate(lines):
        stripped = line.lstrip()

        # --- 整形済みテキストブロック（文頭スペース） ---
        if re.match(r'^ ', line) and not re.match(r'^\s*[-+\*>|:]', line):
            if not in_code_block:
                output.append("```")  # 開始
                in_code_block = True
            output.append(line.strip('\n'))  # 中身はそのまま
            continue
        elif in_code_block:
            output.append("```")  # 終了
            in_code_block = False

        # --- コメント ---
        if line.strip().startswith('//'):
            output.append(re.sub(r'^//\s*(.*)', r'<!-- \1 -->', line))
            continue

        # 色付き (#color(red){text}) → <span style="color:red;">text</span>
        line = re.sub(r'#color\((.+?)\)\{(.+?)\}', r'<span style="color:\1;">\2</span>', line)
        line = re.sub(r'&color\((.+?)\)\{(.+?)\}', r'<span style="color:\1;">\2</span>', line)

        # --- 改行記法 ---
        line = re.sub(r'#br\b', '<br>', line)
        line = re.sub(r'&br;', '<br>', line)

        # --- 見出し（*〜*****） ---
        for level in range(5, 0, -1):
            line = re.sub(r'^' + r'\*' * level + r'\s*(.+)$', r'#' * level + r' \1', line)

        # --- 強調・斜体 ---
        line = re.sub(r"''(.+?)''", r'**\1**', line)
        line = re.sub(r"'''(.+?)'''", r'*\1*', line)

        # --- 定義リスト :term: desc → **term**: desc
        line = re.sub(r'^:(.+?):(.*)$', r'**\1**: \2', line)

        # --- インラインコード ~command → `command` ---
        line = re.sub(r'~(\S+)', r'`\1`', line)

        # 取り消し線 %%text%%
        line = re.sub(r'%%(.+?)%%', r'~~\1~~', line)

        # アンダーバー __text__
        line = re.sub(r'__([^_]+?)__', r'<u>\1</u>', line)

        # 上付き SUP{...};
        line = re.sub(r'SUP\{(.+?)\};', r'<sup>\1</sup>', line)

        # 下付き SUB{...};
        line = re.sub(r'SUB\{(.+?)\};', r'<sub>\1</sub>', line)

        # 左寄せ
        line = re.sub(r'^LEFT:\s*(.+)', r'<div align="left">\1</div>', line)

        # 右寄せ
        line = re.sub(r'^RIGHT:\s*(.+)', r'<div align="right">\1</div>', line)

        # --- 画像 (#ref) ---
        #line = re.sub(
        #    r'#ref\(\s*([^\s,]+)\s*(?:,\s*([^)]+))?\)',
        #    convert_ref_image,
        #    line
        #)
        line = re.sub(
            r'[&#]ref\(\s*([^\s,]+)\s*(?:,\s*([^)]+))?\)',
            convert_ref_image,
            line
        )

        # ---画像キャプションCENTER: ''text''をhtmlで表示
        #line = convert_center_bold(line)
        line = convert_center_with_bold(line)

        # --- リスト＋リンク ---
        line = convert_nested_list(line)

        output.append(line)

    # --- 最後のコードブロックを閉じる ---
    if in_code_block:
        output.append("```")

    # --- テーブル変換 ---
    #markdown
    #output = convert_table(output)
    output = convert_pukiwiki_table_to_html(output)

    return '\n'.join(output)



# --- 実行処理 ---
if __name__ == '__main__':

    # 既存の output.md を削除（あれば）
    if os.path.exists("output.md"):
        os.remove("output.md")
        print("🗑️  output.md を削除しました。")

    with open('sample.pukiwiki', 'r', encoding='utf-8') as f:
        pw_text = f.read()

    md_text = pukiwiki_to_markdown(pw_text)

    with open('output.md', 'w', encoding='utf-8') as f:
        f.write(md_text)

    print("✅ 変換完了：output.md")

