// Title: KBD101
// Created Date: 04/24/2026
// Last Modified Date: 09/08/2026
// .NET Core version: 8.0
// XA Version Tested: 1.9.3
// Example Description:
// This example demonstrates how to connect to a KBD101 device, home it,
// and perform an absolute move of 5 mm.

using Microsoft.VisualBasic;
using System;
using Thorlabs.MotionControl.XA;
using Thorlabs.MotionControl.XA.Products;

namespace KBD101
{
    class Program
    {
        // Change this line to match the serial number on your device.
        private static string _deviceId = "1234";

        static void Main(string[] args)
        {
            SystemManager systemManager;

            // Start up XA.
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

            // Open the KBD101 device.
            Kbd101 device;
            bool ret = systemManager.TryOpenDevice(_deviceId, "", OperatingModes.Default, out device);
            if (ret == false)
            {
                Console.WriteLine("Failed to open device {0}", _deviceId);
                systemManager.Shutdown();
                return;
            }
            else
            {
                Console.WriteLine("Device {0} opened successfully", _deviceId);
            }

            try
            {
                // Enable the device.
                device.SetEnableState(EnableState.Enabled, TimeSpan.FromSeconds(60));
                Console.WriteLine("Device enabled successfully.");

                // Get the hardware information.
                HardwareInfo hardwareInfo = device.GetHardwareInfo(TimeSpan.FromSeconds(1));
                Console.WriteLine("Device Name: {0}", hardwareInfo.PartNumber);

                // Home the device.
                Console.WriteLine("Homing...");
                device.Home(TimeSpan.FromSeconds(60));
                Console.WriteLine("Homed successfully.");

                // Distance to move.
                double distance = 5.0;

                // Get the unit type from the connected actuator.
                ConnectedProductInfo productInfo = device.GetConnectedProductInfo();
                Unit deviceUnit = productInfo.UnitType;

                // Convert the physical distance to device units.
                long valueInDeviceUnits = device.FromPhysicalToDeviceUnit(ScaleType.Distance, deviceUnit, distance);
                Console.WriteLine("Conversion from {0} mm successful. Value in device units: {1}", distance, valueInDeviceUnits);

                // Absolute move to 5 mm.
                Console.WriteLine("Moving to {0} {1}", distance, deviceUnit.ToString());
                device.Move(MoveMode.Absolute, (int)valueInDeviceUnits, TimeSpan.FromSeconds(60));
                Console.WriteLine("Absolute move successful.");

                // Get the current position.
                int currentPosInDeviceUnits = device.GetPositionCounter(TimeSpan.FromSeconds(60));
                UnitConversionResult currentPos = device.FromDeviceUnitToPhysical(ScaleType.Distance, currentPosInDeviceUnits);
                Console.WriteLine("Current Position: {0} {1}", currentPos.Value, currentPos.UnitType);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: {0}", ex.Message);
            }
            finally
            {
                // Close the device.
                device.Disconnect();
                device.Close();
                Console.WriteLine("Device closed.");

                // Shutdown XA.
                systemManager.Shutdown();
            }
        }
    }
}
