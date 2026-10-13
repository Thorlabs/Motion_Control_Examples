Thorlabs Hardware: KPC - K-Cube Piezo Controller and Strain Gauge Reader
https://www.thorlabs.com/thorproduct.cfm?partnumber=KPC101

Description: This VI will enable you to communicate with KPC101 in open loop mode to control Piezos via to a user set voltage. The VI will first connect and initialize the device, set a zero point, wait 10 seconds, and go in to open loop mode awaiting user command to move to a specified voltage.

Instructions: 
1) Connect your KPC101  device to your PC & power the device, ensuring your stage/actutator is connected. For full device setup, the device product manual can be found on our website here. -https://www.thorlabs.com/thorproduct.cfm?partnumber=KPC101
2) Enter the device serial number below.
3) Ensure the device move path is clear.
4) Click 'Run' in the LabVIEW Toolbar which will attempt a connection,set a zero point, and go into open loop mode in that order.
5) Await for device to be be available.
6) Input desired voltage, and press 'Set Voltage'.
7) To end the Program click 'STOP'.

Tested on labVIEW 2023 Q1 64-bit.

### Front Panel
![Front Panel](Front.PNG)

### Block Diagram
![Block Diagram](Block.PNG)