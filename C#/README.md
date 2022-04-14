# C\# Programming Guide

This guide will guide you through the process of setting up a console application project in visual studio, adding references to the necessary libraries, and using the example provided.

### Prerequisites

  - Microsoft Visual Studio with the C\# and .NET development packages
  - Thorlabs Kinesis
  - A KDC101 Controller
  - A connected instrument
    * e.g. a DDR25/M

## Setting up Your Project

This section details the steps necessary to create your project such that it compiles correctly when you add the example file. These steps are general and vary little between examples. If you have any comments or feedback for this guide, please add them to the "Issues" section of the repository.

  - Open Visual Studio, and select "Create new project..." from the opening screen.
    - Alternatively, select File->New->Project 
  - In the resulting "New Project" Window, select "Console App (.NET Framework) from the Visual C# section
  - Choose an appropriate name and location for your project (e.g. KDC101_Console for a KDC101 project)
    - The default file path for Visual Studio projects is "C:\Users\<username>\source\repos". 
      - This can be changed by going to Tools->Options, selecting Projects->Locations, and clicking on the "..."


### Adding Project Dependencies to Your Project Folder

In order for the project to compile successfully, you will need to add library references to your project. For simplicity, the appropriate Kinesis DLLs should be copied into your project folder.

  - Open File Explorer and navigate to your Kinesis Installation folder
    - "C:\Program Files\Thorlabs\Kinesis" for 64-bit installations
    - "C:\Program Files\Thorlabs\Kinesis" for 32-bit installations
  - Open Thorlabs.MotionControl.Kinesis.DLLUtility.exe
    - This utility is designed to help you select only the libraries you need for your project, with no unnecessary files
  - Select the type of project from the drop down menu at the top of the program
    - In this case: .NET (no UI)
  - Change the destination folder to <Your Project Folder>\Bin\Debug
    - You may need to change the source folder to your Kinesis installation folder. Check that this is correct.

Alternatively, you may copy and paste the required files yourself, without using the utility. When using this option, the easiest method is to simply copy and paste all of the files into your projects Bin\Debug folder. This has the disadvantage of copying files that you will not need, however.


### Targeting Your Solution

Depending on which set of DLLs you intend to use (32- or 64-bit), you will need to select an appropriate build target for your solution. Failing to do so is a common source of build errors.

  - Open the solution explorer if it's not open already
    - The easiest method is to use the CTRL+ALT+L shortcut
  - Right click on your project in the solution explorer and select "Properties"
  - In the resulting menu, navigate to "Build" and select your platform target from the drop-down menu
    - Select "x86" if you're using the 32-bit DLLs, and "x64" otherwise.


### Adding References

For any of the examples present in this repository, Visual Studio requires references to a devices dependencies. Some of these dependencies are shared between multiple devices, while others are specific to one device. The exact dependencies required will be listed in the folder for each example.

  - Open solution explorer if it's not open already
  - Right click on your project and select Add->References from the right-click context menu
    - This will bring up a new menu. If you have done this recently, old references will still be present and it may be necessary to clear them before continuing
  - Select "Browse" and navigate to where you saved the Kinesis libraries copied previously (Bin\Debug)
  - Select the following DLLs, which are common to all examples:
    - Thorlabs.MotionControl.DeviceManagerCLI
    - Thorlabs.MotionControl.Tools.Logging
    - Thorlabs.MotionControl.Tools.Common
  - Select the DLLs listed in the example folder


## Adding the Example Code

With your project set up, it is now time to add the example code to your file. By default, Visual Studio sets up a project with a file containing "program.cs" that is uses as the main input when compiling.

Ensure the correct references for your device have also been added before continuing.

To add the example script to your project, first download it from the repository (note: GitHub may only allow you to download the repository in it's entirety). Copy and paste the file into the top level of your project folder (where the project file is located). Next, add the file to your project by righting clicking on the project in the solution explorer and going to "Add->Existing Item" (alternatively, use the shortcut ALT+SHIFT+A). Select the example in your project folder to add it to the project. If "Program.cs" is present in your project, remove it and delete the file.

Alternatively, you may wish to simply copy and paste the example code from GitHub straight into the "program.cs" file. This solution may be more simple.


