---
layout: page
title: ソースからのビルド (windows編、ランタイムライブラリ/mt・/mtd指定)
---
<br>
<a>No English version available.
</a>

<!-- Title: ソースからのビルド (Windows編、ランタイムライブラリ/MT・/MTd指定) -->
Visual Studio でランタイムライブラリにマルチスレッド(/MT)、マルチスレッドデバッグ(/MTd)を指定した RTC を開発する場合、/MT、/MTdの実行ファイルが他の DLL にリンクして処理を行うとヒープ破壊等で異常終了することがあります。
<!-- インストーラーで配布している OpenRTM-aist は マルチスレッドDLL(/MD)、マルチスレッドデバッグ DLL(/MDd) でビルドしてあるため正常に動作しません。 -->
マルチスレッド(/MT)、マルチスレッドデバッグ(/MTd)を指定したい場合は以下の手順で OpenRTM-aist の静的ライブラリを作成してください。

※動作確認はほとんどしていないため、以下の作業は全て自己責任で行ってください。

#contents
## OpenRTM-aist のビルド
### OpenRTM-aist のソースコードの入手
以下より OpenRTM-aist のソースコードを入手してください。

- [http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.2/OpenRTM-aist-1.1.2-win32.zip](http://www.openrtm.org/pub/OpenRTM-aist/cxx/1.1.2/OpenRTM-aist-1.1.2-win32.zip)

ダウンロードしたら適当な場所に展開してください。
この例では以下の位置に配置します。

```
 C:\openrtm_work\OpenRTM-aist
```

### omniORBの入手
以下より omniORB のバイナリパッケージを入手してください。
Visual Studioのバージョンにあったものを選んでください。

- [http://openrtm.org/pub/omniORB/win32/omniORB-4.1.7/](http://openrtm.org/pub/omniORB/win32/omniORB-4.1.7/)

ダウンロードしたら、OpenRTM-aist フォルダー内に omniORB という名前のフォルダーを作成して展開してください。

```
 C:\openrtm_work\OpenRTM-aist\omniORB
```


### 各種ファイルの編集
/MT、/MTd でビルドするために各種ファイルの編集を行います。

#### build.bat
以下の build.bat というバッチファイルを編集します。

```
 C:\openrtm_work\OpenRTM-aist\build.bat
```



環境によって以下の箇所を適宜変更してください。

```
 set RTM_ROOT=%~dp0
 set COIL_ROOT=%RTM_ROOT%\coil
 set OMNI_ROOT=%RTM_ROOT%\omniORB
 if not DEFINED ARCH       set ARCH=x86
 if not DEFINED VC_VERSION set VC_VERSION=12
 if not DEFINED PYTHON_DIR set PYTHON_DIR=c:\python27
 if not DEFINED RTM_VERSION set RTM_VERSION=1.1.2
 if not DEFINED OMNI_VERSION  set OMNI_VERSION=4.1.7
 if not DEFINED OMNITHREAD_VERSION set OMNITHREAD_VERSION=3.4
```


#### libRTC_vc**.vcxproj、libcoil_vc**.vcxproj、libRTCSkel_vc**.vcxproj
以下のlibRTC_vc12.vcxproj、libcoil_vc12.vcxproj、libRTCSkel_vc12.vcxprojというプロジェクトファイルを編集します。
Visual Studio のバージョンに合わせて libRTC_vc11.vcxproj、libcoil_vc11.vcxproj、libRTCSkel_vc11.vcxproj 等を編集するようにしてください。


- C:\openrtm_work\OpenRTM-aist\rtm\libRTC_vc12.vcxproj
- C:\openrtm_work\OpenRTM-aist\rtm\libcoil_vc12.vcxproj
- C:\openrtm_work\OpenRTM-aist\rtm\idl\libRTCSkel_vc12.vcxproj


まずはランタイムライブラリを変更します。
以下のように MultiThreadedDebugDLL と記載してある箇所を MultiThreadedDebug に変更します。
32bitか64bit かによって編集する箇所が違うのですが、両方変更しても問題ありません。

```
 <RuntimeLibrary>MultiThreadedDebugDLL</RuntimeLibrary>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <RuntimeLibrary>MultiThreadedDebug</RuntimeLibrary>
```


同様にMultiThreadedDLLもMultiThreadedに変更します。

```
 <RuntimeLibrary>MultiThreadedDLL</RuntimeLibrary>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <RuntimeLibrary>MultiThreaded</RuntimeLibrary>
```


次に動的ライブラリではなく静的ライブラリを生成するように変更します。
※libRTCSkel_vc12.vcxproj は元々静的ライブラリを生成するので変更の必要はありません。

DynamicLibraryをStaticLibrary に変更してください。

```
 <ConfigurationType>DynamicLibrary</ConfigurationType>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <ConfigurationType>StaticLibrary</ConfigurationType>
```

それに合わせて出力ファイル名も変更します。

```
 <OutputFile>$(OutDir)\RTC$(rtm_dllver).dll</OutputFile>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <OutputFile>$(OutDir)\RTC$(rtm_dllver).lib</OutputFile>
```

```
 <OutputFile>$(OutDir)\RTC$(rtm_dllver)d.dll</OutputFile>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <OutputFile>$(OutDir)\RTC$(rtm_dllver)d.lib</OutputFile>
```

```
 <OutputFile>$(OutDir)\coil$(coil_dllver).dll</OutputFile>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <OutputFile>$(OutDir)\coil$(coil_dllver).dll</OutputFile>
```

```
 <OutputFile>$(OutDir)\coil$(coil_dllver)d.dll</OutputFile>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <OutputFile>$(OutDir)\coil$(coil_dllver)d.dll</OutputFile>
```

また、ファイルをコピーするコマンドも変更します。


```
 <Command>copy &quot;$(OutDir)\\$(TargetName).lib&quot; &quot;$(SolutionDir)bin\\RTC$(rtm_dllver)d.lib&quot;&#x0D;&#x0A;copy &quot;$(OutDir)\\RTC$(rtm_dllver)d.dll&quot; &quot;$(SolutionDir)bin\\&quot;&#x0D;&#x0A;</Command>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <Command>copy &quot;$(OutDir)\\$(TargetName).lib&quot; &quot;$(SolutionDir)bin\\RTC$(rtm_dllver)d.lib&quot;&#x0D;&#x0A;</Command>
```

```
 <Command>copy &quot;$(OutDir)\\$(TargetName).lib&quot; &quot;$(SolutionDir)bin\\RTC$(rtm_dllver).lib&quot;&#x0D;&#x0A;copy &quot;$(OutDir)\\RTC$(rtm_dllver).dll&quot; &quot;$(SolutionDir)bin\\&quot;&#x0D;&#x0A;</Command>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <Command>copy &quot;$(OutDir)\\$(TargetName).lib&quot; &quot;$(SolutionDir)bin\\RTC$(rtm_dllver).lib&quot;&#x0D;&#x0A;;</Command>
```

```
 <Command>copy &quot;$(OutDir)\\$(TargetName).lib&quot; &quot;$(SolutionDir)bin\\coil$(coil_dllver)d.lib&quot;&#x0D;&#x0A;copy &quot;$(OutDir)\\coil$(coil_dllver)d.dll&quot; &quot;$(SolutionDir)bin\\&quot;&#x0D;&#x0A;</Command>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <Command>copy &quot;$(OutDir)\\$(TargetName).lib&quot; &quot;$(SolutionDir)bin\\coil$(coil_dllver)d.lib&quot;&#x0D;&#x0A;</Command>
```

```
 <Command>copy &quot;$(OutDir)\\$(TargetName).lib&quot; &quot;$(SolutionDir)bin\\coil$(coil_dllver).lib&quot;&#x0D;&#x0A;copy &quot;$(OutDir)\\coil$(coil_dllver).dll&quot; &quot;$(SolutionDir)bin\\&quot;&#x0D;&#x0A;</Command>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <Command>copy &quot;$(OutDir)\\$(TargetName).lib&quot; &quot;$(SolutionDir)bin\\coil$(coil_dllver).lib&quot;&#x0D;&#x0A;</Command>
```



OpenRTM-aist-1.1.2、omniORB-4.1.7 でエラーが発生するので、libRTC_vc12.vcxproj の PreprocessorDefinitionsにRTM_OMNIORB_41 を追加してください。OpenRTM-aist-1.2.0、もしくは omniORB-4.2.1 の場合は不要です。

```
 <PreprocessorDefinitions>LIBRARY_EXPORTS;WIN32;_DEBUG;_WINDOWS;_USRDLL;__WIN32__;__NT__;__OSVERSION__=4;__x86__;_WIN32_WINNT=0x0400;_CRT_SECURE_NO_DEPRECATE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <PreprocessorDefinitions>LIBRARY_EXPORTS;WIN32;_DEBUG;_WINDOWS;_USRDLL;__WIN32__;__NT__;__OSVERSION__=4;__x86__;_WIN32_WINNT=0x0400;_CRT_SECURE_NO_DEPRECATE;RTM_OMNIORB_41;%(PreprocessorDefinitions)</PreprocessorDefinitions>
```


#### rtm_config.props
omniORB のリンクするライブラリを変更します。
以下の rtm_config.props というファイルを編集してください。

```
 C:\openrtm_work\OpenRTM-aist\rtm_config.props
```

以下の箇所を変更します。
```
 <omni_lib>omniORB$(omni_dllver)_rt.lib;omniDynamic$(omni_dllver)_rt.lib;omnithread$(omnithread_dllver)_rt.lib</omni_lib>
 <omni_libd>omniORB$(omni_dllver)_rtd.lib;omniDynamic$(omni_dllver)_rtd.lib;omnithread$(omnithread_dllver)_rtd.lib</omni_libd>
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 <omni_lib>omniORB4.lib;omniDynamic4.lib;omnithread.lib</omni_lib>
 <omni_libd>omniORB4d.lib;omniDynamic4d.lib;omnithreadd.lib</omni_libd>
```


### ビルド
build.bat を起動したらビルドを開始します。
終了したら、binフォルダーに以下のファイルが生成されているかを確認してください。

- libRTCSkel.lib
- libRTCSkeld.lib
- coil112_vc12.lib
- coil112_vc12d.lib
- RTC112_vc12.lib
- RTC112_vc12d.lib

※サンプルコンポーネントや rtcd、rtcprof のコンパイルで大量にエラーが出ますが、自分の RTC をビルドするだけならば必要ないので無視してください。



### OpenRTMConfig.cmakeの編集
omniORB のリンクするライブラリ名が変わったのと、新たにリンクするライブラリを追加する必要があるため以下のファイルを編集します。

- C:\openrtm_work\OpenRTM-aist\cmake\OpenRTMConfig.cmake

```
 set(OMNIORB_LIBRARIES optimized;omniORB417_rt;
                       optimized;omniDynamic417_rt;
                       optimized;omnithread34_rt;
                       debug;omniORB417_rtd;
                       debug;omniDynamic417_rtd;
                       debug;omnithread34_rtd)
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 set(OMNIORB_LIBRARIES optimized;omniORB4;
                       optimized;omniDynamic4;
                       optimized;omnithread;
                       debug;omniORB4d;
                       debug;omniDynamic4d;
                       debug;omnithreadd)
```

```
 set(OPENRTM_LIBRARIES optimized;RTC112_vc12;
                       optimized;coil112_vc12;
                       optimized;omniORB4_rt;
                       optimized;omniDynamic4_rt;
                       optimized;omnithread4_rt;
                       optimized;advapi32;
                       optimized;ws2_32;
                       optimized;mswsock;
                       debug;RTC112_vc12d;
                       debug;coil112_vc12d;
                       debug;omniORB4_rtd;
                       debug;omniDynamic4_rtd;
                       debug;omnithread4_rtd;
                       debug;advapi32;
                       debug;ws2_32;
                       debug;mswsock)
```
<div align="center"><a href="arrow.png"><img src="arrow.png" width="30%;"></a></div>
```
 set(OPENRTM_LIBRARIES optimized;RTC112_vc12;
                       optimized;coil112_vc12;
                       optimized;omniORB4;
                       optimized;omniDynamic4;
                       optimized;omnithread;
                       optimized;advapi32;
                       optimized;ws2_32;
                       optimized;mswsock;
                       optimized;libRTCSkel;
                       optimized;rpcrt4;
                       debug;RTC112_vc12d;
                       debug;coil112_vc12d;
                       debug;omniORB4d;
                       debug;omniDynamic4d;
                       debug;omnithreadd;
                       debug;advapi32;
                       debug;ws2_32;
                       debug;mswsock;
                       debug;libRTCSkeld;
                       debug;rpcrt4)
```

※このファイルは再度 OpenRTM-aist をビルドすると上書きするので注意してください。

## RTCのビルド
次に/MT、/MTd を設定してビルドしたいRTCのファイルを編集します。
srcフォルダーの CMakeLists.txt を編集します。
以下の記述を追加することで、ランタイムライブラリを/MT、/MTdに設定します。

```
 set(CMAKE_CXX_FLAGS_RELEASE "/MT")
 set(CMAKE_CXX_FLAGS_DEBUG "/MTd")
```


次にビルドに使用する OpenRTM-aist、omniORB を先ほどビルドしたものに設定して RTC のビルドを行います。
コマンドプロンプトより、以下のコマンドを入力して変数を設定してください。

```
 set RTM_ROOT=C:\openrtm_work\OpenRTM-aist
 set VC_VERSION=12
 set OMNI_ROOT=C:\openrtm_work\OpenRTM-aist\omniORB
 set OpenRTM_DIR=C:\openrtm_work\OpenRTM-aist\cmake
```

Visual Studio のバージョンなどによって適宜変更してください。

最後に以下のコマンドでビルドすれば完了です。

```
 cmake .
 cmake --build . --config Debug
```


## エラーの原因について
/MTの実行ファイルが何らかのDLLとリンクした状態で動作すると以下のエラーメッセージが表示されることがあります。

```
 Expression: _pFirstBlock == pHead
```

実行ファイル側で確保したメモリをDLL側で開放したりすると発生します。

- DLL側

```
__declspec(dllexport) void deleteData(char* v)
{
	delete v;
}
```

- 実行ファイル側

```
void deleteData(char* v);

int main(void)
{
	char *v = new char[1000];
	deleteData(v);
}
```

これはランタイムライブラリに /MT、/MTd を指定した場合、ヒープ領域が実行ファイルと DLL で別に作成されるためヒープ破壊が発生することがあるようです。
ただし確実に発生するわけではなく、例えば deleteData 関数実行前に print文を入れると何故か発生しなかったりします。
この場合、後になって全然関係ない箇所で落ちたりするので原因特定が非常に難しくなります。

一方、ランタイムライブラリに /MD、/MDd を指定した場合、ヒープ領域は共有するためこのような問題は発生しません。


OpenRTM-aist、あるいは omniORB のどこで異常が発生しているのかを調べて修正するのは無理だと思うので、基本的にはランタイムライブラリには /MD、/MDd を使うようにしてください。

どうしてもランタイムライブラリに /MT、/MTd を設定したい場合は、上記の方法で静的ライブラリを作成してください。

上記の方法で /MT、/MTd 指定の RTC が一応動作できるようにはなりますが、omniORB と coil が advapi32.dll という名前のライブラリにリンクしており、advapi32.dll が /MD のランタイムライブラリ(MSVCRT)を使用しているため、ここで何が起こるかは分かりません。

