# C++ Programming Guide

This guide will walk you through some of the options for getting any of the include examples up and running in Visual Studio. The two options covered here are:

 - Opening and building the example from within the MotionControl_Examples Solution
 - Creating your own Visual C++ project from scratch.

The repository is set up as a visual studio solution, which can be downloaded in full by cloning the repository.
Each example in the solution is set within it's own project, and set up with all references required for the project to compile.
As a result, it is the simplest method for getting a project up and running quickly, but with the caveat that you must download all examples in order for it to work.  

If you're project only requires an example for one device, then you may also create a Visual C++ project from scratch.
The guide will explain how to set up a project, add library dependencies, and additional include directories.

For the purposes of this guide, the following are required:

  - Microsoft Visual Studio with the Visual C++ packages installed   
   - It is possible to use other IDEs, but the original repository was written using Visual Studio.
  - An installation of Kinesis    
   - Kinesis can be downloaded from [here](https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control&viewtab=0)
  - A compatible MotionControl Device (see top level README for a full list of supported devices)
 
### Note

All examples included in this section include "stdafx.h", a file that can be found in the Shared Headers folder.
"stdafx.h" includes some standard library tools, as well as targetver.h, which allows you to define Windows version you are targeting.
While stdafx.h isn't necessary for the examples to run, you will need to ensure that you include <stdio.h> and <'

## Using the MotionControl_Examples Solution

Downloading the repository and opening the Visual Studio solution is the simplest way of getting started with examples for any device.
To start, go back to the [top level of this repository](https://github.com/Thorlabs/MotionControl_Examples), and click the green "Code" button to display a drop down menu.
From this menu, choose whether you would like to download the repository as a .zip file, through Github desktop, or through the git or ssh command line interfaces.
If you do not have git or github desktop installed, then download the repository as a .zip.
Save the repository to your local machine, then extract the files into a convenient location and open it in windows file explorer.

From there, navigate through the folders to your desired device example.
For example, the project for the KDC101 can be found in 
 - ./MotionControl_Examples/C++/KCube/KDC101.   
Open the "Required DLLs.txt" file located in the project folder to see which DLLs are needed by the project.
Then, either using the DLLUtility or copy and paste, copy the required DLLs into the project folder (the same folder as the C++ file).

Open the solution (or the project) in Visual Studio and bring up the Solution Explorer (CTRL+ALT+L), then expand the project to display it's contents.
To view the main source file, expand the "Source Files" virtual folder and double-click the .cpp file.
Near the top of the source file, there is a variable called serialNo: change this to match the serial number of your device.
If you're intending to use a simulated device with Kinesis Simulator, you will need to uncomment (delete the "//" on a line) TLI_InitializeSimulations() at the top of the file, and
TLI_UninitializeSimulations() at the bottom of the file.  

Next, right click on the project in the solution explorer and select "Properties" (or press ALT+ENTER).
In the properties dialogue, ensure that the configuration is "Active(Debug)" and the platform matches your DLLs using the drop down menus.
If you are using the 32-bit DLLs, then select "x86" as your platform. Otherwise, select "x64".
Press OK to close the window.  

To build the project, go to solution explorer, right click on your chosen project's title and select "Build.

## Using C++ Projects in the Existing Solution

### Requirements

  - Microsoft Visual Studio
    - Community for hobby projects, Professional for business.
  - Windows 10 or higher

### Cloning the repository

All example projects are include in the visual studio solution in the top directory of this repository. Building a project from within the solution is the most straightforward way of using these examples, but requires that you download the entire repository. To do this, click the green "code" button located at the top right on the repository's first page. Then select "Download Zip, or clone the repository.

### Adding the Kinesis DLLs to Your Chosen Project

TODO

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
