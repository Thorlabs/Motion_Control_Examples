"""An example that uses the APT Communications Protocol to connect to a KBD"""
import serial 
import time

def main():
    #COM Number from loaded VCP in Device Manager
    com = serial.Serial(port = 'COM6',
                        baudrate = 115200, 
                        bytesize=8, 
                        parity=serial.PARITY_NONE, 
                        stopbits=1, xonxoff=0, 
                        rtscts=0, 
                        timeout=1
    )

    time.sleep(1)
    print(f"Port Opened? {com.is_open}")  

    """
    Command MGMSG_MOT_SET_KCUBEPOSTRIGPARAMS - Values are set as default at controller startup
    header-6bytes           26 05 2E 00 D0 01
    channel-2bytes          01 00    
    Start Position Forward-4bytes  
    Interval Forward-4bytes
    Num Pulses Forward-4bytes
    Start Position Reverse-4bytes
    Interval Reverse-4bytes
    Num Pulses Reverse-4bytes
    Pulse Width-4bytes
    Num Cycles-4bytes
    """
    command = '26 05 2E 00 D0 01 01 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 32 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
    data = bytearray.fromhex(command)
    com.write(data)     
    print("Command MGMSG_MOT_SET_KCUBEPOSTRIGPARAMS Sent")
    time.sleep(1)

    """
    Command MGMSG_MOT_SET_KCUBETRIGIOCONFIG - Used to set Trigger States and Operating Modes
    header-6bytes           23 05 16 00 D0 01
    channel-2bytes          01 00   always channel 1 for the KCube
    Trigger 1 Mode          02 00   Input trigger for relative move
    Trigger 1 Polarity      01 00   Active High
    Trigger 2 Mode          0B 00   Trigger output active when motor 'in motion'
    Trigger 2 Polarity      01 00   Active High
    Reserved                00 00 00 00 00 00 00 00 00 00 00 00     (development only)
    """
    command = "23 05 16 00 D0 01 01 00 02 00 01 00 0B 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00"
    data = bytearray.fromhex(command)
    com.write(data)
    print("Command MGMSG_MOT_SET_KCUBETRIGIOCONFIG Sent")
    time.sleep(1)

    """
    Command MGMSG_MOT_SET_MOVERELPARAMS - Used to set Relative move parameters
    header-6bytes           45 04 06 00 D0 01
    channel-2bytes          01 00   always channel 1 for the KCube
    Relative Distance       10 27 00 00 little endian conversion of 5mm = 10000 counts for DDSM100 (signed values)
    """
    command = "45 04 06 00 D0 01 01 00 10 27 00 00"
    data = bytearray.fromhex(command)
    com.write(data)
    print("MGMSG_MOT_SET_MOVERELPARAMS Sent")
    time.sleep(1)

    """
    Command MGMSG_MOD_SET_CHANENABLESTATE - Used to enable the controller
    header-6bytes           10 02 01 01 50 01  3rd byte is channel number, 4th byte is enable state (0x01 enable, 0x02 disable)
    """
    command = '10 02 01 01 50 01' 
    data = bytearray.fromhex(command)
    com.write(data)       
    time.sleep(1)
    print("Enable")
    com.flushInput()
    com.flushOutput()

    """
    Command MGMSG_MOT_MOVE_HOME - Used to home the stage
    header-6bytes           43 04 01 00 50 01
    """
    command = '43 04 01 00 50 01'   # home    
    data = bytearray.fromhex(command)
    com.write(data)
    print("Homing")
    time.sleep(5)

    """
    Send Commands or wait for triggers after home
    """

    com.close()
    

if __name__ == "__main__":
    main()
