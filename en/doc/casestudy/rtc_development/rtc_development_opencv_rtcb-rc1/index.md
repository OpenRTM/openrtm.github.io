---
layout: page
title: creating rt components (opencv edition for rtcb-rc1)
---

<!-- Title: RTコンポーネント作成(OpenCV編 for RTCB-RC1) -->
#contents

## Introduction
This section introduces the procedure for creating an RT component from the OpenCV library using VC9.

### What Is OpenCV? 

[OpenCV](http://opencv.jp/) is an open-source computer vision library developed and released by Intel.

Excerpt from [Wikipedia](http://ja.wikipedia.org/wiki/OpenCV).

### RT Components to Be Created 

- Flip component: An RT component that flips images using the cvFlip() function from the OpenCV library.

- ObjectTracking component: A component that uses the OpenCV library to track an object selected with the mouse.
It has functions such as displaying the image being tracked, outputting the tracking image from an OutPort, and outputting the displacement of the tracked object from an OutPort.

## Creating an RT Component from the OpenCV Library (Flip Component) 
Here, we create an RT component in VC9 from cvFlip(), a function in the OpenCV library that flips images.

The following is the workflow.

- About the cvFlip function
- Component overview
- Operating environment and development environment
- Generating the Flip component template
- Implementing activity processing
- Checking component operation

### About the cvFlip Function

The cvFlip function flips a two-dimensional array vertically, horizontally, or along both axes.

```
 void cvFlip(IplImage* src, IplImage* dst=NULL, int flip_mode=0);
 #define cvMirror cvFlip

 src       入力配列
 dst       出力配列。もし dst=NULL であれば、src が上書きされます。
 flip_mode 配列の反転方法の指定内容:
 　flip_mode = 0: X軸周りでの反転(上下反転)
 　flip_mode > 0: Y軸周りでの反転(左右反転)
 　flip_mode < 0: 両軸周りでの反転(上下左右反転)
```
### Component Overview 
A component that flips an input image from an InPort and outputs it from an OutPort.
<br>
The target axis for flipping is specified using the RTC configuration function with a parameter named flip_mode.

Specify flip_mode as follows according to the direction in which you want to flip the image.

- To flip vertically, specify 0

- To flip horizontally, specify 1

- To flip vertically and horizontally, specify -1

<br>

The specifications of the RTC to be created are as follows.

- InPort
  - Captured image data (TimedOctetSeq)

- OutPort
  - Flipped image data (TimedOctetSeq)

- Configuration
  - Flip method specification (int)
* The TimedOctetSeq type is a data type defined in BasicDataType.idl of OpenRTM-aist as follows.

* The octet type is a basic CORBA IDL type, and is an 8-bit value that is guaranteed not to undergo any data conversion during transfer.

```
   struct Time
  {
        unsigned long sec;    // sec
        unsigned long nsec;   // nano sec
  };

   struct TimedOctetSeq
  {
        Time tm;
        sequence<octet> data;
  };
```


<br>
Figure 1 shows an image of the image processing for each flip_mode.

<br>

<br>

<div align="center"><a href="cvFlip_and_FlipRTC.png"><img src="cvFlip_and_FlipRTC.png" width="70%;"></a></div>
<div align="center"><strong>Figure 1. flip_mode specification patterns of the Flip component</strong></div>
<br>

### Operating Environment and Development Environment
- OS: Windows XP SP2
- Compiler: [Visual C++ 2008 Express Edition Japanese Version](http://www.microsoft.com/japan/msdn/vstudio/express/default.aspx)
- [omniORB: version 4.1.2](http://www.openrtm.org/pub/Windows/omniORB/omniORB-4.1.2_vc9.msi)
- [OpenCV: version 1.0](http://downloads.sourceforge.net/opencvlibrary/OpenCV_1.0.exe?modtime=1161287502&big_mirror=1)
- [OpenRTM-aist: version 1.0.0-RC1]()(No corresponding page available.)

- [OpenCV sample RTC]()(No corresponding page available.)

- RTSystemEditor 1.0
- RTCBuilder 1.0
  - [All-in-one package]()(No corresponding page available.)

- [Extraction tool (Lhaplus)](http://www.forest.impress.co.jp/lib/arc/archive/archiver/lhaplus.html)

### Generating the Flip Component Template

The Flip component template is generated using RTCBuilder.

### Starting RTCBuilder
When you start Eclipse by specifying a new workspace, the following "Welcome" screen is displayed.
Clicking the "X" at the upper left of this "Welcome" screen displays the following screen.
<br>

<div align="center"><a href="fig1-1EclipseInit.png"><img src="fig1-1EclipseInit.png" width="70%;"></a></div>
<!-- CENTER:''図 1-1 Eclipseの初期起動時の画面'' -->
<div align="center"><strong>Figure 2. Screen at initial startup of Eclipse</strong></div>
<br>
Click the [Open Perspective] button at the upper right and select "Other..." from the pull-down menu.
<br>

<div align="center"><a href="fig2-2PerspectiveSwitch.png"><img src="fig2-2PerspectiveSwitch.png" width="70%;"></a></div>
<!-- CENTER:''図 2-2 パースペクティブの切り替え'' -->
<div align="center"><strong>Figure 3. Switching perspectives</strong></div>
<br>
Select "RTC Builder" and click the [OK] button.

<div align="center"><a href="fig2-3PerspectiveSelection.png"><img src="fig2-3PerspectiveSelection.png" width="30%;"></a></div>
<!-- CENTER:''図 2-3　パースペクティブの選択'' -->
<div align="center"><strong>Figure 4. Selecting a perspective</strong></div>
<br>
RTCBuilder starts.
<br>

<div align="center"><a href="fig2-4RTCBuilderInit.png"><img src="fig2-4RTCBuilderInit.png" width="80%;"></a></div>
<!-- CENTER:''図 2-4 RTC Builder の初期起動時画面'' -->
<div align="center"><strong>Figure 5. Screen at initial startup of RTC Builder</strong></div>
<br>

#### Creating an RTCBuilder Project
First, create an Eclipse project for creating an RT component.
From the menu at the top of the screen, select [File] > [New] > [Project].
<br>

<div align="center"><a href="fig2-5CreateProject.png"><img src="fig2-5CreateProject.png" width="70%;"></a></div>
<!-- CENTER:''図 2-5 RTC Builder 用プロジェクトの作成　１'' -->
<div align="center"><strong>Figure 6. Creating an RTC Builder project 1</strong></div>
<br>
In the displayed "New Project" screen, select [Other] > [RTC Builder], and click [Next].
<br>

<div align="center"><a href="fig2-6CreateProject2.png"><img src="fig2-6CreateProject2.png" width="70%;"></a></div>
<!-- CENTER:''図 2-6 RTC Builder 用プロジェクトの作成　２'' -->
<div align="center"><strong>Figure 7. Creating an RTC Builder project 2</strong></div>
<br>
Enter the project name to be created in the "Project name" field and click [Finish].
<br>

<div align="center"><a href="fig2-7CreteProject3.PNG"><img src="fig2-7CreteProject3.PNG" width="70%;"></a></div>
<!-- CENTER:''図 2-7 RTC Builder 用プロジェクトの作成　３'' -->
<div align="center"><strong>Figure 8. Creating an RTC Builder project 3</strong></div>
<br>
A project with the specified name is generated and added to the Package Explorer.
<br>

<div align="center"><a href="fig2-8CreateProject4.png"><img src="fig2-8CreateProject4.png" width="70%;"></a></div>
<!-- CENTER:''図 2-8 RTC Builder 用プロジェクトの作成　４'' -->
<div align="center"><strong>Figure 9. Creating an RTC Builder project 4</strong></div>
<br>
Inside the generated project, an RTC profile XML (RTC.xml) with default values is automatically generated.

#### Setting the Location of the Data Type Definition Files Used by Data Ports

You need to set in advance the location of the IDL files in which the data types used by data ports and service ports are defined.
<br>
* The settings here remain valid unless the workspace is changed, so they do not need to be set for each project.
<br>
Set the location of the IDL files in which data types are defined by following the procedure below.
<br>

```
 1. メニューバーの [ウィンドウ] > [設定] をクリックし、設定ダイアログを表示させます。
 2. [RtcBuilder] > [Data Type] をクリックし、図12の Data Type 入力画面を出します。
 3. Data Type入力画面の [Add] ボタンをクリックし、"IDL File Directories"を入力します。
     OpenRTM-aist で定義されているデータ型の IDL ファイルはデフォルトでは下記にインストールされます。

      C:\Program Files\OpenRTM-aist\1.0\rtm\idl

 4. [OK] ボタンをクリックし、設定を終了します。
```

<br>

<div align="center"><a href="RTCBuilder_datatype_setup.png"><img src="RTCBuilder_datatype_setup.png" width="80%;"></a></div>
<!-- CENTER:''図 2-10 File メニューから Open New Builder Editor'' -->
<div align="center"><strong>Figure 12. Setting the location of the data type definition files</strong></div>

#### Starting the RTC Profile Editor
To open the RTC profile editor, click the [Open New RtcBuilder Editor] button on the toolbar, or select [File] > [Open New Builder Editor] from the menu.
<br>

<div align="center"><a href="fig2-9ToolsBarOpenNewRtcBuilder.png"><img src="fig2-9ToolsBarOpenNewRtcBuilder.png" width="30%;"></a></div>

<!-- CENTER:''図 2-9 ツールバーから Open New RtcBuilder Editor'' -->
<div align="center"><strong>Figure 10. Open New RtcBuilder Editor from the toolbar</strong></div>
<br>
<br>

<div align="center"><a href="fig2-10FileMenuOpenNewBuilder.png"><img src="fig2-10FileMenuOpenNewBuilder.png" width="30%;"></a></div>
<!-- CENTER:''図 2-10 File メニューから Open New Builder Editor'' -->
<div align="center"><strong>Figure 11. Open New Builder Editor from the File menu</strong></div>
<br>

#### Entering Component Profile Information and Generating Code

### Entering Component Profile Information and Generating Code

1. Select the "Basic" tab and enter the basic information.

<br>
- Module name: Flip
- Module description: Flip image component
- Module version: 1.0.0
- Module vender: AIST
- Module category: Category
- Component type: STATIC
- Component's activity type: PERIODIC
- Component kind: DataFlowComponent
- Number of maximum instance: 1
- Execution type: PeriodicExecutionContext
- Execution Rate: 1.0
<br>
- Output Project: Flip


<br>

<div align="center"><a href="RTCBuilder_base.png"><img src="RTCBuilder_base.png" width="80%;"></a></div>
<div align="center"><strong>Figure 13. Entering basic information</strong></div>
<br>

2. Select the "Activity" tab and specify the action callbacks to use.

Since the Flip component uses the onActivated(), onDeactivated(), and onExecute() callbacks, check on_activated, on_deactivated, and on_execute as shown in Figure 14.

<br>

<div align="center"><a href="RTCBuilder_activity.png"><img src="RTCBuilder_activity.png" width="80%;"></a></div>
<div align="center"><strong>Figure 14. Selecting activity callbacks</strong></div>
<br>

3. Select the "Data Ports" tab and enter the data port information.

<br>

- InPort Profile:
  - Port Name: original_image
  - Data Type: TimedOctetSeq
  - Var Name:  image_orig
  - Disp. Position: left

<br>

- OutPort Profile:
  - Port Name: fliped_image
  - Data Type: TimedOctetSeq
  - Var Name:  image_flip
  - Disp. Position: right

<br>

<div align="center"><a href="RTCBuilder_dataport.png"><img src="RTCBuilder_dataport.png" width="80%;"></a></div>
<div align="center"><strong>Figure 15. Entering data port information</strong></div>
<br>

4. Select the "Configuration" tab and enter the Configuration variables.

<br>

- flip_mode
  - Name: flip_mode
  - TYpe: int
  - Default Value: 1
  - Variable name: flip_mode

<br>

<br>

- image_height
  - Name: image_height
  - TYpe: int
  - Default Value: 240
  - Variable name: img_height

<br>

- image_width
  - Name: image_width
  - TYpe: int
  - Default Value: 320
  - Variable name: img_width

<br>

<div align="center"><a href="RTCBuilder_config.png"><img src="RTCBuilder_config.png" width="80%;"></a></div>
<div align="center"><strong>Figure 16. Entering configuration information</strong></div>
<br>

5. Select the "Language and Environment" tab and select the programming language.

This time, select C++ (language).

<br>

<div align="center"><a href="RTCBuilder_lang.png"><img src="RTCBuilder_lang.png" width="80%;"></a></div>
<div align="center"><strong>Figure 17. Selecting the programming language</strong></div>
<br>

6. Click the [Code Generation] button on the "Basic" tab to generate the component template.

<br>

<div align="center"><a href="RTCBuilder_base.png"><img src="RTCBuilder_base.png" width="80%;"></a></div>
<div align="center"><strong>Figure 18. Generating the template (Generate)</strong></div>
<br>

<span style="color:red;">* The generated code files are generated in the workspace folder specified when Eclipse was started. You can check the current workspace from [File] > [Switch Workspace].</span>;

### Implementing Activity Processing

In the Flip component, the image received from the InPort is saved in an image storage buffer, and the saved image is converted using the OpenCV cvFlip() function. After that, the converted image is sent from the OutPort.
<br>

<br>
Figure 19 shows the processing performed in onActivated(), onExecute(), and onDeactivated().
<br>

<div align="center"><a href="FlipRTC_State.png"><img src="FlipRTC_State.png" width="70%;"></a></div>
<div align="center"><strong>Figure 19. Overview of activity processing</strong></div>
<br>

Figure 20 shows the processing in onExecute().

<br>

<div align="center"><a href="FlipRTC.png"><img src="FlipRTC.png" width="70%;"></a></div>
<div align="center"><strong>Figure 20. Processing in onExecute()</strong></div>
<br>


#### Copying the User Property Sheet for OpenCV

A property sheet is a type of VC configuration file that describes various options required for compilation, such as include paths, library load paths, libraries, and macros.
In VC projects generated by RTCBuilder or rtc-template, VC property sheets are used to provide various options. In addition, a user-defined property sheet is also included so that users can add options.
- rtm_config.vsprop: A property sheet containing information related to OpenRTM. Since this file depends on the installed OpenRTM-aist, use copyprops.bat to copy it from the OpenRTM system directory to the current project.
- user_config.vsprops: A user-defined property sheet. It is empty by default. For usage, refer to user_config.vsprops (OpenCV settings) included in the source code: OpenRTM-aist/win32/OpenRTM-aist/example/USBCamera.

Save the following content with the file name user_config.vsprops and copy it to the Flip folder.

Alternatively, download the vsprops file from the link below and save it to the Flip folder.

<br>
[user_config.vsprops]()(No corresponding page available.)

* A user_config.vsprops file already exists in the Flip folder, but you can overwrite it.

<br>
```
 <?xml version="1.0" encoding="shift_jis"?>
 <VisualStudioPropertySheet
    ProjectType="Visual C++"
    Version="8.00"
    Name="OpenCV"
    >
    <Tool
        Name="VCCLCompilerTool"
        AdditionalIncludeDirectories="$(cv_includes)"
    />
    <Tool
        Name="VCLinkerTool"
        AdditionalLibraryDirectories="$(cv_libdir)"
    />
    <UserMacro
        Name="user_lib"
        Value="$(cv_lib)"
    />
    <UserMacro
        Name="user_libd"
        Value="$(cv_libd)"
    />
    <UserMacro
        Name="cv_root"
        Value="C:\Program Files\OpenCV"

    />
    <UserMacro
        Name="cv_includes"
        Value="&quot;$(cv_root)\cv\include&quot;;&quot;$(cv_root)\cvaux\include&quot;;&quot;$(cv_root)\cxcore\include&quot;;&quot;$(cv_root)\otherlibs\highgui&quot;;&quot;$(cv_root)\otherlibs\cvcam\include&quot;"
    />
    <UserMacro
        Name="cv_libdir"
        Value="&quot;$(cv_root)\lib&quot;"
    />
    <UserMacro
        Name="cv_bin"
        Value="$(cv_root)\bin"
    />
    <UserMacro
        Name="cv_lib"
        Value="cv.lib cvcam.lib highgui.lib cxcore.lib"
    />
    <UserMacro
        Name="cv_libd"
        Value="cv.lib cvcam.lib highgui.lib cxcore.lib"
    />
 </VisualStudioPropertySheet>
```
#### Running copyprops.bat

By executing the file named copyprops.bat, a file named rtm_config.vsprops is copied.

The rtm_config.vsprops file describes the include paths, libraries to link, and other settings required to build RT components with VC++.

#### Editing the Header File
- Include the OpenCV include files in order to use the OpenCV library.

```
 //OpenCV 用インクルードファイルのインクルード
 #include<cv.h>
 #include<cxcore.h>
 #include<highgui.h>
```

- This cvFlip component performs each of the following operations: allocating an image area, Flip processing, and releasing the allocated image area. Since these operations will be called in the onActivated(), onDeactivated(), and onExecute() callback functions, uncomment these three functions.

```
   /***
    *
    * The activated action (Active state entry action)
    * former rtc_active_entry()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    *
    *
    */
   virtual RTC::ReturnCode_t onActivated(RTC::UniqueId ec_id);

   /***
    *
    * The deactivated action (Active state exit action)
    * former rtc_active_exit()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
   virtual RTC::ReturnCode_t onDeactivated(RTC::UniqueId ec_id);

   /***
    *
    * The execution action that is invoked periodically
    * former rtc_active_do()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
   virtual RTC::ReturnCode_t onExecute(RTC::UniqueId ec_id);
```

- Add member variables for saving the flipped image.

```
   IplImage* m_image_buff;
   IplImage* m_flip_image_buff;
```

#### Editing the Source File 

Implement onActivated(), onDeactivated(), and onExecute() as follows.

```
 RTC::ReturnCode_t Flip::onActivated(RTC::UniqueId ec_id)
 {
   // イメージ用メモリーの確保
   m_image_buff = cvCreateImage(cvSize(m_img_width, m_img_height), IPL_DEPTH_8U, 3);
   m_flip_image_buff = cvCreateImage(cvSize(m_img_width, m_img_height), IPL_DEPTH_8U, 3);
   return RTC::RTC_OK;
 }


 RTC::ReturnCode_t Flip::onDeactivated(RTC::UniqueId ec_id)
 {
   // イメージ用メモリーの解放
   cvReleaseImage(&m_image_buff);
   cvReleaseImage(&m_flip_image_buff);
   return RTC::RTC_OK;
 }


 RTC::ReturnCode_t Flip::onExecute(RTC::UniqueId ec_id)
 {
   // 新しいデータのチェック
   if (m_image_origIn.isNew()) {
     // InPortデータの読み込み
     m_image_origIn.read();

     // InPortの画像データをIplImageのimageDataにコピー
     memcpy(m_image_buff->imageData,(void *)&(m_image_orig.data[0]),m_image_orig.data.length());
 
     // InPortからの画像データを反転する。 m_flip_mode 0: X軸周り, 1: Y軸周り, -1: 両方の軸周り
     cvFlip(m_image_buff, m_flip_image_buff, m_flip_mode);
 
     // 画像データのサイズ取得
     int len = m_flip_image_buff->nChannels * m_flip_image_buff->width * m_flip_image_buff->height;
     m_image_flip.data.length(len);
 
     // 反転した画像データを OutPort にコピー
     memcpy((void *)&(m_image_flip.data[0]),m_flip_image_buff->imageData,len);
 
     // 反転した画像データを OutPort から出力する。
     m_image_flipOut.write();
  }
   return RTC::RTC_OK;
 }

```
#### Running the Build

Build the component as shown in Figure 21.

<br>

<div align="center"><a href="VC++_build.png"><img src="VC++_build.png" width="70%;"></a></div>
<div align="center"><strong>Figure 21. Running the build</strong></div>
<br>

#### Checking Operation of the Flip Component

Here, we connect and check the operation of the USBCameraAqcuireComp component and the USBCameraMonitorCom component included in the OpenRTM-aist sample components, together with the Flip component.

#### Starting NameService

Start the omniORB name service.

<br>
Click [Start] > [All Programs] > [OpenRTM-aist] > [C++] > [examples], then click [Start Naming Service].

#### Creating rtc.conf

For RT components, information such as the name server address and the registration format for the name server must be specified in a file named rtc.conf.

Save the following content with the file name rtc.conf and place it in the Flip\FlipComp\Debug (or Release) folder.

```
 corba.nameservers: localhost
 naming.formats: %n.rtc
```

#### Starting the Flip Component

Start the Flip component.

Run the FlipComp.exe file located in the folder where you placed the rtc.conf file earlier.

#### Starting the USBCameraAqcuire and USBCameraMonitor Components 

Start the USBCameraAqcuireComp component, which outputs captured images from a USB camera from an OutPort, and the USBCameraMonitorCOmp component, which displays images received through an InPort on the screen.

These two components can be started with the following procedure.

Click [Start] > [All Programs] > [OpenRTM-aist] > [C++] > [examples], and click "USBCameraAqcuireComp" and "USBCameraMonitorCOmp" respectively to run them.

#### Connecting the Components

Connect the USBCameraAqcuireComp, Flip, and USBCameraMonitorComp components in RTSystemEditor as shown in Figure 22.

<br>

<div align="center"><a href="RTSystemEditor_connection_flip.png"><img src="RTSystemEditor_connection_flip.png" width="70%;"></a></div>
<div align="center"><strong>Figure 22. Connecting the components</strong></div>
<br>

#### Changing the Configuration of the Flip Component

As shown in Figure 23, you can change the configuration in the Configuration View.

If you use the ELECOM UCAM-DLM 130HWH (white USB camera), change the image_height and image_width parameters as follows.

```
 image_height : 480
 image_width  : 640
```

Also, if you use the ELECOM UCAM-DLM 130HWH (white USB camera), you need to change the image_height and image_width parameters of USBCameraMonitor as shown above.

<br>

<div align="center"><a href="RTSystemEditor_config_edit.png"><img src="RTSystemEditor_config_edit.png" width="70%;"></a></div>
<div align="center"><strong>Figure 23. Changing configuration parameters</strong></div>
<br>

#### Activating the Components

Click the "ALL" icon at the top of RTSystemEditor to activate all components.

If they are activated successfully, the components are displayed in yellow-green as shown in Figure 24.

<br>

<div align="center"><a href="RTSystemEditor_activate.png"><img src="RTSystemEditor_activate.png" width="70%;"></a></div>
<div align="center"><strong>Figure 24. Activating the components</strong></div>
<br>

#### Operation Check


Change the configuration parameter "flip_mode" of the Flip component to "0" or "-1", etc., and check whether the image is flipped.

## Source File of the Flip Component

```
 // -*- C++ -*-
 /*!
  * @file  Flip.cpp
  * @brief Flip image component
  * @date $Date$
  *
  * $Id$
  */
 
 #include "Flip.h"
 
 // Module specification
 static const char* flip_spec[] =
   {
     "implementation_id", "Flip",
     "type_name",         "Flip",
     "description",       "Flip image component",
     "version",           "1.0.0",
     "vendor",            "AIST",
     "category",          "Category",
     "activity_type",     "PERIODIC",
     "kind",              "DataFlowComponent",
     "max_instance",      "1",
     "language",          "C++",
     "lang_type",         "compile",
     "exec_cxt.periodic.rate", "1.0",
     // Configuration variables
     "conf.default.flip_mode", "1",
     "conf.default.image_height", "240",
     "conf.default.image_width", "320",
     ""
   };
 
 /*!
  * @brief constructor
  * @param manager Maneger Object
  */
 Flip::Flip(RTC::Manager* manager)
   : RTC::DataFlowComponentBase(manager),
     m_image_origIn("original_image", m_image_orig),
     m_image_flipOut("fliped_image", m_image_flip),
     dummy(0),
     m_image_buff(0),
     m_flip_image_buff(0)
 {
   // Registration: InPort/OutPort/Service
 
   // Set InPort buffers
   registerInPort("original_image", m_image_origIn);
   
   // Set OutPort buffer
   registerOutPort("fliped_image", m_image_flipOut);
 }
 
 /*!
  * @brief destructor
  */
 Flip::~Flip()
 {
 }
 
 
 RTC::ReturnCode_t Flip::onInitialize()
 {
   // Bind variables and configuration variable
   bindParameter("flip_mode", m_flip_mode, "1");
   bindParameter("image_height", m_img_height, "240");
   bindParameter("image_width", m_img_width, "320");
   return RTC::RTC_OK;
 }
 
 RTC::ReturnCode_t Flip::onActivated(RTC::UniqueId ec_id)
 {
   // イメージ用メモリーの確保
   m_image_buff = cvCreateImage(cvSize(m_img_width, m_img_height), IPL_DEPTH_8U, 3);
   m_flip_image_buff = cvCreateImage(cvSize(m_img_width, m_img_height), IPL_DEPTH_8U, 3);
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t Flip::onDeactivated(RTC::UniqueId ec_id)
 {
   // イメージ用メモリーの解放
   cvReleaseImage(&m_image_buff);
   cvReleaseImage(&m_flip_image_buff);
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t Flip::onExecute(RTC::UniqueId ec_id)
 {
   // 新しいデータのチェック
   if (m_image_origIn.isNew()) {
     // InPort データの読み込み
     m_image_origIn.read();
 
     // InPortの 画像データを IplImage の imageData にコピー
     memcpy(m_image_buff->imageData,(void *)&(m_image_orig.data[0]),m_image_orig.data.length());
 
     // InPortからの画像データを反転する。 m_flip_mode 0: X軸周り, 1: Y軸周り, -1: 両方の軸周り
     cvFlip(m_image_buff, m_flip_image_buff, m_flip_mode);
 
     // 画像データのサイズ取得
     int len = m_flip_image_buff->nChannels * m_flip_image_buff->width * m_flip_image_buff->height;
     m_image_flip.data.length(len);
 
     // 反転した画像データを OutPort にコピー
     memcpy((void *)&(m_image_flip.data[0]),m_flip_image_buff->imageData,len);
 
     // 反転した画像データを OutPort から出力する。
     m_image_flipOut.write();
  }
   return RTC::RTC_OK;
 }
 
 extern "C"
 {
  
   void FlipInit(RTC::Manager* manager)
   {
     RTC::Properties profile(flip_spec);
     manager->registerFactory(profile,
                              RTC::Create<Flip>,
                              RTC::Delete<Flip>);
   }
   
 };
```

### Header File of the Flip Component

```
 // -*- C++ -*-
 /*!
  * @file  Flip.h
  * @brief Flip image component
  * @date  $Date$
  *
  * $Id$
  */
 
 #ifndef FLIP_H
 #define FLIP_H
 
 #include <rtm/Manager.h>
 #include <rtm/DataFlowComponentBase.h>
 #include <rtm/CorbaPort.h>
 #include <rtm/DataInPort.h>
 #include <rtm/DataOutPort.h>
 #include <rtm/idl/BasicDataTypeSkel.h>
 
 // (1)  OpenCV 用インクルードファイルのインクルード
 #include<cv.h>
 #include<cxcore.h>
 #include<highgui.h>
 
 
 using namespace RTC;
 
 /*!
  * @class Flip
  * @brief Flip image component
  *
  */
 class Flip
   : public RTC::DataFlowComponentBase
 {
  public:
   /*!
    * @brief constructor
    * @param manager Maneger Object
    */
   Flip(RTC::Manager* manager);
 
   /*!
    * @brief destructor
    */
   ~Flip();
 
 
   /*!
    *
    * The initialize action (on CREATED->ALIVE transition)
    * formaer rtc_init_entry() 
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
    virtual RTC::ReturnCode_t onInitialize();
 
   /***
    *
    * The activated action (Active state entry action)
    * former rtc_active_entry()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
   virtual RTC::ReturnCode_t onActivated(RTC::UniqueId ec_id);
 
   /***
    *
    * The deactivated action (Active state exit action)
    * former rtc_active_exit()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
   virtual RTC::ReturnCode_t onDeactivated(RTC::UniqueId ec_id);
 
   /***
    *
    * The execution action that is invoked periodically
    * former rtc_active_do()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    * 
    * 
    */
   virtual RTC::ReturnCode_t onExecute(RTC::UniqueId ec_id);
 
 
  protected:
   // Configuration variable declaration
   /*!
    * flip_mode = 0: flipping around x-axis 
    * flip_mode > 1: flipping around y-axis 
    * flip_mode < 0: flipping around both axises
    * - Name: flip_mode flip_mode
    * - DefaultValue: 1
    */
   int m_flip_mode;
   /*!
    * 
    * - Name:  m_img_height
    * - DefaultValue: 240
    * - 画像の高さ
    */
   int m_img_height;
   /*!
    * 
    * - Name:  m_img_width
    * - DefaultValue: 320
    * - 画像の幅
    */
   int m_img_width;
 
 
   // DataInPort declaration
   TimedOctetSeq m_image_orig;
   InPort<TimedOctetSeq> m_image_origIn;
   
 
   // DataOutPort declaration
   TimedOctetSeq m_image_flip;
   OutPort<TimedOctetSeq> m_image_flipOut;
   
  private:
   int dummy;
   IplImage* m_image_buff;
   IplImage* m_flip_image_buff;
 };
 
 
 extern "C"
 {
   void FlipInit(RTC::Manager* manager);
 };
 
 #endif // FLIP_H
```


### Built Package of the Flip Component 

The built package can be downloaded from the following link.

The extension is set to "zip_", so rename it to "zip" before extracting it.


- [Built package]()(No corresponding page available.)

## Bonus (Object Tracking Component) 

This component performs object tracking using the OpenCV library.

### Component Overview

A component that displays image data from an InPort and tracks an object selected with the mouse.

From the OutPort, it outputs the object tracking image and the amount of movement from the position selected with the mouse.

The image size, brightness, and saturation can be changed through the configuration.

The specifications of the RTC to be created are as follows.

- InPort
  - Captured image data (TimedOctetSeq)

- OutPort
  - Object tracking image data (TimedOctetSeq)

- OutPort
  - Displacement of the center position of the object selected with the mouse (TimedFloatSeq)

- Configuration
  - Maximum brightness value (int) default: 256
  - Minimum brightness value (int) default: 10
  - Minimum saturation value (int) default: 30
  - Image height (int)   default: 240
  - Image width (int)     default: 320

### Profile Information Input in RTCBuilder
#### Basic Information

- Module name: ObjectTracking
- Module description: Object tracking component
- OutputProject: ObjectTracking

#### Data Ports

<br>

- InPort Profile:
  - Port Name: in_image
  - Data Type: TimedOctetSeq
  - Var Name:  in_image
  - Disp. Position: left
<br>

- OutPort Profile:
  - Port Name: tracing_image
  - Data Type: TimedOctetSeq
  - Var Name:  tracking_image
  - Disp. Position: right
<br>

- OutPort Profile:
  - Port Name: displacement
  - Data Type: TimedFloatSeq
  - Var Name:  displacement
  - Disp. Position: right

#### Configuration Parameters

<br>

- brightness_max
  - Name: brightness_max
  - TYpe: int
  - Default Value: 256
  - Variable name: b_max

<br>

- brightness_min
  - Name: brightness_min
  - TYpe: int
  - Default Value: 10
  - Variable name: b_min

<br>

- saturation_min
  - Name: saturation_min
  - TYpe: int
  - Default Value: 30
  - Variable name: s_min

<br>

- image_height
  - Name: image_height
  - TYpe: int
  - Default Value: 240
  - Variable name: img_height

<br>

- image_width
  - Name: image_width
  - TYpe: int
  - Default Value: 320
  - Variable name: img_width

### Source File of the ObjectTracking Component 

```
 // -*- C++ -*-
 /*!
  * @file  ObjectTracking.cpp
  * @brief Object tracking component
  * @date $Date$
  *
  * $Id$
  */
 
 #include "ObjectTracking.h"
 
 #define HIST_RANGE_MAX 180.0
 #define HIST_RANGE_MIN 0.0
 
 // 入力画像用 IplImage
 IplImage* g_image;
 
 // CamShift トラッキング用変数
 CvPoint g_origin;
 CvRect g_selection;  // 
 
 // 初期追跡領域の設定判別フラグ値 (0: 設定なし, 1: 設定あり)
 int g_select_object;
 
 // トラッキングの開始/停止用フラグ値 (0: 停止, -1: 開始, 1: トラッキング中)
 int g_track_object;
 
 // オブジェクト選択判定用フラグ(0: 1以外 1: 選択された直後)
 int g_selected_flag;
 
 // 選択された範囲の中心座標
 float g_selected_x;
 float g_selected_y;
 
 
 // Module specification
 static const char* objecttracking_spec[] =
   {
     "implementation_id", "ObjectTracking",
     "type_name",         "ObjectTracking",
     "description",       "Object tracking component",
     "version",           "1.0.0",
     "vendor",            "AIST",
     "category",          "Category",
     "activity_type",     "PERIODIC",
     "kind",              "DataFlowComponent",
     "max_instance",      "1",
     "language",          "C++",
     "lang_type",         "compile",
     "exec_cxt.periodic.rate", "1.0",
     // Configuration variables
     "conf.default.brightness_max", "256",
     "conf.default.brightness_min", "10",
     "conf.default.saturation_min", "30",
     "conf.default.image_height", "240",
     "conf.default.image_width", "320",
     ""
   };
 
 /*!
  * @brief constructor
  * @param manager Maneger Object
  */
 ObjectTracking::ObjectTracking(RTC::Manager* manager)
   : RTC::DataFlowComponentBase(manager),
     m_in_imageIn("in_image", m_in_image),
     m_tracking_imageOut("tracing_image", m_tracking_image),
     m_displacementOut("displacement", m_displacement),
     dummy(0),
     m_hsv(0), m_hue(0), m_mask(0), m_backproject(0),
     m_hist(0), m_backproject_mode(0),m_hdims(16),
     m_init_flag(0)
 {
   // Registration: InPort/OutPort/Service
   // Set InPort buffers
   registerInPort("in_image", m_in_imageIn);
   
   // Set OutPort buffer
   registerOutPort("tracing_image", m_tracking_imageOut);
   registerOutPort("displacement", m_displacementOut);
 
   m_hranges_arr[0] = HIST_RANGE_MIN;
   m_hranges_arr[1] = HIST_RANGE_MAX;
   m_hranges = m_hranges_arr;
 }
 
 /*!
  * @brief destructor
  */
 ObjectTracking::~ObjectTracking()
 {
 }
 
 
 
 RTC::ReturnCode_t ObjectTracking::onInitialize()
 {
   // Bind variables and configuration variable
   bindParameter("brightness_max", m_b_max, "256");
   bindParameter("brightness_min", m_b_min, "10");
   bindParameter("saturation_min", m_s_min, "30");
   bindParameter("image_height", m_img_height, "240");
   bindParameter("image_width", m_img_width, "320");
   m_displacement.data.length(2);
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t ObjectTracking::onActivated(RTC::UniqueId ec_id)
 {
   m_init_flag = 0;
   // ウインドウを生成する
   cvNamedWindow( "ObjectTracking", 1 );
   // マウス操作時のコールバック処理の登録
   cvSetMouseCallback( "ObjectTracking", on_mouse, 0 );
   g_selected_flag = 0;
   g_selected_x = 0.0;;
   g_selected_y = 0.0;;
 
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t ObjectTracking::onDeactivated(RTC::UniqueId ec_id)
 {
   if (m_init_flag) {
     // メモリーを解放する
     cvReleaseImage(&g_image);
     cvReleaseImage(&m_hsv);
     cvReleaseImage(&m_hue);
     cvReleaseImage(&m_mask);
     cvReleaseImage(&m_backproject);
  }
   // ウインドウを破棄する
   cvDestroyWindow("ObjectTracking");
   m_init_flag = 0;
   return RTC::RTC_OK;
 }
 
 
 RTC::ReturnCode_t ObjectTracking::onExecute(RTC::UniqueId ec_id)
 {
   if (m_in_imageIn.isNew()) {
     m_in_imageIn.read();
 
     if(!m_init_flag) allocateBuffers();
 
     memcpy(g_image->imageData,(void *)&(m_in_image.data[0]),m_in_image.data.length());
     cvShowImage("ObjectTracking", g_image);
 
     // キャプチャされた画像を HSV 表色系に変換して hsv に格納
     cvCvtColor( g_image, m_hsv, CV_BGR2HSV );
 
     // g_track_objectフラグが0以下なら、以下の処理を行う
     if( g_track_object )
       {
 	cvInRangeS( m_hsv, cvScalar(HIST_RANGE_MIN,m_s_min,MIN(m_b_min,m_b_max),0),
 		    cvScalar(HIST_RANGE_MAX,256,MAX(m_b_min,m_b_max),0), m_mask );
 	cvSplit( m_hsv, m_hue, 0, 0, 0 );
 
 	if( g_track_object < 0 ) calcHistogram();
 
 	// バックプロジェクションを計算する
 	cvCalcBackProject( &m_hue, m_backproject, m_hist );
 	// backProjectionのうち、マスクが1であるとされた部分のみ残す
 	cvAnd( m_backproject, m_mask, m_backproject, 0 );
 	// CamShift法による領域追跡を実行する
 	cvCamShift( m_backproject, m_track_window,
 		    cvTermCriteria( CV_TERMCRIT_EPS | CV_TERMCRIT_ITER, 10, 1 ),
 		    &m_track_comp, &m_track_box );
 	m_track_window = m_track_comp.rect;
 	
 	if( m_backproject_mode )
 	  cvCvtColor( m_backproject, g_image, CV_GRAY2BGR );
 	if( g_image->origin )
 	  m_track_box.angle = -m_track_box.angle;
 	cvEllipseBox( g_image, m_track_box, CV_RGB(255,0,0), 3, CV_AA, 0 );
 
 	// マウスで選択された領域の中心座標を保存
 	if (g_selected_flag) {
 	  g_selected_x = m_track_box.center.x;
 	  g_selected_y = m_track_box.center.y;
 	  g_selected_flag = 0;
	}
 
 	// マウスで選択された位置からの移動量をOutPortから出力
 	m_displacement.data[0] = m_track_box.center.x - g_selected_x;
 	m_displacement.data[1] = -(m_track_box.center.y - g_selected_y);
 	m_displacementOut.write();
       }
         
     // マウスで選択中の初期追跡領域の色を反転させる
     if( g_select_object && g_selection.width > 0 && g_selection.height > 0 )
       {
 	cvSetImageROI( g_image, g_selection );
 	cvXorS( g_image, cvScalarAll(255), g_image, 0 );
 	cvResetImageROI( g_image );
       }
 
     // 画像を表示する
     cvShowImage( "ObjectTracking", g_image );
 
     // 画像をOutPortから出力する
     int len = g_image->nChannels * g_image->width * g_image->height;
     m_tracking_image.data.length(len);
     memcpy((void *)&(m_tracking_image.data[0]),g_image->imageData,len);
     m_tracking_imageOut.write();
 
     // キー入力を待ち、押されたキーによって処理を分岐させる
     int c = cvWaitKey(10);
     // while無限ループから脱出（プログラムを終了）
     if( (char) c == 27 ) {
       this->exit();
    }
  }
   return RTC::RTC_OK;
 }
 
 /*!
  * 全てのイメージ用メモリーの確保
  */
 void ObjectTracking::allocateBuffers() {
   g_image = cvCreateImage( cvSize(m_img_width,m_img_height),8, 3 );
   m_hsv = cvCreateImage( cvSize(m_img_width,m_img_height),8, 3 );
   m_hue = cvCreateImage( cvSize(m_img_width,m_img_height),8, 1 );
   m_mask = cvCreateImage( cvSize(m_img_width,m_img_height),8, 1 );
   m_backproject = cvCreateImage( cvSize(m_img_width,m_img_height),8, 1 );
   m_hist = cvCreateHist( 1, &m_hdims, CV_HIST_ARRAY, &m_hranges, 1 );
   m_init_flag = 1;
 }
 
 /*!
  * ヒストグラムの計算
  */
 void ObjectTracking::calcHistogram() {
   float max_val = 0.f;
   cvSetImageROI( m_hue, g_selection );
   cvSetImageROI( m_mask, g_selection );
   // ヒストグラムを計算し、最大値を求める
   cvCalcHist( &m_hue, m_hist, 0, m_mask );
   cvGetMinMaxHistValue( m_hist, 0, &max_val, 0, 0 );
   // ヒストグラムの縦軸（頻度）を0-255のダイナミックレンジに正規化
   cvConvertScale( m_hist->bins, m_hist->bins, max_val ? 255. / max_val : 0., 0 );
   // hue,mask画像に設定された ROI をリセット
   cvResetImageROI( m_hue );
   cvResetImageROI( m_mask );
   m_track_window = g_selection;
   // track_object をトラッキング中にする
   g_track_object = 1;
 }
 
 
 extern "C"
 {
  
   void ObjectTrackingInit(RTC::Manager* manager)
   {
     RTC::Properties profile(objecttracking_spec);
     manager->registerFactory(profile,
                              RTC::Create<ObjectTracking>,
                              RTC::Delete<ObjectTracking>);
   }
   
 
   //
   //	マウスドラッグによって初期追跡領域を指定する
   //
   //	引数:
   //		event	: マウス左ボタンの状態
   //		x		: マウスが現在ポイントしているx座標
   //		y		: マウスが現在ポイントしているy座標
   //		flags	: 本プログラムでは未使用
   //		param	: 本プログラムでは未使用
   //
   void on_mouse( int event, int x, int y, int flags, void* param )
   {
     // 画像が取得されていなければ、処理を行わない
     if( !g_image )
       return;
 
     // 原点の位置に応じてyの値を反転（画像の反転ではない）
     if( g_image->origin )
       y = g_image->height - y;
 
     // マウスの左ボタンが押されていれば以下の処理を行う
     if( g_select_object )
       {
 	g_selection.x = MIN(x,g_origin.x);
 	g_selection.y = MIN(y,g_origin.y);
 	g_selection.width = g_selection.x + CV_IABS(x - g_origin.x);
 	g_selection.height = g_selection.y + CV_IABS(y - g_origin.y);
         
 	g_selection.x = MAX( g_selection.x, 0 );
 	g_selection.y = MAX( g_selection.y, 0 );
 	g_selection.width = MIN( g_selection.width, g_image->width );
 	g_selection.height = MIN( g_selection.height, g_image->height );
 	g_selection.width -= g_selection.x;
 	g_selection.height -= g_selection.y;
       }
 
     // マウスの左ボタンの状態によって処理を分岐
     switch( event )
       {
       case CV_EVENT_LBUTTONDOWN:
 	// マウスの左ボタンが押されたのであれば、
 	// 原点および選択された領域を設定
 	g_origin = cvPoint(x,y);
 	g_selection = cvRect(x,y,0,0);
 	g_select_object = 1;
 	break;
       case CV_EVENT_LBUTTONUP:
 	// マウスの左ボタンが離されたとき、width と height がどちらも正であれば、
 	// g_track_objectフラグを開始フラグにする
 	g_select_object = 0;
 	if( g_selection.width > 0 && g_selection.height > 0 ) {
 	  g_track_object = -1;
 	  g_selected_flag = 1;
	}
 	break;
       }
   }
 
 };

```

### Header File of the ObjectTracking Component

```
 // -*- C++ -*-
 /*!
  * @file  ObjectTracking.h
  * @brief Object tracking component
  * @date  $Date$
  *
  * $Id$
  */

 #ifndef OBJECTTRACKING_H
 #define OBJECTTRACKING_H

 #include <rtm/Manager.h>
 #include <rtm/DataFlowComponentBase.h>
 #include <rtm/CorbaPort.h>
 #include <rtm/DataInPort.h>
 #include <rtm/DataOutPort.h>
 #include <rtm/idl/BasicDataTypeSkel.h>

 #include <cv.h>
 #include <highgui.h>
 #include <stdio.h>
 #include <ctype.h>

 using namespace RTC;

 /*!
  * @class ObjectTracking
  * @brief Object tracking component
  *
  */
 class ObjectTracking
   : public RTC::DataFlowComponentBase
 {
  public:
   /*!
    * @brief constructor
    * @param manager Maneger Object
    */
   ObjectTracking(RTC::Manager* manager);

   /*!
    * @brief destructor
    */
   ~ObjectTracking();

   /*!
    *
    * The initialize action (on CREATED->ALIVE transition)
    * formaer rtc_init_entry()
    *
    * @return RTC::ReturnCode_t
    *
    *
    */
    virtual RTC::ReturnCode_t onInitialize();


   /***
    *
    * The activated action (Active state entry action)
    * former rtc_active_entry()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    *
    *
    */
   virtual RTC::ReturnCode_t onActivated(RTC::UniqueId ec_id);

   /***
    *
    * The deactivated action (Active state exit action)
    * former rtc_active_exit()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    *
    *
    */
   virtual RTC::ReturnCode_t onDeactivated(RTC::UniqueId ec_id);

   /***
    *
    * The execution action that is invoked periodically
    * former rtc_active_do()
    *
    * @param ec_id target ExecutionContext Id
    *
    * @return RTC::ReturnCode_t
    *
    *
    */
   virtual RTC::ReturnCode_t onExecute(RTC::UniqueId ec_id);

   /*!
    *    入力された1つの色相値を RGB に変換する
    *
    *    引数:
    *        hue        : HSV表色系における色相値H
    *    戻り値：
    *        CvScalar: RGB の色情報が BGR の順で格納されたコンテナ
    */

   CvScalar hsv2rgb( float hue ) {
     int rgb[3], p, sector;
     static const int sector_data[][3]=
     { {0,2,1}, {1,2,0}, {1,0,2}, {2,0,1}, {2,1,0}, {0,1,2} };
     hue *= 0.033333333333333333333333333333333f;
     sector = cvFloor(hue);
     p = cvRound(255*(hue - sector));
     p ^= sector & 1 ? 255 : 0;
 
     rgb[sector_data[sector][0]] = 255;
     rgb[sector_data[sector][1]] = 0;
     rgb[sector_data[sector][2]] = p;
     
     return cvScalar(rgb[2], rgb[1], rgb[0],0);
   }

   /*!
    * 全てのイメージ用バッファの確保
    */
   void allocateBuffers();

   /*!
    * ヒストグラムの計算
    */
   void calcHistogram();

  protected:
   // Configuration variable declaration
   /*!
    *
    * - Name:  b_max
    * - DefaultValue: 256
    * - 明度の最大値
    */
   int m_b_max;
   /*!
    *
    * - Name:  b_min
    * - DefaultValue: 10
    * - 明度の最小値
    */
   int m_b_min;

  /*!
    *
    * - Name:  s_min
    * - DefaultValue: 30
    * - 彩度の最小値
    */
   int m_s_min;
   /*!
    *
    * - Name:  m_img_height
    * - DefaultValue: 240
    * - 画像の高さ
    */
   int m_img_height;
   /*!
    *
    * - Name:  m_img_width
    * - DefaultValue: 320
    * - 画像の幅
    */
   int m_img_width;

  // DataInPort declaration
   TimedOctetSeq m_in_image;
   InPort<TimedOctetSeq> m_in_imageIn;

   // DataOutPort declaration
   TimedOctetSeq m_tracking_image;
   OutPort<TimedOctetSeq> m_tracking_imageOut;

   TimedFloatSeq m_displacement;
   OutPort<TimedFloatSeq> m_displacementOut;

  private:
   int dummy;
   IplImage* m_hsv;         // HSV 表色系用 IplImage
   IplImage* m_hue;         // HSV 表色系のHチャンネル用 IplImage
   IplImage* m_mask;        // マスク画像用 IplImage
   IplImage* m_backproject; // バックプロジェクション画像用 IplImage

   CvHistogram * m_hist; // ヒストグラム処理用構造体

  // 処理モード選択用フラグ
   int m_backproject_mode; // バックプロジェクション画像の表示/非表示用フラグ値 (0: 非表示, 1: 表示)

   // CamShiftトラッキング用変数
   CvRect m_track_window;
   CvBox2D m_track_box;
   CvConnectedComp m_track_comp;

   // ヒストグラム用変数
   int m_hdims;                // ヒストグラムの次元数
   float m_hranges_arr[2]; // ヒストグラムのレンジ
   float* m_hranges;

   // 初期化判定フラグ
   int m_init_flag;
 };

 extern "C"
 {
   void ObjectTrackingInit(RTC::Manager* manager);
   void on_mouse( int event, int x, int y, int flags, void* param );
 };

 #endif // OBJECTTRACKING_H

```

### Connecting the Components

Figure 25 shows an example connection of the USBCameraAcquire, Flip, ObjectTracking, and SeqIn components.

First, the USBCameraAcquire component acquires the image from the USB camera.

Next, the Flip component flips it horizontally.

The reason for flipping it is that when the output of the object tracking component is used as a joystick, it is easier to operate if the image is displayed like a mirror.

Next, the ObjectTracking component outputs the displacement of the tracking target selected in advance from the OutPort (displacement), and the SeqIn component displays the displacement.


<br>

<div align="center"><a href="RTSystemEditor_connection.png"><img src="RTSystemEditor_connection.png" width="70%;"></a></div>
<div align="center"><strong>Figure 25. Example component connection</strong></div>
<br>
## Built Package of the ObjectTracking Component 

The built package can be downloaded from the following link.

<!-- 拡張子を"zip_"としてますので、"zip"にリネームしてから解凍して下さい。-->

 
- [Built package (No Link)]()(No corresponding page available.)


