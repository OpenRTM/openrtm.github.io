---
layout: page
title: コンテナ技術を活用したソフトウェアプロファイルに基づくソフトウェアモジュール生成・運用に関する研究
---

# コンテナ技術を活用したソフトウェアプロファイルに基づくソフトウェアモジュール生成・運用に関する研究

<!-- 
- 元ページ: `/openrtm/ja/project/contest2025-si2025-1336`
- Drupal node ID: `7316`
- 投稿者: root
-->
- 投稿日時: 水, 2025-11-05 14:17
- 問合先（メールアドレス）: 220447031@ccmailg.meijo-u.ac.jp
- OS: Windows, Linux
- 言語: Python
- OpenRTM ver.: 1.2, 2.0
- Average: 0 まだ投票はありません
- タグ: ツール, GUI tool, system development, RTM contest 2025
- 最終更新日時: 月, 2025-12-01 19:03

# 目的

ロボットシステム開発において、ソフトウェアモジュールの動作環境構築は大きな課題です。 従来の開発手法では、以下のような問題が頻発していました。

- **環境構築の複雑さ:** 依存ライブラリのバージョン不整合や、複雑なインストール手順により、環境構築だけで多くの時間を要する。
- **再現性の欠如:** 「開発者のPCでは動くが、配布先のPCでは動かない」といった問題が発生する。
- **標準化の壁:** ソフトウェアの仕様記述（プロファイル）が標準化されておらず、異種ミドルウェア間での再利用が困難。

本研究では、これらの課題を解決するために、**「ISO 22166-202規格準拠の情報モデル」**と**「コンテナ技術（Docker）」**を融合させ、環境構築から運用までを自動化するシステムを開発しました。

# 概要

本プロジェクトでは、**異種ミドルウェアのロボットソフトウェアモジュールの動作環境を自動生成するシステム**を開発しました。

このシステムは、ロボットソフトウェアモジュールの仕様記述から、その実行環境（Dockerコンテナ）を自動生成するツールキットです。 以下の図のように、XML形式の情報モデル（SIM）を中心として、環境構築に必要なファイルを自動生成します。[![system_diagram1.png](/openrtm/sites/default/files/system_diagram1.png)](/openrtm/sites/default/files/system_diagram1.png)

リポジトリ内は処理の段階ごとに以下の3つのツールで構成されています。

**1. SIM\_generator (GUI Tool)** PythonのGUIフレームワーク **Streamlit** を用いたプロファイル作成ツールです。 ISO 22166-202規格に準拠した情報モデル（XML）を、ブラウザベースの直感的な操作で生成できます。複雑なXML構造を意識することなく、必須項目や依存関係を定義可能です。

**2. Dockerfile\_generator** SIM\_generatorで作成されたXMLを解析し、ミドルウェア（ROS 1/ROS 2/OpenRTM）や依存ライブラリ、Gitリポジトリからのソースコード取得命令を含んだ **Dockerfile** を自動生成します。 OSバージョン（Ubuntu 18.04/20.04/22.04等）やROSディストリビューション（Noetic/Humble等）を自動判別して記述します。

**3. robot\_container\_env (Compose Generator)** 生成された複数のDockerfileを組み合わせてシステム全体を起動するための **docker-compose.yml** を自動生成します。 特に、ROS 2利用時には **FastDDS** の設定ファイル（XML）や通信設定を自動で注入し、コンテナ間通信（Integration Mode）を容易に実現します。

# 特徴

- **国際標準（ISO 22166-202）への準拠** OpenRTMだけでなく、ROS 1/ROS 2など異種ミドルウェアへの対応も見据えた、共通形式でのデータ記述を採用しています。

- **ハードウェアアクセスの自動設定** Dockerコンテナ利用時の障壁となる、USBデバイス（カメラ、通信機器）へのアクセス権限や、GUI表示（X11 Forwarding）の設定を自動化しています。

- **ROS 2 コンテナ間通信のサポート** 複数のROS 2コンテナを連携させる際に必要となるDDS（Data Distribution Service）の設定やネットワーク設定を自動生成し、分散システムの構築を支援します。

# 仕様

## 開発環境 / 動作環境

- **言語:** Python 3.10+
- **GUIフレームワーク:** Streamlit
- **OS:** Linux (Ubuntu 20.04/22.04 推奨)
  - ※Windows (WSL2) 上のUbuntu環境でも動作可能です。ただし、WSLの仕様上、ホストPCのハードウェアデバイス（USBカメラ等）をコンテナにマウントできない場合があります。
- **依存ツール:** Docker Engine, Docker Compose

## システム構成

1. **SIM\_generator:** XMLプロファイル作成
2. **Dockerfile\_generator:** Dockerイメージ定義の自動生成
3. **robot\_container\_env:** コンテナオーケストレーション設定の自動生成

# 関連動画 (デモンストレーション・操作手順)

各ツールの操作手順と、最終的なシミュレーション動作の様子です。

- **1. SIM generator (環境構築＆情報モデル生成GUIの起動)** <https://youtu.be/OTg8-yjwZVI>

- **2. Dockerfile generator (Dockerfile自動生成の動作手順)** <https://youtu.be/HaDy8PuVPVg>

- **3. robot\_container\_env (docker-compose.yml自動生成の動作手順)** <https://youtu.be/PNStjX_-aOE>

- **4. 実行デモ (コンテナ起動＆シミュレーション動作確認)** <https://youtu.be/gdhVv0ZXGsw>

# ソースコード・リンク

本ツールのソースコードはGitHubにて公開しています。

- **GitHub Repository:** [masahiro0720/sim\_to\_env\_generate](https://github.com/masahiro0720/sim_to_env_generate.git)
- **License:** MIT License
