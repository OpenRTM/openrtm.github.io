---
layout: page
title: チュートリアル(画像処理実習)
---

<!-- チュートリアル(画像処理実習) -->
#contents

## はじめに

このページでは、OpenCVの画像処理により図形を検出して移動ロボット (Raspberry Piマウス) を追従させるRTCの作成手順を説明します。

## 作成するRTコンポーネント

- CircleTracking コンポーネント：OpenCVライブラリのHoughCircles関数で画像から円を検出して、検出した円の方向に移動ロボットが回転するように制御するRTC

<div align="center"><a href="opencv10.jpg"><img src="opencv10.jpg" width="50%;"></a></div>


## HoughCircles関数について

HoughCirclesはハフ変換を用いてグレースケール画像から円を検出する関数です。
詳細は以下のページを参照。

- [特徴検出 — opencv 2.2 documentation](http://opencv.jp/opencv-2svn/cpp/feature_detection.html#cv-houghcircles)

## RTCの概要

カメラで取得した画像をグレースケール画像に変換後、HoughCircles関数で円を検出します。
検出した円の方向に移動ロボットが回転するように制御します。
具体的には、検出した円の位置が画像の右側の場合は右回り、左側の場合は左回りの回転する目標速度を指令します。
また、動作確認用に円の位置情報を付加した画像を出力します。

<div align="center"><a href="opencv2.jpg"><img src="opencv2.jpg" width="100%;"></a></div>

## RTCの作成
以降はRTCの基本的な作成方法を理解している前提で進めます。
基本的な作成手順は以下のページを参照。

- [チュートリアル(Raspberry Pi Mouse、RTM講習会)]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar)

### RTCBuilderによるひな型コード生成

RTCBuilderで、以下の仕様のRTCのひな型コードを生成します。

<table class="table-alt">
  <tr>
    <th>コンポーネント名称</th>
    <th>CircleTracking</th>
  </tr>
  <tr>
    <td>アクティビティ</td>
    <td>onActivated、onDeactivated、onExecute</td>
  </tr>
  <tr>
    <td>言語</td>
    <td>C++</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>image_in</td>
  </tr>
  <tr>
    <td>型</td>
    <td>RTC::CameraImage</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>入力画像</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">InPort</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>velocity_in</td>
  </tr>
  <tr>
    <td>型</td>
    <td>RTC::TimedVelocity2D</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>変更前の目標速度</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>image_out</td>
  </tr>
  <tr>
    <td>型</td>
    <td>RTC::CameraImage</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>円の情報を付加した画像</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">OutPort</td>
  </tr>
  <tr>
    <td>ポート名</td>
    <td>velocity_out</td>
  </tr>
  <tr>
    <td>型</td>
    <td>RTC::TimedVelocity2D</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>変更後の目標速度</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>speed_r</td>
  </tr>
  <tr>
    <td>型</td>
    <td>double</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>0.5</td>
  </tr>
  <tr>
    <td>制約</td>
    <td>0.0&lt;x&lt;2.0</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>slider</td>
  </tr>
  <tr>
    <td>Step</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>図形の位置により、右回転、左回転する場合の回転速度</td>
  </tr>
  <tr>
    <td>Configuration</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>houghcircles_dp</td>
  </tr>
  <tr>
    <td>型</td>
    <td>double</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>text</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>HoughCircles関数の引数dp</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>houghcircles_minDist</td>
  </tr>
  <tr>
    <td>型</td>
    <td>double</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>30</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>text</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>HoughCircles関数の引数minDist</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>houghcircles_param1</td>
  </tr>
  <tr>
    <td>型</td>
    <td>double</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>100</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>text</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>HoughCircles関数の引数param1</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>houghcircles_param2</td>
  </tr>
  <tr>
    <td>型</td>
    <td>double</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>100</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>text</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>HoughCircles関数の引数param2</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>houghcircles_minRadius</td>
  </tr>
  <tr>
    <td>型</td>
    <td>int</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>text</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>HoughCircles関数の引数minRadius</td>
  </tr>
  <tr>
    <td colspan="2" style="text-align: center;">Configuration</td>
  </tr>
  <tr>
    <td>パラメーター名</td>
    <td>houghcircles_maxRadius</td>
  </tr>
  <tr>
    <td>型</td>
    <td>int</td>
  </tr>
  <tr>
    <td>デフォルト値</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Widget</td>
    <td>text</td>
  </tr>
  <tr>
    <td>説明</td>
    <td>HoughCircles関数の引数maxRadius</td>
  </tr>
</table>

## RTC::CameraImage型について

RTC::CameraImage型は画像データを格納するデータ型です。

```
    struct CameraImage
    {
        /// Time stamp.
        Time tm;
        /// Image pixel width.
        unsigned short width;
        /// Image pixel height.
        unsigned short height;
        /// Bits per pixel.
        unsigned short bpp;
        /// Image format (e.g. bitmap, jpeg, etc.).
        string format;
        /// Scale factor for images, such as disparity maps, where the integer pixel value should be divided by this factor to get the real pixel value.
        double fDiv;
        /// Raw pixel data.
        sequence<octet> pixels;
    };
```

このデータ型には、画像の幅**width**、画像の高さ**height**、画像データ**pixels**等を設定できます。

<div align="center"><a href="CameraImage.png"><img src="CameraImage.png" width="50%;"></a></div>

## ファイル編集

以下のファイルを編集します。

- src/CMakeLists.txt
- include/CircleTracking/CircleTracking.h
- src/CircleTracking.cpp


### src/CMakeLists.txtの編集

**src**フォルダの**CMakeLists.txt**をメモ帳などで開いて編集してください。
ここでは、OpenCVを利用するための設定を行います。

以下のように**find_package**によりOpenCVのライブラリを検出します。
find_packageの行を追加してください。

```
 set(comp_srcs CircleTracking.cpp )
 set(standalone_srcs CircleTrackingComp.cpp)
 
 find_package(OpenCV REQUIRED) #追加
```

次にリンクするライブラリに、OpenCVのライブラリを追加します。
以下の2か所を変更します。

```
 # target_link_libraries(${PROJECT_NAME} ${OPENRTM_LIBRARIES}) #修正前
 target_link_libraries(${PROJECT_NAME} ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) #修正後、${OpenCV_LIBS}を追加する
```

```
 # target_link_libraries(${PROJECT_NAME}Comp ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) #修正前
 target_link_libraries(${PROJECT_NAME}Comp  ${OPENRTM_LIBRARIES} ${OpenCV_LIBS}) #修正後、${OpenCV_LIBS}を追加する
```


### include/CircleTracking/CircleTracking.h

**include/CircleTracking/CircleTracking.h**の編集を行います。
まず、37行目付近でインクルードファイルを記述します。

```
 #include <rtm/DataInPort.h>
 #include <rtm/DataOutPort.h>
 
 #include <opencv2/opencv.hpp> //追加
```


314行目付近に**private:**という記述があるため、その下に**m_imageBuff**、**m_outputBuff**、**m_direction**の3つのメンバ変数を追加します。

```
 private:
   cv::Mat m_imageBuff; //追加、入力画像を格納する変数
   cv::Mat m_outputBuff; //追加、円の情報を付加した画像を格納する変数
   int m_direction; //追加、移動ロボットの回転方向を格納する変数
```

### src/CircleTracking.cpp

**src/CircleTracking.cpp**の編集を行います。
**onActivated**、**onDeactivated**、**onExecute**の3つの関数を編集します。


```
 RTC::ReturnCode_t CircleTracking::onActivated(RTC::UniqueId /*ec_id*/)
 {
   // OutPortの画面サイズを0に設定
   m_image_out.width = 0;
   m_image_out.height = 0;
 
   //進行方向を0(回転方向を指定しない)に設定
   m_direction = 0;
   return RTC::RTC_OK;
 }
```

```
 RTC::ReturnCode_t CircleTracking::onDeactivated(RTC::UniqueId /*ec_id*/)
 {
   if (!m_outputBuff.empty())
   {
     // 画像用メモリの解放
     m_imageBuff.release();
     m_outputBuff.release();
   }
 
   return RTC::RTC_OK;
 }
```

```
 RTC::ReturnCode_t CircleTracking::onExecute(RTC::UniqueId /*ec_id*/)
 {
   if (m_image_inIn.isNew()) {
     cv::Mat gray;
     std::vector<cv::Vec3f> circles;
     // 画像データの読み込み
     m_image_inIn.read();
 
     // InPortとOutPortの画面サイズ処理およびイメージ用メモリの確保
     if (m_image_in.width != m_image_out.width || m_image_in.height != m_image_out.height)
     {
       m_image_out.width = m_image_in.width;
       m_image_out.height = m_image_in.height;
 
       m_imageBuff.create(cv::Size(m_image_in.width, m_image_in.height), CV_8UC3);
       m_outputBuff.create(cv::Size(m_image_in.width, m_image_in.height), CV_8UC3);
 
     }
 
     // InPortの画像データをm_imageBuffにコピー
     std::memcpy(m_imageBuff.data, (void*)&(m_image_in.pixels[0]), m_image_in.pixels.length());
 
     //カラー画像をグレースケールに変換
     cv::cvtColor(m_imageBuff, gray, cv::COLOR_BGR2GRAY);
 
     //HoughCircles関数で円を検出する
     cv::HoughCircles(gray, circles, cv::HOUGH_GRADIENT, m_houghcircles_dp, m_houghcircles_minDist, 
       m_houghcircles_param1, m_houghcircles_param2, m_houghcircles_minRadius, m_houghcircles_maxRadius);
 
     
     //円を検出できた場合の処理
     if (!circles.empty())
     {
       //円の位置が画像の左側の場合は左回りに回転するように設定
       if (circles[0][0] < gray.cols / 2)
       {
         m_direction = 1;
       }
       //円の位置が画像の右側の場合は右回りに回転するように設定
       else
       {
         m_direction = 2;
       }
     }
     //円を検出できなかった場合は回転方向の指定をしないように設定
     else
     {
       m_direction = 0;
     }
 
     //元のカラー画像をコピーして円の情報を画像に追加
     m_outputBuff = m_imageBuff.clone();
 
     for (auto circle : circles)
     {
       cv::circle(m_outputBuff, cv::Point(static_cast<int>(circle[0]), static_cast<int>(circle[1])), static_cast<int>(circle[2]), cv::Scalar(0, 0, 255), 2);
     }
 
     // 画像データのサイズ取得
     int len = m_outputBuff.channels() * m_outputBuff.cols * m_outputBuff.rows;
     m_image_out.pixels.length(len);
 
     // 円の情報を付加した画像データをOutPortにコピー
     std::memcpy((void*)&(m_image_out.pixels[0]), m_outputBuff.data, len);
     //画像データを出力
     m_image_outOut.write();
   }
 
   if (m_velocity_inIn.isNew()) {
     //速度指令値を読み込み
     m_velocity_inIn.read();
     m_velocity_out = m_velocity_in;
     
     //円が画像の左側にある場合、左回りに回転する
     if (m_direction == 1)
     {
       m_velocity_out.data.va = m_speed_r;
     }
     //円が画像の右側にある場合、右回りに回転する
     else if (m_direction == 2)
     {
       m_velocity_out.data.va = -m_speed_r;
     }
     //速度指令値を出力
     m_velocity_outOut.write();
   }
   return RTC::RTC_OK;
 }
```

## RTシステムの構築、動作確認

ここからはRTSystemEditorで作業します。
Raspberry Piマウスを使用する場合は、Raspberry Piのアクセスポイントに接続した状態で作業してください。
以下のページのRobotControllerコンポーネントが必要なため、実機での動作確認まで進めておいてください。

- [チュートリアル(RTコンポーネントの作成入門、Raspberry Pi Mouse、Windows)]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar/tutorial_rtm_seminar_win_part2)
- [チュートリアル(RTコンポーネントの作成入門、Raspberry Pi Mouse、Ubuntu)]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar/tutorial_rtm_seminar_ubuntu_part2)


### 事前準備

動作確認には、Raspberry Piマウス、USBカメラ、カメラ用マウント、LiDAR付属のネジ、円形状の図形を印刷した紙が必要です。
講習会ではUSBカメラとカメラ用マウントは接続済みです。紙も配布しています。


<div align="center"><a href="DSC04155.JPG"><img src="DSC04155.JPG" width="50%;"></a></div>

専用LiDARマウントかマルチLiDARマウントかで使用するネジが異なります。

まず、以下の専用LiDARマウントの場合は、ネジは2個付属しているので、それを使用してください。

<div align="center"><a href="DSC04139.JPG"><img src="DSC04139.JPG" width="50%;"></a></div>

<div align="center"><a href="DSC04152.JPG"><img src="DSC04152.JPG" width="50%;"></a></div>

以下のマルチLiDARマウントの場合は、なべタッピングネジ3-8を使用してください。

<div align="center"><a href="DSC04142.JPG"><img src="DSC04142.JPG" width="50%;"></a></div>

<div align="center"><a href="DSC04151.JPG"><img src="DSC04151.JPG" width="50%;"></a></div>

以下のようにRaspberry Piマウス前方の2か所で固定します。

<div align="center"><a href="DSC04153.JPG"><img src="DSC04153.JPG" width="100%;"></a></div>

PCとUSBカメラをUSBポートで接続してください。

<div align="center"><a href="DSC04154.JPG"><img src="DSC04154.JPG" width="100%;"></a></div>


### 動作確認

#### RTCの起動
動作確認には、以下の5つのRTCの起動が必要です。

- RaspberryPiMouseRTC
- RobotController
- OpenCVCamera
- CameraViewer
- CircleTracking


RaspberryPiMouseRTCとRobotControllerコンポーネントの起動ついては、以下のページの手順を参考にしてください。

- [チュートリアル(RTコンポーネントの作成入門、Raspberry Pi Mouse、Windows)]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar/tutorial_rtm_seminar_win_part2)
- [チュートリアル(RTコンポーネントの作成入門、Raspberry Pi Mouse、Ubuntu)]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar/tutorial_rtm_seminar_ubuntu_part2)

OpenCVCamera、CameraViewerはOpenRTM-aist付属のサンプルコンポーネントです。
Windows 10の場合は、画面左下の「ここに入力して検索」に**C++_OpenCV-Examples**と入力して、C++_OpenCV-Examplesを選択したら起動するエクスプローラから**CameraViewer.bat**と**OpenCVCamera.bat**をダブルクリックして実行してください。

<div align="center"><a href="opencv8.jpg"><img src="opencv8.jpg" width="70%;"></a></div>

Ubuntuの場合はビルドとインストール作業が必要です。

- [LinuxにおけるOpenCVサンプルのビルド手順]({{ site.baseurl }}/ja/doc/installation/sample_components/opencvcamera/opencv_sample_build)

CircleTrackingはビルドで生成したCircleTrackingComp.exeを実行してください。

#### RTシステムの構築

RTSystemEditor上で以下のようにポートを接続してください。

<div align="center"><a href="opencv3.jpg"><img src="opencv3.jpg" width="100%;"></a></div>

<table class="table-alt">
  <tr>
    <th>RTC名</th>
    <th>OutPort名</th>
    <th>RTC名</th>
    <th>InPort名</th>
  </tr>
  <tr>
    <td>OpenCVCamera0</td>
    <td>out</td>
    <td>CircleTracking0</td>
    <td>image_in</td>
  </tr>
  <tr>
    <td>RobotController0</td>
    <td>out</td>
    <td>CircleTracking0</td>
    <td>velocity_in</td>
  </tr>
  <tr>
    <td>CircleTracking0</td>
    <td>image_out</td>
    <td>CameraViewer0</td>
    <td>in</td>
  </tr>
  <tr>
    <td>CircleTracking0</td>
    <td>velocity_out</td>
    <td>RaspberryPiMouseRTC0</td>
    <td>target_velocity_in</td>
  </tr>
  <tr>
    <td>RaspberryPiMouseRTC0</td>
    <td>ir_sensor_out</td>
    <td>RobotController</td>
    <td>in</td>
  </tr>
</table>

RTCをアクティブ化すれば動作確認を開始します。

カメラの前で円形状の図形を印刷した紙を左右に動かして、動作を確認してください。

<div align="center"><a href="opencv9.png"><img src="opencv9.png" width="70%;"></a></div>

OpenCVCameraコンポーネントがRaspberry Piマウスに取り付けたUSBカメラではなく、別のUSBカメラやノートPC内蔵カメラを使用する場合があります。
この場合は他のカメラの画像が表示されているので、RTSystemEditorでOpenCVCamera0を選択して、コンフィギュレーションパラメータを編集します。

<div align="center"><a href="opencv4_2.jpg"><img src="opencv4_2.jpg" width="70%;"></a></div>

以下の**device_num**を変更して確認してください。

<div align="center"><a href="opencv5_2.jpg"><img src="opencv5_2.jpg" width="70%;"></a></div>

また、円の誤検出が多い場合、RTSystemEditorでCircleTracking0を選択して、コンフィギュレーションパラメータを変更して試してみてください。

<div align="center"><a href="opencv6_2.jpg"><img src="opencv6_2.jpg" width="70%;"></a></div>

HoughCircles関数の引数の詳細についてはOpenCVのドキュメントを参考にしてください。

<div align="center"><a href="opencv7_2.jpg"><img src="opencv7_2.jpg" width="70%;"></a></div>


## Raspberry Piに接続したUSBカメラを使う

OpenCVCameraコンポーネントをRaspberry Pi上で起動して、Raspberry Piに接続したUSBカメラの画像をPCに送信して処理するシステムを構築します。
USBカメラをRaspberry Piに接続してください。

<div align="center"><a href="sytemopencvcamera.png"><img src="sytemopencvcamera.png" width="100%;"></a></div>

まず、OpenCVCameraコンポーネントはWebブラウザ上の操作で起動できるようになっていないため、Tera TermによりRaspberry Pi上のLinuxにSSHログインして操作します。

- [TeraTerm](https://teratermproject.github.io/)

Tera Term起動後に、ホストに**192.168.11.1**と入力してLinuxと接続します。
ユーザー名とパスフレーズは講習会で説明しています。

ログイン後、Tera Termから以下のコマンドを実行することで、予めインストールしておいたOpenCVCameraコンポーネントを起動できます。

```
 /usr/local/share/openrtm-1.2/components/c++/opencv-rtcs/OpenCVCamera/OpenCVCameraComp
```

Raspberry Pi上で起動したOpenCVCamera0をCircleTracking0のデータポートと接続してください。
PCで起動したOpenCVCamera0は不要のため終了してください。

<div align="center"><a href="systemopencv2.png"><img src="systemopencv2.png" width="100%;"></a></div>

動作確認すると分かりますが、無線LANで送受信するカメラ画像データが大きいため、PC上でカメラ画像を表示すると遅延が大きい事が分かります。
このため、圧縮した画像を送受信するように変更します。

まず、OpenCVCamera0のコンフィギュレーションのパラメータで、**string_encode**を**jpeg**に変更します。

次に、CircleTrackingコンポーネントを一旦終了して、以下のようにonExecute関数を変更します。

```
 RTC::ReturnCode_t CircleTracking::onExecute(RTC::UniqueId /*ec_id*/)
 {
    (中略)
       m_outputBuff.create(cv::Size(m_image_in.width, m_image_in.height), CV_8UC3);
 
     }
     (以下を追加)
     //圧縮のフォーマットにより処理を分岐
     std::string format = (const char*)m_image_in.format;
     if (format == "jpeg" || format == "png")
     {
        std::vector<uchar> buff;
        int len = m_image_in.pixels.length();
        buff.resize(len);
        memcpy(&buff[0], &m_image_in.pixels[0], sizeof(unsigned char) * len);
        m_imageBuff = cv::imdecode(cv::Mat(buff), cv::IMREAD_COLOR);
     }
     else
     {
        std::memcpy(m_imageBuff.data,
            (void*)&(m_image_in.pixels[0]),
            m_image_in.pixels.length());
     }
     //以下の部分はコメントアウト。
     /*
     // InPortの画像データをm_imageBuffにコピー
     std::memcpy(m_imageBuff.data,
            (void *)&(m_image_in.pixels[0]),
            m_image_in.pixels.length());
     */
```

CircleTrackingコンポーネントをビルド後、RTC起動とデータポートの接続して動作確認してみてください。
