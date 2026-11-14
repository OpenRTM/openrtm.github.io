---
layout: page
title: ソースからのビルド (linux編)
---

<!-- Title: ソースからのビルド (Linux編) -->
#contents

OpenRTM-aist本体のソースを変更して利用したい場合には、OpenRTM-aistのソースコードを取得してビルドできます。


## Dockerでのビルド

Dockerfileを使い、OpenRTM-aistソースビルドに必要な最小限のライブラリだけをインストールした環境でビルドを行う手順を紹介します。 <br>
docker build コマンドで Dockerイメージを生成するのですが、毎回まっさらな環境でビルドできるのでお勧めです。

初めてDockerを使う場合は、以下のようにインストールしてください。Ubuntuのデスクトップ環境であれば docker.io パッケージが提供されていると思います。

```
 sudo apt install docker.io
```

<!-- - 参考：docker.io パッケージの提供が無い場合のインストール -->
<!-- -- 手動で、DockerのGPGキーを取得して、リポジトリ情報を書き込んで、docker-ceをインストールする流れになります -->
<!-- -- QEMU上にubuntu-20.04-server-cloudimg-arm64.imgで aarch64 環境を構築した時は、以下の手順でインストールしました -->
<!-- sudo apt install apt-transport-https ca-certificates curl software-properties-common -->
<!-- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - -->
<!-- sudo add-apt-repository "deb [arch=arm64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  -->
<!-- sudo apt update -->
<!-- sudo apt install docker-ce -->


## C++ソースのビルド

OpenRTM-aist 2.1系のソースには、Ubuntu22.04、24.04用のDockerfileが含まれています。

```
 OpenRTM-aist/scripts/ubuntu_2204/Dockerfile
 OpenRTM-aist/scripts/ubuntu_2404/Dockerfile
```

ビルド手順は以下となります。　Ubuntu24.04用のビルド例です。　<br>
ここではGitHubから最新のOpenRTM-aistソースを取得していますが、修正を加えたソースのビルドでも同様の手順で行えます。

```
 git clone https://github.com/OpenRTM/OpenRTM-aist
 sudo docker build -t test -f OpenRTM-aist/scripts/ubuntu_2404/Dockerfile .
```

エラーなくビルドが終了したら、-tオプションで指定した test という名前のDockerイメージが生成されていることを確認できます。

```
 sudo docker images
 REPOSITORY       TAG           IMAGE ID          CREATED           SIZE
 test                    latest         0bc00f471b64   27 seconds ago   1.52GB
```

ソースを修正しながらビルドが通るまで繰り返すと、 <none> というイメージが多数生成されます。　docker rmi で IMAGE ID を指定して削除できますが、まとめて削除したい場合は下記コマンド実行が便利です。

```
 sudo docker rmi $(sudo docker images -f dangling=true -q)
```

### Dockerイメージ「openrtm/devel-rtm」について

ソースビルドで使用した Dockerfile の1行目は、Ubuntu22.04用と24.04用でそれぞれの以下のようになっており、Dockerハブにアップロードされているこの名前のイメージを使用します。

```
 FROM openrtm/devel-rtm:ubuntu22.04
        or
 FROM openrtm/devel-rtm:ubuntu24.04
```

これらのイメージは、下記 Docierfile.devel-rtm から生成したものです。fluent-bitと、ROS2がインストールされています。
- Ubuntu22.04用：humble
- Ubuntu24.04用：jazzy

```
 OpenRTM-aist/scripts/ubuntu_2204/Dockerfile.devel-rtm
 OpenRTM-aist/scripts/ubuntu_2404/Dockerfile.devel-rtm
```

### Dockerでdebパッケージ生成まで一括処理するスクリプト

ここで紹介するスクリプトは、OpenRTM-aistのリリース用debパッケージ作成時に利用しているものです。 <br>
OpenRTM-aistソースを変更してインストールしたい場合、debパッケージで手軽に試せます。


このスクリプトは、Dockerでソースビルドからdebパッケージ生成まで行い、成果物であるdebパッケージをDockerコンテナからホスト側へコピーする処理までを一括で行います。

Ubuntu24.04用のdebパッケージを作成する場合の手順は以下となります。

```
 git clone https://github.com/n-kawauchi/RTM-src-pkgs-docker-build
 cd RTM-src-pkgs-docker-build/ubuntu_2404/
 sh build-cxx.sh
 ls -l
 drwxr-xr-x  2 root    root    4096 Jun 30 15:53 cxx-deb-pkgs/
```

成果物のdebパッケージは cxx-deb-pkgs 下に出力されています。所有者がrootになっていますので、実行ユーザに変更しておいた方がアクセスしやすいです。 <br>
ROSがインストールされたDockerイメージを使用しているので、ROS2向けのパッケージ（openrtm2-ros2-tp）も生成されます。
2.1系から追加されたSSMパッケージ（openrtm2-ssm-tp）も生成されます。

```
 ls cxx-deb-pkgs/
 openrtm2_2.1.0-0_amd64.buildinfo  openrtm2-dev_2.1.0-0_amd64.deb      openrtm2-naming_2.1.0-0_amd64.deb
 openrtm2_2.1.0-0_amd64.changes    openrtm2-doc_2.1.0-0_all.deb        openrtm2-ros2-tp_2.1.0-0_amd64.deb
 openrtm2_2.1.0-0_amd64.deb        openrtm2-example_2.1.0-0_amd64.deb  openrtm2-ssm-tp_2.1.0-0_amd64.deb
 openrtm2_2.1.0-0.dsc              openrtm2-idl_2.1.0-0_amd64.deb      openrtm2-ssm-tp-dbgsym_2.1.0-0_amd64.ddeb
```

（※）このスクリプトを amd64 環境で実行すれば amd64 用debパッケージが生成され、aarch64 環境で実行すれば arm64 用debパッケージが生成されます。

OpenRTM-aistソースを変更してインストールしたい場合、build-cxx.sh スクリプトの以下の部分をコメントアウトし、build-cxx.sh と同じディレクトリにOpenRTM-aistソースを配置して実行してください。

```
 #----- OpenRTM-aist
 echo "${password}" | sudo -S rm -rf ${TARGET}-*
 #rm -rf OpenRTM-aist    <-- コメントアウト
 #git clone https://github.com/OpenRTM/OpenRTM-aist    <-- コメントアウト
```

## Pythonソースのビルド

OpenRTM-aist-Python ソースには Dockerfile は含まれておりません。OpenRTM-aist-Pythonのリリース用debパッケージ作成時に下記Dockerfileを利用しています。
- [ubuntu_2204/Dockerfile-python-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2204/Dockerfile-python-deb)
- [ubuntu_2404/Dockerfile-python-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2404/Dockerfile-python-deb)

C++ソースビルドと同様に、Dockerでソースビルドからdebパッケージ生成まで行い、成果物であるdebパッケージをDockerコンテナからホスト側へコピーする処理までを一括で行うスクリプトを紹介します。

Ubuntu24.04用のdebパッケージを作成する場合の手順は以下となります。

```
 git clone https://github.com/n-kawauchi/RTM-src-pkgs-docker-build
 cd RTM-src-pkgs-docker-build/ubuntu_2404/
 sh build-python.sh
```

成果物のdebパッケージはpython-deb-pkgs下に出力されます。

```
 ls python-deb-pkgs/
 openrtm2-python3_2.1.0-0_amd64.changes  openrtm2-python3_2.1.0-0.dsc
 openrtm2-python3_2.1.0-0_amd64.deb      openrtm2-python3-example_2.1.0-0_amd64.deb
```

OpenRTM-aist-Pythonソースを変更してインストールしたい場合、build-python.sh スクリプトの以下の部分をコメントアウトし、build-python.sh、Dockerfile-python-debと同じディレクトリにOpenRTM-aist-Pythonソースを配置して実行してください。

```
 #----- OpenRTM-aist-Python
 echo "${password}" | sudo -S rm -rf ${TARGET}-*
 #--------　コメントアウト　ここから
 #rm -rf OpenRTM-aist-Python
 #git clone https://github.com/OpenRTM/OpenRTM-aist-Python
 #cd OpenRTM-aist-Python
 #git checkout ${BRANCH}
 #cd -
 #--------　コメントアウト　ここまで
```

## Javaソースのビルド

OpenRTM-aist-Java ソースには Dockerfile は含まれておりません。OpenRTM-aist-Javaのリリース用debパッケージ作成時に下記Dockerfileを利用しています。
- [ubuntu_2204/Dockerfile-java-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2204/Dockerfile-java-deb)
- [ubuntu_2404/Dockerfile-java-deb](https://github.com/n-kawauchi/RTM-src-pkgs-docker-build/blob/master/ubuntu_2404/Dockerfile-java-deb)

C++ソースビルドと同様に、Dockerでソースビルドからdebパッケージ生成まで行い、成果物であるdebパッケージをDockerコンテナからホスト側へコピーする処理までを一括で行うスクリプトを紹介します。

Ubuntu24.04用のdebパッケージを作成する場合の手順は以下となります。

```
 git clone https://github.com/n-kawauchi/RTM-src-pkgs-docker-build
 cd RTM-src-pkgs-docker-build/ubuntu_2404/
 sh build-java.sh
```

成果物のdebパッケージはjava-deb-pkgs下に、ソースパッケージはjava-src-pkgs下に出力されます。

```
 ls java-deb-pkgs/
 openrtm2-java_2.1.0-0_amd64.buildinfo  openrtm2-java_2.1.0-0_amd64.deb  openrtm2-java-doc_2.1.0-0_all.deb
 openrtm2-java_2.1.0-0_amd64.changes    openrtm2-java_2.1.0-0.dsc        openrtm2-java-example_2.1.0-0_amd64.deb
```

```
 ls java-src-pkgs/
 OpenRTM-aist-Java-2.1.0-jar.zip  OpenRTM-aist-Java-2.1.0.tar.gz  OpenRTM-aist-Java-2.1.0.zip
```

OpenRTM-aist-Javaソースを変更してインストールしたい場合、build-java.sh スクリプトの以下の部分をコメントアウトし、build-java.sh、Dockerfile-java-debと同じディレクトリにOpenRTM-aist-Javaソースを配置して実行してください。

```
 #----- OpenRTM-aist-Java
 echo "${password}" | sudo -S rm -rf ${TARGET}-*
 #--------　コメントアウト　ここから
 #rm -rf OpenRTM-aist-Java
 #git clone https://github.com/OpenRTM/OpenRTM-aist-Java
 #cd OpenRTM-aist-Java
 #git checkout ${BRANCH}
 #cd -
 #--------　コメントアウト　ここまで
```
