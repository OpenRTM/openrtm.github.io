---
layout: page
title: views (repository view)
---

<!-- Title: ビュー（リポジトリビュー編） -->
<!-- #contents -->

This section explains the Repository View.
<br>

The Repository View has a function for loading RT component specification description files and displaying them in a tree view.
<br>

<div align="center"><a href="RTCBuilder1.1.2_041.jpg"><img src="RTCBuilder1.1.2_041.jpg" width="50%;"></a></div>
<div align="center"><strong>Repository View</strong></div>
<br>


### Loading a File
This section explains how to specify and display an RT component specification description file in the Repository View.<br>
Right-click inside the Repository View and select [Load from File] from the displayed context menu. A file selection dialog is displayed. Select the RT component specification description file to load into the Repository View.<br>
This dialog is filtered to display only xml files.
<br>

<div align="center"><a href="RTCBuilder1.1.2_042.jpg"><img src="RTCBuilder1.1.2_042.jpg" width="85%;"></a></div>
<div align="center"><strong>Loading a File</strong></div>
<br>

When a local RT component specification description file is loaded, the top level displays the absolute path of the loaded RT component specification description file.
The second level displays the value of the category attribute defined in the RT component specification description file.
The third level displays the value described in the name attribute in the RT component specification description file and the RT component specification description file name.


### Loading a Directory
This section explains how to specify a directory containing RT component specification description files and load and display all files in the directory.<br>
Right-click in the Repository View and select [Load from Directory] from the displayed context menu. A directory selection dialog is displayed.
Select the directory to load into the Repository View. RT component specification description files under the directory are loaded.
<br>

<div align="center"><a href="RTCBuilder1.1.2_043.jpg"><img src="RTCBuilder1.1.2_043.jpg" width="85%;"></a></div>
<div align="center"><strong>Loading a Directory</strong></div>
<br>

The display method is the same as when loading a file.<br>
If a new RT component specification description file is added to a directory that has already been expanded and loading is performed again, only the added RT component specification description file is loaded.
<br>


### Deletion
Components in the Repository View can be deleted by right-clicking in the Repository View and selecting [Delete] from the context menu.<br>
[Delete] can be selected only when a path, category, or component is selected.
<br>

<div align="center"><a href="RTCBuilder1.1.2_044.jpg"><img src="RTCBuilder1.1.2_044.jpg" width="50%;"></a></div>
<div align="center"><strong>Deleting a Component</strong></div>
<br>

If the path, which is the top level, is deleted, the lower-level categories and components are also deleted at the same time. Also, if a component at the third level is deleted and no other components exist, the entries are deleted recursively up to the top level.
<br>
<br>

