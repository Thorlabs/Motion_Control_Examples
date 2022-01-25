# C++ Programming Guide

This guide aims to help you set up and compile a C++ project using our examples, either by using the Visual Studio project, or creating a project from scratch. If you cloned the entire repository, then you will have access to a solution that contains all examples. As such, this guide is split into 2 parts:

  - Using the Existing Project in the MotionControl_Examples Solution
  - Creating a New Visual C++ Project in Visual Studio from scratch

Frequently asked questions will be added to the end of this file.

## Using C++ Projects in the Existing Solution

### Requirements

  - Microsoft Visual Studio
    - Community for hobby projects, Professional for business.
  - Windows 10 or higher

### Cloning the repository

All example projects are include in the visual studio solution in the top directory of this repository. Building a project from within the solution is the most straightforward way of using these examples, but requires that you download the entire repository. To do this, click the green "code" button located at the top right on the repository's first page. Then select "Download Zip, or clone the repository.

### Adding the Kinesis DLLs to Your Chosen Project

### A Note of stdafx.h

The Kinesis library makes calls and references to Windows' standard libraries. In order to improve compilation speed, these libraries are included in precompiled headers, referenced in "stdafx.h".
It is recommended to include this file in your project. If not, the header file generally includes the following libraries:

  - "targetver.h"
  - <WS2tcpip.h>
  - <windows.h>
  - <stdio.h>
  - <tchar.h>.

Kinesis' dependence on Windows libraries is the reason for it's incompatibility with Linux. For Linux programming, please refer to our Serial communications examples.

## Referencing Kinesis Libraries

  - Refer to Linker settings
  - Additional Include Directories (optional step)
  - Specificy .lib file to use
  - Point to device examples for the correct .lib file (include as comment?
