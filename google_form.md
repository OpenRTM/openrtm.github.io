## Googleフォームで講習会参加登録フォームを作るときに設定する事

### 「メールアドレスを収集する」にチェックを入れる
### 登録した人に回答のコピーを送信する

![image](https://user-images.githubusercontent.com/6216077/59592353-d6ce2980-912a-11e9-9ad7-6eafbffda5b5.png)
![image](https://user-images.githubusercontent.com/6216077/59592707-85726a00-912b-11e9-9bc8-dbc0aff57020.png)

### 残り人数を制限、表示する

![image](https://user-images.githubusercontent.com/6216077/59592413-f49b8e80-912a-11e9-917c-fa10c2c005ff.png)

以下のコードをスクリプトエディタで設定。

```
function endFormCheck() {
  var LIMIT_COUNT = 10;

  var form = FormApp.getActiveForm();
  if (form.getResponses().length >= LIMIT_COUNT) {
    form.setAcceptingResponses(false);
  }
  else{
    var seat = LIMIT_COUNT -form.getResponses().length; 
     var description = '2019年6月5日(水)(10:00-17:00) 広島国際会議場 地下1F 会議運営事務室2・3において、ROBOMECH2019 RTミドルウエア講習会を開催いたします。\nご希望の方は、以下の申し込みフォームにてお申し込みください。\n'+'残り'+ seat + '席です。\n';
    form.setDescription(description); 
  }
}
```

![image](https://user-images.githubusercontent.com/6216077/59592564-40e6ce80-912b-11e9-9261-e95194405ea1.png)

![image](https://user-images.githubusercontent.com/6216077/59592875-d5e9c780-912b-11e9-83a5-ce6570f41790.png)

以下の2つのトリガーを設定する。
1つは送信時のトリガー。
![image](https://user-images.githubusercontent.com/6216077/59592937-f3b72c80-912b-11e9-8ae1-5509f025e1b4.png)
もう1つは時間ベースのトリガー。これはフォーム作成時、回答削除時には上のトリガーは作動しないため。
![image](https://user-images.githubusercontent.com/6216077/59593716-670d6e00-912d-11e9-81cf-564730b3a8a4.png)
