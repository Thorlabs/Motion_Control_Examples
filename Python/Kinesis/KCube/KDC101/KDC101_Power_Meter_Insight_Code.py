import time
import clr
import os

clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.KCube.DCServoCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import KCubeMotor
from Thorlabs.MotionControl.GenericMotorCLI.ControlParameters import JogParametersBase
from Thorlabs.MotionControl.KCube.DCServoCLI import *
from System import Decimal
from TLPM import TLPM
from ctypes import c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_double

def main():
    """The main entry point for the application"""
    os.add_dll_directory(os.getcwd())
    meter = TLPM()
    deviceCount = c_uint32()
    meter.findRsrc(byref(deviceCount))

    if deviceCount == 0:
        print('No connected meters')
        quit()

    resourceName = create_string_buffer(1024)
    meter.getRsrcName(c_int(0), resourceName)

    meter.open(resourceName, c_bool(True), c_bool(True))
    
    meter.setWavelength(c_double(635.0))

    #SimulationManager.Instance.InitializeSimulations()

    serial_num = str("27000001")
    
    DeviceManagerCLI.BuildDeviceList() 

    controller  = KCubeDCServo.CreateKCubeDCServo(serial_num)

    if not controller == None:
        controller.Connect(serial_num)
        if not controller.IsSettingsInitialized():
            controller.WaitForSettingsInitialized(3000)
        
        controller.StartPolling(50)
        time.sleep(.1)
        controller.EnableDevice()
        time.sleep(.1)
        config = controller.LoadMotorConfiguration(serial_num, DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings)
        config.DeviceSettingsName = str('PRM1-Z8')
        config.UpdateCurrentConfiguration()

        print('Homing Motor')
        controller.Home(60000);

        jog_params = controller.GetJogParams()
        jog_params.StepSize = Decimal(10)
        jog_params.VelocityParams.MaxVelocity = Decimal(10)     
        jog_params.JogMode = JogParametersBase.JogModes.SingleStep

        controller.SetJogParams(jog_params)

        print('Moving motor')
        controller.MoveJog(MotorDirection.Forward, 0)
        time.sleep(.25)
        while controller.IsDeviceBusy:        
            power =  c_double()
            meter.measPower(byref(power))
            print(f'{controller.Position}, {power.value*1000}')
            time.sleep(.1)

        controller.StopPolling()
        controller.Disconnect(False);
    meter.close()
    #SimulationManager.Instance.UninitializeSimulations()


if __name__ == "__main__":
    main()