---
layout: page
title: "bulk installation scripts"

---

<!-- Title: Bulk Installation Scripts -->
<!-- #contents(5) -->

## Downloading Bulk Installation Scripts

The following installation scripts are provided by openrtm.org.

To obtain a script, right-click one of the links below and select **"Copy Link Location"** (Firefox) to obtain the URL, then download it using a command such as `wget` (examples are provided below). Alternatively, select **"Save Link As..."** (Firefox) to download the script directly.

Downloaded scripts should be executed with root privileges.

These scripts install the required packages sequentially using `apt-get`.

- [Ubuntu Bulk Installation Script](https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_ubuntu.sh)
- [Debian Bulk Installation Script](https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_debian.sh)
- [Raspbian Bulk Installation Script](https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_raspbian.sh)
- [Fedora Bulk Installation Script](https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/pkg_install_fedora.sh)

By specifying options, these scripts can install packages appropriate for your intended use.

However, these scripts install all OpenRTM-aist-related packages, which may include packages that are not required for your environment.

If you fully understand the package dependencies, manual installation is also possible.

<span style="color:red;">*Please verify the version number of the Ubuntu and Raspbian scripts.</span>

To install OpenRTM-aist 1.2.2 with Python 3 support, you must use the corresponding script version.

You can check the script version as shown below. If the version number cannot be obtained, the script is outdated.

Ubuntu scripts require version **2.0.0.05** or later, and Raspbian scripts require version **2.0.0.03** or later.

```bash
$ sh pkg_install_ubuntu.sh --version
2.0.0.05
````

```bash
$ sh pkg_install_raspbian.sh --version
2.0.0.03
```

## pkg_install_{ubuntu|debian|raspbian}.sh Scripts

The available options are the same for all scripts.

However, `pkg_install_raspbian.sh` does not support OpenRTP installation. Therefore, `openrtp` cannot be specified as an argument to the `-l` option.

<span style="color:red;">*The `-t` option is supported only by the Ubuntu and Raspbian scripts.</span>

### Available Options

```text
Usage:
  pkg_install_ubuntu.sh -l {all|c++} [-r|-d|-s|-c] [-t OpenRTM-aist old version number] [-u|--yes]
  pkg_install_ubuntu.sh [-u|--yes]
  pkg_install_ubuntu.sh -l {python} [-r|-d|-c] [-t OpenRTM-aist old version number] [-u|--yes]
  pkg_install_ubuntu.sh -l {java} [-r|-d|-c] [-u|--yes]
  pkg_install_ubuntu.sh -l {openrtp|rtshell} [-d] [-u|--yes]
  pkg_install_ubuntu.sh {--help|-h|--version}

Example:
  pkg_install_ubuntu.sh [= pkg_install_ubuntu.sh -l all -d]
  pkg_install_ubuntu.sh -l all -d
  pkg_install_ubuntu.sh -l c++ -c --yes
  pkg_install_ubuntu.sh -l all -u

Options:
  -l <argument>  language or tool {c++|python|java|openrtp|rtshell|all}
     all         install packages for all supported languages and tools
  -r             install robot component runtime
  -d             install packages for robot component developers [default]
  -t <argument>  install an older OpenRTM-aist version
  -s             install packages required for building from source code
  -c             install packages required for core developers
  -u             uninstall packages
  --yes          automatically answer yes to prompts
  --help, -h     display help
  --version      display version number
```

The option `-l all` specifies that packages for all supported languages and tools should be installed.

Depending on the selected options, the packages shown below will be installed.

### List of Installed DEB Packages

Packages shown in red are removed when the `-u` (uninstall) option is specified.

<span style="color:red;">*Starting with OpenRTM-aist 1.2.2, Python support was migrated from Python 2 to Python 3, so the following packages are installed.</span>

```text
omniidl-python3
openrtm-aist-python3
openrtm-aist-python3-example
openrtm-aist-python3-doc
```

<div align="center"><a href="deb-list.png"><img src="deb-list.png" width="80%;"></a></div>

## pkg_install_fedora.sh

### Available Options

```text
Usage:
  pkg_install_fedora.sh -l {all|c++} [-r|-d|-s|-c] [-u|--yes]
  pkg_install_fedora.sh [-u|--yes]
  pkg_install_fedora.sh -l {python|java} [-r|-d|-c] [-u|--yes]
  pkg_install_fedora.sh -l {openrtp|rtshell} [-d] [-u|--yes]
  pkg_install_fedora.sh {--help|-h|--version}

Example:
  pkg_install_fedora.sh [= pkg_install_fedora.sh -l all -d]
  pkg_install_fedora.sh -l all -d
  pkg_install_fedora.sh -l python -c --yes

Options:
  -l <argument>  language or tool {c++|python|java|openrtp|rtshell|all}
      all        install packages for all supported languages and tools
  -r            install robot component runtime
  -d            install packages for robot component developers [default]
  -s            install packages required for building from source code
  -c            install packages required for core developers
  -u            uninstall packages
  --yes         automatically answer yes to prompts
  --help, -h    display help
  --version     display version number
```

### List of Installed RPM Packages

Packages shown in red are removed when the `-u` option is specified.

<div align="center"><a href="rpm-list.png"><img src="rpm-list.png" width="80%;"></a></div>

## Using the Bulk Installation Scripts

The following examples demonstrate how to download and install OpenRTM-aist using the bulk installation scripts.

(Replace the word **ubuntu** with **debian**, **raspbian**, or **fedora** as appropriate for your target distribution.)

Download the installation script appropriate for your environment using the following command:

```bash
$ wget <download URL of pkg_install_ubuntu.sh>
```

#### Installing the C++ Edition

The following example is recommended for first-time users installing the C++ edition.

Simply add the `-l` option to specify the target language. No other options are required (or you may explicitly specify `-d`) to perform the default installation.

```bash
$ sudo sh ./pkg_install_ubuntu.sh -l c++
# During installation, several prompts will appear.
# Enter 'y' or 'Y' when prompted.
```

#### Installing the Python Edition (Without Prompting for "Y")

The following example is recommended for first-time users installing the Python edition.

Adding the `--yes` option suppresses installation confirmation prompts.

Since no other options are specified, the installation is equivalent to specifying the `-d` option.

```bash
$ sudo sh ./pkg_install_ubuntu.sh -l python --yes
```

#### Installing the C++ Edition, Python Edition, and Core Development Packages

Adding the `-c` option installs packages required for core development of OpenRTM-aist itself.

The `--yes` option suppresses confirmation prompts.

```bash
$ sudo sh ./pkg_install_ubuntu.sh -l c++ -l python -c --yes
```

#### Uninstalling the C++ Edition

Adding the `-u` option uninstalls the C++ edition.

For details on the packages that will be removed, refer to the sections:

* List of Installed DEB Packages
* List of Installed RPM Packages

```bash
$ sudo ./pkg_install_ubuntu.sh -l c++ -u
```

#### Installing an Older Version (1.2.1)

If the latest version of OpenRTM-aist is 1.2.2, you can install version 1.2.1 using the `-t` option.

This option is supported only for the C++ and Python editions.

If version 1.2.2 is already installed, executing the following commands will downgrade the installation to version 1.2.1.

```bash
$ sudo ./pkg_install_ubuntu.sh -l c++ -t 1.2.1
$ sudo ./pkg_install_ubuntu.sh -l python -t 1.2.1
```

