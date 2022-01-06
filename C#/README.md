C\# Programming Guide

This guide will attempt to guide you through the process of setting up a console application project in visual studio, adding references to the necessary libraries, and using the example provided.

### Prerequisites

  - Microsoft Visual Studio with the C\# and .NET development packages
  - Thorlabs Kinesis
  - A KDC101 Controller
  - A connected instrument
    * e.g. a DDR25/M

## Creating Your Project

  - Open Visual Studio, and select "Create new project..." from the opening screen.
    - Alternatively, select File->New->Project 

In the resulting "New Project" Window, select "Console App (.NET Framework) from the Visual C# section, choose an appropriate name and location for your project (e.g. KDC101_Console) and press ok. This will create a new folder with your project name.

By default, the file path for Visual studio projects is "C:\Users\<your username>\source\repos. This can be changed by navigating to the tool bar and selecting Tools, and opening the options menu. Within the options menu, expand the projects and solutions menu (if not expanded already) and select "Locations". Change the Projects location by clicking on the "...", then navigate to your chosen folder.

Next, open file explorer and navigate to your Kinesis installation folder ("C:\Program Files\Thorlabs\Kinesis" for 64-bit installations or "C:\Program Files (x86)\Thorlabs\Kinesis" for 32-bit installations). Within this folder is a program named "Thorlabs.MotionControl.Kinesis.DLLutility.exe", which can be used to copy the libraries you need into your project folders Bin\\Debug folder. Alternatively, you can manually copy and paste the files.

The DLLUtility has the advantage of allowing you to select your device and target programming language; ensuring that you have all of the required libraries and their dependencies.

## Targeting Your Solution

Depending on which set of DLLs you intend to use (32- or 64-bit), you will need to select an appropriate build target for your solution. To do this, go to the solution explorer (CTRL+ALT+L will open the widget if it's not open already), right click on project and select "Properties". Then, go to the Build menu and select your platform target: if you are using the 32-bit Dlls, select "x86", otherwise select "x64". Failing to set this option is a common cause of build errors.

## Adding References

The .NET API contains a list of dependencies required in order to control the device. You will need to add some of these dependencies as references to your project. To do this, right-click the project in the solution explorer and select "Add->References", which will open a new window. In this window, select "Browse" and navigate to the folder into which you copied the Kinesis DLLs.

Select the following DLLs, which are common to all examples:

  - Thorlabs.MotionControl.DeviceManagerCLI
  - Thorlabs.MotionControl.Tools.Logging
  - Thorlabs.MotionControl.Tools.Common

Since the exact dependencies required by a project will depend upon the device being used, only the shared references are included here. Additional references required by these projects are listed within the project folders.

## Adding the Example Code

Ensure the correct references for your device have also been added before continuing.

To add the example script to your project, first download it from the repository (note: GitHub may only allow you to download the repository in it's entirety). Copy and paste the file into the top level of your project folder (where the project file is located). Next, add the file to your project by righting clicking on the project in the solution explorer and going to "Add->Existing Item" (alternatively, use the shortcut ALT+SHIFT+A). Select the example in your project folder to add it to the project. If "Program.cs" is present in your project, remove it and delete the file.

Alternatively, you may wish to simply copy and paste the example code from GitHub straight into the "program.cs" file. This solution may be more simple.

## Adjusting the Example to Use Your Device

By default, most examples are programmed to take command line inputs in the form [Program Name] [Serial Number] <Optional Arguments>. Although example serial numbers are given in the code, the scripts as-written will not use them.

Instead, they use the [Serial Number] argument.