# MotionControl_Examples
Software examples for Thorlabs'  range of motion control products (e.g. KCubes)


## How to Find an Example for Your Device in Your Chosen Language

Examples for individual devices or device groups can be found in their own individual subfolders with the "Devices" folder. Each device has at least one example written in each of three programming languages (C#, C++, and Python), each in their own subfolder. Directions on using specific examples are given within the folders.

## Requirements

All examples are built using the libraries provided with Thorlabs' Kinesis software package, which can be found [here](https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control&viewtab=0). DLLs are not provided by this repository in order to save space and ensure that the latest or most appropriate versions of the DLLs are used with your application.

Additionally, Thorlabs currently only provides DLLs for Windows. While Kinesis might be supported on Mac and Linux in the future, it is currently necessary to communicate with devices using serial commands via the FTDI chip present in all MotionControl devices. The FTDI drivers can be found [here](https://ftdichip.com/drivers/d2xx-drivers/)

### C\# and C++ Soft Requirements

Guides written for these examples are written with Microsoft's Visual Studio in mind, which can be downloaded [here](https://visualstudio.microsoft.com/).
Other IDEs can be used, but instructions are not provided in this repository.

### Python Requirements

Python examples make use of the pythonNET and cTypes modules. If pythonNET is not installed already, it can be using the command

```
pip install pythonnet
```

## Frequently Asked Questions (FAQs)

Will go here.
