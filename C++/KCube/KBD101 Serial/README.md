## Example Description
This example shows how to control the KBD101 with serial commands.
It demonstrates how to set the serial port, home the stage, set the parameters, move the stage and read the status of the stage.

## Preparation
The electrical interface within the Thorlabs controllers uses a Future Technology Devices International (FTDI), type FT232BM USB peripheral chip to communicate with the host PC. The complete communications protocol can be found in the "Communications Protocol" tab of the following link:
https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control&viewtab=0  

**Configuration Wizard is written for Windows OS in mind.**
### Install the driver
The driver can be installed in two methods:
1. Install the Thorlabs Motion Controller Software Kinesis, then the FTDI driver will be installed automatically. In this case, the library files can be found in C:\Program Files\Thorlabs\Kinesis\Drivers\Kinesis\VCP Driver or C:\Program Files (x86)\Thorlabs\Kinesis\Drivers\Kinesis\VCP Driver according to the bit of the software.  
Download Link of the Kinesis: https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control&viewtab=0

2. Install the FTDI driver from the official website. The installation guide can be found on the download page.   
Download Link of the FTDI driver: https://ftdichip.com/drivers/d2xx-drivers/
### Setup a Virtual Communication Port
After installing the driver, please follow the following steps to setup a Virtual Communication Port for Windows OS. 
1. Power up the KCube and connect the device to the PC using the USB cable
2. Open the device manager by selecting Start/Control Panel/Device Manager/
3. Click ‘USB Serial Bus Controllers’ and select the APT USB Device to be configured, then right click and select ‘Properties’.
4. Select the ‘Advanced’ tab, and check the ‘Load VCP’ box.
5. Click OK, then power cycle the device being configured.
6. In the device manager, click ‘Ports (COM & LPT)’, and note the ‘APT USB Device Serial Port’ COM port number (e.g. COM3). This COM port can then be used for low level protocol messages.

## Instructions for Operating the Example
Guides written for this example are written with Microsoft's Visual Studio in mind. Other IDEs can be used, but instructions are not provided in this repository.
1) Create a new VC++ project file or open the existed VC++ project file
2) Under the Solution Explorer, right click the Source Files, then add the Source.cpp to the Source Files
3) Set the path of the header file:   
   a. Open Project\Properties\Configuration Properties\C/C++\General  
   b. Enter the path of the header file **ftd2xx.h** into Additional include Directories 
4) Set the path of the library:  
   a. Open Project\Properties\Configuration Properties\Linker\General  
   b. Enter the path of the library files **ftd2xx.lib** into Additional Library Directories 
5) Set additional depended library:  
   a. Open Project\Properties\Configuration Properties\Linker\Input  
   b. Enter the name of the additional depended library **ftd2xx.lib** into Additional Dependencies
