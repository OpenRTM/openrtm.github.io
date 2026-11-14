---
layout: page
title: rtshell
---

<!-- Title: rtshell -->
#contents

## Introduction

rtshell is a tool that allows you to manage RT Components registered on a name server from the shell.
You can activate/deactivate/reset components and connect ports.
You can also manage RT systems.

This tool is useful for systems with limited resources, environments where a GUI cannot be used (especially environments that are not connected via a network to another PC used to manage components), environments where RTSystemEditor cannot be used, and cases where an RT System is built using scripts. It is also a useful tool for people who are familiar with using the command line.

<!-- このソフトウエアはNEDO(独立行政法人新エネルギー産業技術総合開発機構)の次世代ロボット知能化技術開発プロジェクトの支援により、独立行政法人産業技術総合研究所によって開発されています。 -->
<!-- 管理番号H23PRO-1214。 -->

<!-- This software is licensed under the GNU Lesser General Public License version 3 -->
<!-- (LGPL3). See LICENSE.txt. -->
<!--  -->

## Requirements

- rtctree is required.
- rtsprofile is required.
- Python 3 or later and OpenRTM-aist-Python are required.
  - For details on supported Python versions, please check the [download page]({{ site.baseurl }}/en/download/openrtm-aist-cpp/openrtm-aist-cpp_1_2_2_release#toc1).


<!-- pipによりインストールする場合は、trctreeとrtsprofileは自動的にインストールされます。 -->


## Installation

For installation instructions, see the [Installing rtshell]({{ site.baseurl }}/en/doc/installation/install_rtshell) page.
<!-- インストールはいくつかの方法が利用可能です。 -->
<!--  -->
<!-- - (好ましい方法) pipを利用してPyPiからインストールする。 -->
<!--  -->
<!-- ++ 必要にお応じてpipをインストールします。 -->
<!-- https://pip.pypa.io/en/latest/installing/を参照してください。 -->
<!-- ++ pipを実行します。 -->
<!-- $ pip install rtshell -->
<!-- ++ 以下のコマンドを実行し、インストール後のアクションを行います。 -->
<!-- $ rtshell_post_install -->
<!-- ++ Windows上では、必要に応じて環境変数を設定します。通常デフォルトで設定されていますが、設定されていない場合は自分で設定する必要があります。 -->
<!-- PythonスクリプトのディレクトリがPATH環境変数に設定されていることを確認してください。通常、これらはC:\Python27\Scripts\です（PythonがC:\Python27\にインストールされた場合）。 -->
<!-- ++ リポジトリまたはソースアーカイブからダウンロード後、適当なディレクトリで解凍し、インストールする。 -->
<!-- ++ ソースを展開します。 -->
<!-- $ cd /home/blurgle/src/ -->
<!-- $ tar -xvzf rtshell.tar.gz -->
<!-- ++ setup.pyを実行します。 -->
<!-- $ python setup.py install -->
<!-- ++ 以下のコマンドを実行し、インストール後のアクションを行います。 -->
<!-- $ rtshell_post_install -->
<!-- ++ Windows上では、必要に応じて環境変数を設定します。通常デフォルトで設定されていますが、設定されていない場合は自分で設定する必要があります。 -->
<!-- PythonスクリプトのディレクトリがPATH環境変数に設定されていることを確認してください。通常、これらはC:\Python27\Scripts\です（PythonがC:\Python27\にインストールされた場合）。 -->
<!-- Windows上では、インストーラープログラムを利用してインストール可能です。 -->
<!--  -->

## Repository

The latest source code is available in the GitHub repository (URL: http://github.com/OpenRTM/rtshell).
You can download it by clicking [Download ZIP]. You can also use the "git clone" command as shown below. (git must be installed beforehand.)

```
  $ git clone git://github.com/OpenRTM/rtshell.git
```


## Documentation

On Linux, the documentation is provided as man pages and installed in /usr/local/share/man. On Windows, it is provided in HTML format, and the English and Japanese versions are copied under the en and ja directories under <python directory>\Lib\site-packages\rtshell\data\doc\html, respectively. It is also published on this website.

<!-- このパスを$MANPATHという環境変数に追加する必要な場合があります。例えば、rtshellのmanページが/usr/local/share/manにインストールされた場合、以下の行を.bashrcに追加してください。 -->
<!-- export MANPATH=/usr/local/share/man:${MANPATH} -->

<!-- **テストの実行 -->
<!--  -->
<!-- コマンドのテストはソースディレクトリから実行できます: -->
<!--  -->
<!-- ~/src/rtshell $ ./test/test_cmds.py ~/share/OpenRTM-aist/examples/rtcs/ -->
<!--  -->
<!-- 変数はRTCのモジュールを持つディレクトリです。Motor、ControllerおよびSensorのモジュールが必要です。 -->
<!--  -->
<!-- 一つのコマンドのテストだけを実行するの場合、そのテストの名を変数に追加してください。: -->
<!--  -->
<!-- $ ./test/test_cmds.py ~/share/OpenRTM-aist/examples/rtcs/ rtactTests -->

<hr>

Not yet created below.

- [rtshell Command Reference](./command_reference)
- [rtctree Module](./rtctree)
- [rtsprofile Module](./rtsprofile)

