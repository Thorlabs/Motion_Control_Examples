"""
Example PDXC2_serial.py
Example Date of Creation: 2024-08-22
Example Date of Last Modification on Github: 2024-08-22
Version of Python used for Testing: 3.10
Version of PDXC2 firmware: 1.0.6
==================
Example Description: The example shows how to connect to PDXC2 on Windows and Linux. 
It also shows how to move the stage in open loop and close loop mode. 
The close loop mode is only available for stages with encoder. 
"""
from struct import pack, unpack
import serial
import time

serialPort = "COM4" #find out COM port number in the Device Manager
openLoopStep = 0 #unit: step
closeLoopPos = 0 #unit: nm, minimum step: 10 nm

#Find section "4 Description of the message header" of the APT communication protocl PDF for detail
#APT communication protocl PDF can be found https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=Motion_Control&viewtab=2
destination = 0x50 #Destination Byte. 0x50 for generic USB hardware unit. 
source = 0x01 #Source Byte
channel = 0x01 #choose the channel to control. For PDXC2, the channel is set to 0x01

def main():
    
    try:
        # open serial port
        # For Windows
        ser=serial.Serial(port=serialPort ,baudrate=115200,bytesize=8,
                        parity=serial.PARITY_NONE,stopbits=1,xonxoff=0,
                        rtscts=0,timeout=1)
        # For Linux
        # use 'dmesg | grep tty' to find serial port, eventually need to change permissions for /dev/tty*
        # uncomment the following lines
        ##    ser=serial.Serial('/dev/ttyUSB0', baudrate=115200,bytesize=8,
        ##                      parity=serial.PARITY_NONE,stopbits=1,xonxoff=0,
        ##                      rtscts=0,timeout=1)  
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return -1
    
    try:
        # Flush input and output buffer
        ser.flushInput()
        ser.flushOutput()
        # Enable the stage
        channelStatus = Enable(ser)
        if channelStatus == 0:
            print("Fail to enable the channel.")
        elif channelStatus == 1:
            OpenLoopMove(ser)
            # The close loop mode is only valid for PDX series stages with encoder
            CloseLoopMove(ser)  
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ser.close()   
        print("Program finishes.")
        return 1


def Enable(ser):
    Rx = ser.read(90)
	# Request Hardware information || MGMSG_HW_REQ_INFO || 0x0005
    command = pack('<HBBBB',0x0005, 0x00, 0x00, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    # Get hardware information || MGMSG_HW_GET_INFO || 0x0006
    Rx = ser.read(90)
    if len(Rx) >= 10: 
        serialNum = unpack('<I',Rx[6:10])[0]
        print(f"Opening SN: {serialNum}")
    else:
        print("MGMSG_HW_GET_INFO: Fail to receive bytes. ")
        return -1
    
    # Flush input and output buffer
    ser.flushInput()
    ser.flushOutput()
    
    # Request device status || MGMSG_PZMOT_REQ_STATUSUPDATE ||0x08E0
    command = pack('<HBBBB',0x08E0, 0x00, 0x00, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    #Get device status of channel 1 || MGMSG_PZMOT_GET_STATUSUPDATE ||0x08E1
    Rx = ser.read(62)
    if len(Rx) >= 20:
        statusBits = unpack('<L',Rx[16:20])[0]
        # check if there are any errors in the controller's status.
        if (statusBits & 0x0F000000)!= 0:
            print(f"Status Error: 0x0{(statusBits& 0x0F000000):0x}")
            print("""Status bits:
    0x01000000 Excess current error
    0x02000000 Exces temperature error
    0x04000000 Abnormal mode detected
    0x08000000 Wrong stage detected\n""")
            return -1
    else: 
        print("MGMSG_PZMOT_GET_STATUSUPDATE: Fail to receive bytes.")
        # Flush input and output buffer
        ser.flushInput()
        ser.flushOutput() 
        return -1
    
    # Flush input and output buffer
    ser.flushInput()
    ser.flushOutput() 
    
    # enable the channel || MGMSG_MOD_SET_CHANENABLESTATE || 0x0210
    command = pack('<HBBBB',0x0210, channel, 0x01, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    # request the channel status || MGMSG_MOD_REQ_CHANENABLESTATE ||0x0211
    command = pack('<HBBBB',0x0211, channel, 0x00, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    # get the channel status || MGMSG_MOD_GET_CHANENABLESTATE ||0x0212
    channelStatus = 0
    Rx = ser.read(6)
    if len(Rx) >= 3: 
        channelStatus = unpack('<B',Rx[2:3])[0]
    else:
        print("MGMSG_MOD_GET_CHANENABLESTATE: Fail to receive bytes.")
        return -1

	# Flush input and output buffer
    ser.flushInput()
    ser.flushOutput()

    return channelStatus
    
def OpenLoopMove(ser):
    print("Open Loop Operation.")
    # Set the operating loop mode to open loop || MGMSG_PZ_SET_POSCONTROLMODE  ||0x0640
    command = pack('<HBBBB',0x0640, channel, 0x01, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    # Set the open loop move step size || MGMSG_PZMOT_SET_PARAMS (Set_PZMOT_OpenMoveParams) ||0x08C0 (sub-message ID 0x46)
    command = pack('<HBBBBHHl',0x08C0, 0x08, 0x00, destination, source, 0x46, channel, openLoopStep)
    ser.write(command)
    time.sleep(0.05)
    
    # Flush input and output buffer
    ser.flushInput()
    ser.flushOutput() 
    
    # Start Open Loop Move || MGMSG_PZMOT_MOVE_START ||0x2100
    command = pack('<HBBBB',0x2100, channel, 0x01, destination, source)
    ser.write(command)
    time.sleep(0.05)
    # Upon completion of the movement, a message will send || MGMSG_PZMOT_MOVE_COMPLETED || 0x08D6
    
    # Flush input and output buffer
    ser.flushInput()
    ser.flushOutput() 
    
    # Request device status || MGMSG_PZMOT_REQ_STATUSUPDATE ||0x08E0
    command = pack('<HBBBB',0x08E0, 0x00, 0x00, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    #Get device status and position of channel 1 || MGMSG_PZMOT_GET_STATUSUPDATE ||0x08E1
    Rx = ser.read(62)
    if len(Rx) >= 20:
        currentPos, encCount ,statusBits = unpack('<llL',Rx[8:20])
        # wait for the movement to stop
        # if Rx contains '\d6\08', it's the auto message MGMSG_PZMOT_MOVE_COMPLETED, skip and request the status again
        while ((statusBits & 0xF0) != 0) or ((b'\xd6\x08') in Rx):
            # Flush input and output buffer
            ser.flushInput()
            ser.flushOutput() 
            command = pack('<HBBBB',0x08E0, 0x00, 0x00, destination, source)
            ser.write(command)
            time.sleep(0.05)
            Rx = ser.read(62)
            currentPos, encCount ,statusBits = unpack('<llL',Rx[8:20])
        print(f"The stage stops at {currentPos} steps.")
        # Flush input and output buffer
        ser.flushInput()
        ser.flushOutput() 
        return 1
    else: 
        print("MGMSG_PZMOT_GET_STATUSUPDATE: Fail to receive bytes.")
        # Flush input and output buffer
        ser.flushInput()
        ser.flushOutput() 
        return -1

    
def CloseLoopMove(ser):
    print("Close Loop Operation.")
    # Set the operating loop mode to close loop || MGMSG_PZ_SET_POSCONTROLMODE ||0x0640
    command = pack('<HBBBB',0x0640, channel, 0x02, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    # Flush input and output buffer
    ser.flushInput()
    ser.flushOutput()
    
    # Request device status || MGMSG_PZMOT_REQ_STATUSUPDATE ||0x08E0
    command = pack('<HBBBB',0x08E0, 0x00, 0x00, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    #Get device status of channel 1 || MGMSG_PZMOT_GET_STATUSUPDATE || 0x08E1
    Rx = ser.read(62)
    if len(Rx) >= 20:
        statusBits = unpack('<L',Rx[16:20])[0]
        # check if the stage is set to close loop mode
        if (statusBits & 0x800)!= 0x800:
            print("Fail to set the mode to close loop mode.")
            return -1
    else: 
        print("MGMSG_PZMOT_GET_STATUSUPDATE: Fail to receive bytes.")
        ser.flushInput()
        ser.flushOutput() 
        return -1
    
    # Flush input and output buffer
    ser.flushInput()
    ser.flushOutput()
    
    # home the stage || MGMSG_MOT_MOVE_HOME ||0x0443
    command = pack('<HBBBB',0x0443, channel, 0x00, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    # Upon completion of home sequence, a message will send || MGMSG_MOT_MOVE_HOMED || 0x0444
    startTime = time.time()
    Rx = bytearray()
    while len(Rx) < 6:
        new_data = ser.read(ser.inWaiting() or 1)
        Rx.extend(new_data)
        time.sleep(0.01)
        endTime = time.time()
        # overtime break
        if endTime - startTime > 30:
            print(f"Fail to home the stage")
            return -1

    print("The stage is Homed.")
    
    # Flush input and output buffer
    ser.flushInput()
    ser.flushOutput() 
    
    #Set Close Loop Move Parameter|| MGMSG_PZMOT_SET_PARAMS (Set_PZMOT_CloseMoveParams) ||0x08C0 (sub-message ID 0x47)
    command = pack('<HBBBBHHl',0x08C0, 0x08, 0x00, destination, source, 0x47, channel, closeLoopPos)
    ser.write(command)
    time.sleep(0.05)
    
    # Flush input and output buffer
    ser.flushInput()
    ser.flushOutput() 
    
    #Start Close Loop Move || MGMSG_PZMOT_MOVE_START ||0x2100
    command = pack('<HBBBB',0x2100, channel, 0x01, destination, source)
    ser.write(command)
    time.sleep(0.05)
    # Upon completion of the movement, a message will send || MGMSG_PZMOT_MOVE_COMPLETED || 0x08D6
    
    # Flush input and output buffer
    ser.flushInput()
    ser.flushOutput() 
    
    # Request device status || MGMSG_PZMOT_REQ_STATUSUPDATE ||0x08E0
    command = pack('<HBBBB',0x08E0, 0x00, 0x00, destination, source)
    ser.write(command)
    time.sleep(0.05)
    
    #Get device status and position of channel 1 || MGMSG_PZMOT_GET_STATUSUPDATE ||0x08E1
    Rx = ser.read(62)
    if len(Rx) >= 20:
        currentPos, encCount ,statusBits = unpack('<llL',Rx[8:20])
        # wait for the movement to stop
        # if Rx contains '\d6\08', it's the auto message MGMSG_PZMOT_MOVE_COMPLETED, skip and request the status again
        while ((statusBits & 0xF0) != 0) or ((b'\xd6\x08') in Rx):
            # Flush input and output buffer
            ser.flushInput()
            ser.flushOutput() 
            command = pack('<HBBBB',0x08E0, 0x00, 0x00, destination, source)
            ser.write(command)
            time.sleep(0.05)
            Rx = ser.read(62)
            currentPos, encCount ,statusBits = unpack('<llL',Rx[8:20])
        print(f"The stage stops at {currentPos} nm.")
        # Flush input and output buffer
        ser.flushInput()
        ser.flushOutput() 
        return 1
    else: 
        print("MGMSG_PZMOT_GET_STATUSUPDATE: Fail to receive bytes.")
        # Flush input and output buffer
        ser.flushInput()
        ser.flushOutput() 
        return -1


if __name__ == "__main__":
    main()


