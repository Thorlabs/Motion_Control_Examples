// Title: KDC101
// Created Date: 11/17/2025
// Last Modified Date: 11/17/2025
// .NET Framework version: 4.8
// Thorlabs DLL version: 1.2.0.25903
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// KDC101 controllers, home it, and move it by 1 mm or degrees.

using System;
using Thorlabs.MotionControl.XA;
using Thorlabs.MotionControl.XA.Products;

namespace KDC101
{
    class Program
    {
        //Change this line to match the serial number on your device
        private static string _deviceId = "27265111";

        static void Main(string[] args)
        {
            SystemManager systemManager;

            //Start up XA
            try
            {
                systemManager = SystemManager.Create();
                systemManager.Startup();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: {0}", ex.Message);
                return;
            }

            //Open the device
            Kdc101 device;
            bool ret = systemManager.TryOpenDevice(_deviceId, "", OperatingModes.Default, out device);
            if (ret == false)
            {
                Console.WriteLine("Fail to open device {0}", _deviceId);
                systemManager.Shutdown();
                return;
            }
            else
            {
                Console.WriteLine("Device {0} opened successfully", _deviceId);
            }

            try
            {
                //Enable the device
                device.SetEnableState(EnableState.Enabled, TimeSpan.FromSeconds(1));

                //Get the hardware information
                HardwareInfo hardwareInfo = device.GetHardwareInfo(TimeSpan.FromSeconds(1));
                Console.WriteLine("Device Name:{0}", hardwareInfo.PartNumber);

                //Home the device
                Console.WriteLine("Homing");
                device.Home(TimeSpan.FromSeconds(60));
                Console.WriteLine("Homing completed");

                //Set the distance. Unit: millimeters or degrees depending on the actuator
                double distance = 1; 

                //Get the unit type of the actuator
                ConnectedProductInfo productInfo = device.GetConnectedProductInfo();
                Unit deviceUnit = productInfo.UnitType;

                //Convert the distance to device unit
                long valueInDeviceUnits = device.FromPhysicalToDeviceUnit(ScaleType.Distance, deviceUnit, distance);

                //Move the device
                Console.WriteLine("Moving to {0} {1}", distance, deviceUnit.ToString());
                device.Move(MoveMode.RelativeMove, (int)valueInDeviceUnits, TimeSpan.FromSeconds(60));
                Console.WriteLine("Moving completed");

                //Get the current position
                int currentPosInDeviceUnits = device.GetPositionCounter(TimeSpan.FromSeconds(1));

                //Convert the device unit to physical unit
                UnitConversionResult currentPos = device.FromDeviceUnitToPhysical(ScaleType.Distance, currentPosInDeviceUnits);
                Console.WriteLine("Current Position: {0} {1}", currentPos.Value, currentPos.UnitType);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: {0}", ex.Message);
            }
            finally
            {
                //Close the device
                device.Disconnect();
                device.Close();

                //Shutdown XA
                systemManager.Shutdown();
            }
        }
     }
}