## PDXC2 Examples
Software examples for Thorlabs' PDXC2 Compact ORIC® Piezo Inertia Stage Controller.

### PDXC2_ctype.py
This example uses the Kinesis C/C++ library and the Python module 'ctypes'.

### PDXC2_pythonnet.py
This example uses the Kinesis .NET library and the Python module 'pythonNET'.

### PDXC2_serial.py
This example uses serial commands and the Python module "serial". 
#### Setup a Virtual Communication Port
Please follow the following steps to setup a Virtual Communication Port for Windows OS. 
1. Power up the device and connect the device to the PC using the USB cable.
2. Open the device manager by selecting Start/Control Panel/Device Manager/.
3. Click ‘USB Serial Bus Controllers’ and select the APT USB Device to be configured, then right click and select ‘Properties’.
4. Select the ‘Advanced’ tab, and check the ‘Load VCP’ box.
5. Click OK, then power cycle the device being configured.
6. In the device manager, click ‘Ports (COM & LPT)’, and note the ‘APT USB Device Serial Port’ COM port number (e.g. COM3). This COM port can then be used for low level protocol messages.
#### Serial Command Protocol
Please download the detailed APT Serial Commands Documentation from this link:
https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control&viewtab=2  
The example also includes some commands that are specialized for PDXC2. 
>1. **MGMSG_PZMOT_MOVE_START**  
   Command Head: `0x2100`  
   Command Structure: 00 21 (ChanIdent) (StartMove) d s  
   Data: StartMove = `0x01`: Start move, StartMove = `Others`: Don't move.  
   Description: Used to start a open/close loop move. Upon completion of the open/close loop move sequence, the controller sends a MGMSG_PZMOT_MOVE_COMPLETED. Please find the description of MGMSG_PZMOT_MOVE_COMPLETED in the APT Serial Commands documentation.  
>2. **MGMSG_PZMOT_SET_PARAMS**  
   Command Head: `0x08C0`  
   Command Structure: C0 08 (PackLen) d s + (SubCode)  
   Description: This generic parameter set/request message is used to control the functionality of the PDXC2 controllers. Need to be used with sub-message ID and Sub Code listed in below table.  
  >    * **Set_PZMOT_OpenMoveParams**  
   Sub-message ID: `0x46`  
   Sub-message Structure: (SubMsgID) (ChanIdent) (StepSize)  
     Data: SubMsgID ( word ) : always `0x46`; ChanIdent ( word ) : Channel select. Fixed to `0x1`; StepSize ( long ) : Set the move step size, range from -10000000 to +10000000.   
   Description: Used to set the open loop move parameters.  
  >    * **Set_PZMOT_CloseMoveParams**  
   Sub-message ID: `0x47`  
   Sub-message Structure: (SubMsgID) (ChanIdent) (DePos)  
   Data: SubMsgID ( word ) : always `0x47`; ChanIdent ( word ) : Channel select. Fixed to `0x1`; DePos ( long ) : Set desired position, the range is from -1000000 to +1000000 nm. The min set unit is 10nm.  
   Description: Used to set the close loop move parameters.

The complete serial commands for PDXC2 will be updated to the APT Serial Commands Documentation in the near future.  
