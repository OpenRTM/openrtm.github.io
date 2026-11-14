---
layout: page
title: code generation, save, and load
---
<!-- Title: コード生成・セーブとロード -->
#contents

## Code Generation
After setting various profile information for the RT component to be generated, generate the template code.
When you click the [Generate Code] button on the Basic Profile input page, template code corresponding to the entered profile information is generated.
<br>

<div align="center"><a href="CodeGen.png"><img src="CodeGen.png" width="60%;"></a></div>
<div align="center"><strong>Generating Template Code</strong></div>
<br>

The template files generated when code generation is executed after selecting each language are as follows.

<div align="center"><strong>List of Generated Files</strong></div>

- C++ (when the "Use old build environment." checkbox is not selected)

<table class="table-alt">
  <tr style="text-align: center;">
    <td>File Name</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt; Comp.cpp</td>
    <td>Code for starting the RT component.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;.h</td>
    <td>Header of the RT component body.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;.cpp</td>
    <td>Code of the RT component body.</td>
  </tr>
  <tr>
    <td>&lt;service type name&gt;SVC_impl.h</td>
    <td>Header of the service provider. (*)<br>Only the Type specified in ServiceProvider is output.</td>
  </tr>
  <tr>
    <td>&lt;service type name&gt;SVC_impl. cpp</td>
    <td>Implementation code of the service provider. (*)<br>Only the Type specified in ServiceProvider is output.</td>
  </tr>
  <tr>
    <td>CMakeLists.txt</td>
    <td>Configuration file for CMake.</td>
  </tr>
  <tr>
    <td>doc/</td>
  </tr>
  <tr>
    <td>doxyfile.in</td>
    <td>Configuration file for Doxygen.</td>
  </tr>
  <tr>
    <td>cmake/</td>
  </tr>
  <tr>
    <td>uninstall_target.cmake.in</td>
    <td>Template file for adding an uninstall target (for CMake)</td>
  </tr>
  <tr>
    <td>cpack_options.cmake</td>
    <td>Module for creating WiX packages (for CMake/WiX)</td>
  </tr>
  <tr>
    <td>License.rtf</td>
    <td>License display included in package information (for CMake/WiX)</td>
  </tr>
  <tr>
    <td>wix.xsl.in</td>
    <td>Template for specifying files to include in the WiX package (for CMake/WiX)</td>
  </tr>
  <tr>
    <td>cmake/Modules/</td>
  </tr>
  <tr>
    <td>FindOpenRTM.cmake</td>
    <td>Module for obtaining OpenRTM-aist environment settings (for CMake)</td>
  </tr>
</table>

<br>

- C++ (when the [Use old build environment.] checkbox is selected)
<table class="table-alt">
  <tr style="text-align: center;">
    <td>File Name</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt; Comp.cpp</td>
    <td>Code for starting the RT component.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;.h</td>
    <td>Header of the RT component body.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;.cpp</td>
    <td>Code of the RT component body.</td>
  </tr>
  <tr>
    <td>&lt;service type name&gt;SVC_impl.h</td>
    <td>Header of the service provider. (*)<br>Only the Type specified in ServiceProvider is output.</td>
  </tr>
  <tr>
    <td>&lt;service type name&gt;SVC_impl. cpp</td>
    <td>Implementation code of the service provider. (*)<br>Only the Type specified in ServiceProvider is output.</td>
  </tr>
  <tr>
    <td>Makefile.&lt;RTC name&gt;</td>
    <td>Makefile for compiling.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt; _vc8.sln </td>
    <td>Solution file for Visual Studio 2005.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;_vc8.vcproj</td>
    <td>RT component project file for Visual Studio 2005.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;Comp_vc8.vcproj</td>
    <td>Project file for startup code for Visual Studio 2005.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;_vc9.sln</td>
    <td>Solution file for Visual Studio 2008.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;_vc9.vcproj</td>
    <td>RT component project file for Visual Studio 2008.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;Comp_vc9.vcproj</td>
    <td>Project file for startup code for Visual Studio 2008.</td>
  </tr>
  <tr>
    <td>Copyprops.bat</td>
    <td>Batch file for copying property files.</td>
  </tr>
  <tr>
    <td>User_config.vsprops</td>
    <td>User-defined property file.</td>
  </tr>
  <tr>
    <td>OpenRTM-aist.vsprops</td>
    <td>Property file for OpenRTM-aist.</td>
  </tr>
</table>


<br>

- Java

<br>
<table class="table-alt">
  <tr style="text-align: center;">
    <td>File Name</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;Comp.java</td>
    <td>Class for starting the RT component.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;.java</td>
    <td>Class that defines the RT component's Component Profile, initialization processing, and so on.</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;Impl.java</td>
    <td>Main body of the RT component.</td>
  </tr>
  <tr>
    <td>build_&lt;RTC name&gt;.xml</td>
    <td>Build file for the RT component.</td>
  </tr>
  <tr>
    <td>&lt;service type name&gt; SVC_impl.java</td>
    <td>Implementation class of the service provider. (*)</td>
  </tr>
  <tr>
    <td>CMakeLists.txt</td>
    <td>Configuration file for CMake.</td>
  </tr>
  <tr>
    <td>doc/</td>
  </tr>
  <tr>
    <td>doxyfile.in</td>
    <td>Configuration file for Doxygen.</td>
  </tr>
  <tr>
    <td>cmake_modules/</td>
  </tr>
  <tr>
    <td>cmake_javacompile.cmake.in</td>
    <td>Template file for adding a Java compile target (for CMake)</td>
  </tr>
  <tr>
    <td>FindOpenRTMJava.cmake</td>
    <td>Module for obtaining OpenRTM-aist-Java environment settings (for CMake)</td>
  </tr>
  <tr>
    <td>cmake/</td>
  </tr>
  <tr>
    <td>uninstall_target.cmake.in</td>
    <td>Template file for adding an uninstall target (for CMake)</td>
  </tr>
  <tr>
    <td>cpack_options.cmake</td>
    <td>Module for creating WiX packages (for CMake/WiX)</td>
  </tr>
  <tr>
    <td>License.rtf</td>
    <td>License display included in package information (for CMake/WiX)</td>
  </tr>
  <tr>
    <td>cpack_resources/</td>
  </tr>
  <tr>
    <td>wix.xsl.in</td>
    <td>Template for specifying files to include in the WiX package (for CMake/WiX)</td>
  </tr>
</table>

<br>

- Python

<table class="table-alt">
  <tr style="text-align: center;">
    <td>File Name</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>&lt;RTC name&gt;.py</td>
    <td>Code of the RT component.</td>
  </tr>
  <tr>
    <td>&lt;service type name&gt;_idl.py</td>
  </tr>
  <tr>
    <td>&lt;service type name&gt;_idl_example.py</td>
    <td>Implementation file of the service provider. (*)</td>
  </tr>
  <tr>
    <td>CMakeLists.txt</td>
    <td>Configuration file for CMake.</td>
  </tr>
  <tr>
    <td>doc/</td>
  </tr>
  <tr>
    <td>doxyfile.in</td>
    <td>Configuration file for Doxygen.</td>
  </tr>
  <tr>
    <td>cmake_modules/</td>
  </tr>
  <tr>
    <td>FindOpenRTMPython.cmake</td>
    <td>Module for obtaining OpenRTM-aist-Python environment settings (for CMake)</td>
  </tr>
  <tr>
    <td>cmake/</td>
  </tr>
  <tr>
    <td>uninstall_target.cmake.in</td>
    <td>Template file for adding an uninstall target (for CMake)</td>
  </tr>
  <tr>
    <td>cpack_options.cmake</td>
    <td>Module for creating WiX packages (for CMake/WiX)</td>
  </tr>
  <tr>
    <td>License.rtf</td>
    <td>License display included in package information (for CMake/WiX)</td>
  </tr>
  <tr>
    <td>cpack_resources/</td>
  </tr>
  <tr>
    <td>Description.txt</td>
    <td>Description included in package information (for CMake)</td>
  </tr>
  <tr>
    <td>License.txt</td>
    <td>License display included in package information (for CMake/Linux)</td>
  </tr>
  <tr>
    <td>wix.xsl.in</td>
    <td>Template for specifying files to include in the WiX package (for CMake/WiX)</td>
  </tr>
</table>

<br>


* When outputting the service provider implementation file, RtcBuilder parses the IDL in order to generate operation templates. However, this parsing function has the following limitations.
- In the preprocessor, only the #include directive can be used. (#ifdef and similar directives are simply ignored.)
- The generated operations are only the operations of the directly specified interface, and do not include operations inherited from parent interfaces.


### Output Selection
If a file with the same name as a generated file already exists in the output destination, and there is a difference in output content between the existing file and the generated file, RtcBuilder displays a confirmation screen for selecting which output to use.
<br>


<div align="center"><a href="fig4-2SelectOutPut_ja.png"><img src="fig4-2SelectOutPut_ja.png" width="50%;"></a></div>
<div align="center"><strong>Output Selection Screen</strong></div>
<br>

In output selection, select from the following three output candidates.
- Original: Leave the existing file as-is
- Merge: Perform merging using merge blocks (**Note 1**)
- Generate: Overwrite with the newly generated content
<!-- -Cancel ： 既に存在するファイルをそのまま残す -->

**Note 1** In Merge, only the range enclosed by the `<rtc-template block=”block”>` tag is overwritten with the latest generated content. In the generated template, the range that users should not modify is enclosed with this tag in advance.
Anything inside this tag will disappear after modification when merged, so do not modify it.

### Perspective Switching
If a development environment plugin for the target generation language is installed, a confirmation message for switching perspectives is displayed after code generation is executed.
If the target plugin is installed, a message like the following is displayed, so select whether or not to switch perspectives.
<br>


<div align="center"><a href="fig4-3MessagePerspectiveSwitch_ja.png"><img src="fig4-3MessagePerspectiveSwitch_ja.png" width="70%;"></a></div>
<div align="center"><strong>Perspective Switching Confirmation Message</strong></div>
<br>
The relationship between the generation language and the development environment plugin is as follows.
- Java: JDT (Java Development Tools) → A development environment included in Eclipse in advance.
- C++: CDT (C/C++ Development Tooling)
- Python: PyDev

**Note:** If a development environment plugin for each language is installed and the output target project is a newly created project, the attributes of the target language are set in the properties of each project.

## Packaging Function for Generated Files
This function archives generated template files, executable binary files of RT components created based on template files, and other artifacts in various formats.
When you click the [Package] button on the Basic Profile input page, the "RT Component Packaging" screen for setting packaging details is displayed.
<br>

<div align="center"><a href="fig6-1FunctionPack_ja.png"><img src="fig6-1FunctionPack_ja.png" width="60%;"></a></div>
<!-- CENTER:''図 6-1 各種成果物のパッケージング機能'' -->
<div align="center"><strong>Packaging Function for Various Artifacts</strong></div>
<br>
<br>

<div align="center"><a href="fig6-2ExportRTC_ja.png"><img src="fig6-2ExportRTC_ja.png" width="60%;"></a></div>
<!-- CENTER:''図 6-2 RTコンポーネント エクスポート画面'' -->
<div align="center"><strong>RT Component Packaging Screen</strong></div>
<br>
Each item is explained below.
<div align="center"><strong>RT Component Packaging Screen Item Descriptions</strong></div>
<table class="table-alt">
  <tr>
    <td>Item</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>Target Project</td>
    <td>Select the project to be packaged.</td>
  </tr>
  <tr>
    <td>Destination Directory</td>
    <td>Enter the directory to output the packaged artifacts. By using the "Browse" button, a directory selection dialog is displayed.</td>
  </tr>
  <tr>
    <td>Archive Method</td>
    <td>Select the format of the archive to be created.</td>
  </tr>
  <tr>
    <td>Options</td>
    <td>Overview description of the behavior within each action. This item can be omitted.</td>
  </tr>
  <tr>
    <td>Archive Format</td>
    <td>It is possible to create archives using the ZIP format and archives using the tar format. Select the format to use.</td>
  </tr>
  <tr>
    <td>Compress Archive Contents</td>
    <td>If you want to compress the archive contents, turn on the checkbox.</td>
  </tr>
  <tr>
    <td>Directory Structure</td>
    <td>Select whether to archive while preserving the directory structure of the target project as-is, or to archive with everything placed in the root directory.</td>
  </tr>
</table>
**Note:** For each archive method ("source", "binary", "source + binary"), which file types are included in the archive can be configured on the "Settings Screen" described later.

<br>

## Saving and Loading Settings 
RTCBuilder can save the content entered in the RTC Profile Editor to an RTC profile XML (RTC.xml), and can load the saved content again.


### Save
The content entered in the RTC Profile Editor can be saved to an RTC profile XML (RTC.xml). The entered content can be saved by the following operations.
- Right-click the editor and select [Save] or [Save As...] from the displayed context menu
- Select [File] > [Save...] or [File] > [Save As...] from the menu bar


**Note:** If [Save As...] is selected, it can be saved in any project.
<br>


<table class="table-alt">
  <tr>
    <td><div align="center"><a href="fig5-1Save_ja.png"><img src="fig5-1Save_ja.png" width="60%;"></a></div></td>
    <td><div align="center"><a href="fig5-1Save2_ja.png"><img src="fig5-1Save2_ja.png" width="60%;"></a></div></td>
  </tr>
  <tr>
    <th colspan="2">Save</th>
  </tr>
</table>
<br>

<!-- ''　※''任意のプロジェクト以外のディレクトリーを保存先に指定した場合は、以下のメッセージが表示され保存されません。保存先を任意のプロジェクト内のディレクトリーに指定し直してください。 -->
<!-- #br -->
<!--  -->
<!-- #ref(SaveError.png,nolink,center) -->
<!-- CENTER:''保存先の指定が不正の場合のエラー'' -->
<!--  -->
### Load
The RTC profile XML (RTC.xml) that stores the content of the RTC Profile Editor can be loaded by the following operations.
- Right-click the editor and select [Open] from the context menu
- Select [File] > [Open File...] from the menu bar
<br>


<table class="table-alt">
  <tr>
    <td><div align="center"><a href="fig5-2Load_ja.png"><img src="fig5-2Load_ja.png" width="60%;"></a></div></td>
    <td><div align="center"><a href="fig5-2Load2_ja.png"><img src="fig5-2Load2_ja.png" width="60%;"></a></div></td>
  </tr>
  <tr>
    <th colspan="2">Load</th>
  </tr>
</table>
<br>
