# C++ Programming Guide

This guide will walk you through the process of creating a C++ project in visual studio, linking the necessary libraries, and filling out the code.

### Prerequisites

  - Microsoft Visual Studio with the Visual C++ packages installed
  - An installation of Kinesis 
  - A compatible MotionControl Device

## Creating a New Visual C++ Project

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
