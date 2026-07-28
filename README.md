# MotionControl_Examples
Software examples for Thorlabs'  range of motion control products 

https://www.thorlabs.com/motion-control

**Benchtop Controllers**

BBD101, BBD102, BBD103, BBD201, BBD202, BBD203, BBD301, BBD202, BBD203,
BPC101, BPC103, BPC201, BPC203, BPC301, BPC303, PDXC2, UDXC,
BDC101, BDC103, M30X, M30XY, MTRS,
BNT001,
PPC001, PPC102,
BSC101, BSC102, BSC103, BSC201, BSC202, BSC203,
BVC101

**Integrated Stages**

GNM, K10CR1, LTS150, LTS300, L490MZ, MLJ050, MLJ150,
MPC220, MPC320,
MFF101

**Modular Rack**

MMR601

**K-Cubes**

KBD101, KVC101,
KDC101,
KIM001, KIM101,
KPA101,
KSC101,
KST101,
KSG101,
KPZ101,
KPC101,
KNA101

**T-Cubes**

TTC001,
TSG001,
TST001, TST101,
TSC001,
TPA101, TQD001,
TPZ001,
TNA001,
TLS001,
TLD001,
TIM101,
TBD001,
TDC001,
TPA101, TQD001



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

