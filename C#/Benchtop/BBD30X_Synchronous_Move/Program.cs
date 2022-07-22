using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;

namespace BBD30X_Synchronous_Move
{
    class Program
    {
        static void Main(string[] args)
        {
            // Uncomment this line (and the equivalent Uninitialize statement at the end)
            // If you are using simulations.
            SimulationManager.Instance.InitializeSimulations();


            // Serial number for Benchtop Brushless Motor (Example)
            // Change this line to match your device
            string serialNo = "103000001";

            try
            {
                // Build device list (necessary for operation)
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception raised by BuildDeviceList {0}", ex);
                Console.ReadKey();
                return;
            }

            // Get available Benchtop Brushless Motor and check our serial number is correct
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(BenchtopBrushlessMotor.DevicePrefix103);
            if (!serialNumbers.Contains(serialNo))
            {
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device and check it is the correct type
            BenchtopBrushlessMotor device = BenchtopBrushlessMotor.CreateBenchtopBrushlessMotor(serialNo);
            if (device == null)
            {
                Console.WriteLine("{0} is not a BenchtopBrushlessMotor", serialNo);
                Console.ReadKey();
                return;
            }

            // Open device
            Console.WriteLine("Opening device {0}", serialNo);
            device.Connect(serialNo);
            bool connected = device.IsConnected;
            if (!connected)
            {
                Console.WriteLine("Failed to open device {0}", serialNo);
                Console.ReadKey();
                return;
            }

            // Check bay 1 exists
            if (!device.IsBayValid(1))
            {
                Console.WriteLine("Failed to open device {0}", serialNo);
                Console.ReadKey();
                return;
            }
        }
    }
}
