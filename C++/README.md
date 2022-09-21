# C++ Programming Guide

This guide will walk you through some of the options for getting any of the included examples up and running in Visual Studio. The two options covered here are:

 - Opening and building the example from within the MotionControl_Examples Solution
 - Creating your own Visual C++ project from scratch.

The repository is set up as a visual studio solution, which can be downloaded in full by cloning the repository.
Each example in the solution is set within it's own project, and set up with all references required for the project to compile.
As a result, it is the simplest method for getting a project up and running quickly, but with the caveat that you must download all examples in order for it to work.  

If you're project only requires an example for one device, then you may also create a Visual C++ project from scratch.
The guide will explain how to set up a project, add library dependencies, and additional include directories.

For the purposes of this guide, the following are required:


  - Microsoft Visual Studio with the Visual C++ packages installed
   - When installing Visual Studio, check the "Desktop development with C++" option under "Desktop and Mobile. 
   - It is possible to use other IDEs, but the original repository was written using Visual Studio.
  - An installation of Kinesis    
   - Kinesis can be downloaded from [here](https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control&viewtab=0)
  - A compatible MotionControl Device (see top level README for a full list of supported devices)
 

## Using the MotionControl_Examples Solution


### Opening the Project for Your Device(s)

Downloading the repository and opening the Visual Studio solution is the simplest way of getting started with examples for any device.
To start, go back to the [top level of this repository](https://github.com/Thorlabs/MotionControl_Examples), and click the green "Code" button to display a drop down menu.
From this menu, choose whether you would like to download the repository as a .zip file, through Github desktop, or through the git or ssh command line interfaces.
If you do not have git or github desktop installed, then download the repository as a .zip.
Save the repository to your local machine, then extract the files into a convenient location and open it in windows file explorer.

From there, navigate through the folders to your desired device example.
For example, the project for the KDC101 can be found in 
 - ./MotionControl_Examples/C++/KCube/KDC101.   

Open the "Required DLLs.txt" file located in the project folder to see which DLLs are needed by the project.
These DLL's are bundled with installations of Kinesis, and can be found in C:\Program Files\Thorlabs\Kinesis folder for 64-bit installations, and C:\Program Files (x86)\Thorlabs\Kinesis for 32-bit installations
Once you have found the required DLLs, copy and paste them into the project folder (the same folder as the source file).
Alternatively, you may use the DLLUtility (also located in the Kinesis installation folder) to automatically select and copy the files for you.

Open either the main solution file, "MotionControl_Examples.sln" (located at the top level of this repository), or the project file for your device of choice (file extension .vcxproj)
and press "CTRL + ALT + L" on your keyboard to bring up the solution explorer.
You may be prompted to upgrade the platform toolset, depending on which version of visual studio you are using; selecting "No" can prevent you from building the project.
To view the main source file, expand the "Source Files" virtual folder and double-click the .cpp file.
Near the top of every source file, there is a variable called serialNo or testSerialNo: change the value of this string to match the serial number of your device.
If you're intending to use a simulated device with Kinesis Simulator, you will need to uncomment (delete the "//" on a line) TLI_InitializeSimulations() at the top of the file, and
TLI_UninitializeSimulations() at the bottom of the file.
You will also need to use the serial number provided by the Kinesis Simulator for the simulated device (the simulator default is used as the placeholder in the source file, so you might not need to do this).

Next, right click on your selected project in the solution explorer and select "Properties" (or press ALT+ENTER).
For example, if you are opening the KDC101 example, right-click on the "KDC101" title in the solution explorer.
In the properties dialogue, ensure that the configuration is "Active(Debug)" and the platform matches your DLLs using the drop down menus.
If you are using the 32-bit DLLs, then select "x86" as your platform. Otherwise, select "x64".
Press OK to close the window.  

To build the project, go to solution explorer, right click on your chosen project's title and select "Build.



## Referencing Kinesis Libraries

All of the C++ projects in the Motion_Control_Examples solution have a .lib file as input to the linker. 
For these projects to build correctly, you will need to save the .lib file and its associated .dll and .h files into the project directory.
DLL and Lib files are not uploaded to this repository to save on space, as well as to encourage users to make use of the latest DLLs.

The C API libraries can be found in the Kinesis installation folder on Windows.
If you are using a 32-bit installation on 32-bit Windows or a 64-bit installation on 64-bit Windows, then the program will be installed in C:\Program Files\Thorlabs\Kinesis\ .
Users with a 32-bit installation on a 64-bit Windows may find the install folder under C:\Program Files (x86)\Thorlabs\Kinesis.
Generally speaking, C++ examples have two dependencies:
 - The device specific dependency (e.g. Thorlabs.MotionControl.KCube.BrushlessMotor.dll for the KBD101)
 - A Generic Device dependency (Thorlabs.MotionControl.DeviceManager.dll)
To use these examples, you will need to copy a minimum of 4 files from the installation folder to the project folder for a single device. 
These include the device specific dependencies with extensions .dll, .lib, and .h and the DeviceManager dll.

Alternatively, you may wish to use the DLLUtility in the Kinesis installation folder to copy the files.
This utility allows you to select a programming language and the devices you wish to use, and copies the DLLs directly to the project folder.
The advantage of using this tool is that it elimates guesswork, and ensures you have the correct DLLs and .lib files.

### Adding the Library to Your Linker Settings

Although each project in this repository already adds the .lib file to the Linker, you may also want to add your own.
To do this, open the project properties by right-clicking on the project and selecting "Properties", or by pressing ALT+ENTER.
Under configuration properties, expand the linker options and click "Input" and click the "Additional Dependencies" text box.
Click the arrow to bring up the drop-down menu and select "Edit", then type a comma-separated list of any libraries you wish to include.
By default, this will follow the relative filepath from the project file: if you wish to use a library in another folder,
you can edit the "Additional Library Directories" under the General Linker settings.