# MATLAB Programming Guide

This guide will guide you through using and running an example in MATLAB.

### Prerequisites

 - MATLAB software
 - Thorlabs Kinesis
 - A Thorlabs controller and compatable stage

## Available Examples

 - Benchtop Controllers
   * BBD30X controller using a DDR100 stage
   * BSC201 controller using a HDR50 stage
 - Intergrated Stages
   * LTS150 stage
 - KCube Controllers
   * KDC101 controller with a PRM1/M-Z8 stage
   * KIM101 controller
   * KSC101 controller

## FAQs

 - Accessing .NET enums in MATLAB.

To access .NET enums from the DLLs they need to be extracted. To do this you need to assign an name to the assembly, access the handle, and then access the enums. For example, to access the MotorChannels enum for the KIM101 the lines of code you will need are 

```  
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.KCube.InertialMotorCLI.dll');
channelsHandle = motCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.KCube.InertialMotorCLI.InertialMotorStatus+MotorChannels');
channelsEnums = channelsHandle.GetEnumValues();
```

And then to access channel 1 you would use channelsEnums.GetValue(0)

