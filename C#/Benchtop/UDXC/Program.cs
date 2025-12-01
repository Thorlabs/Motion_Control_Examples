// Title: UDXC
// Created Date: 10/27/2025
// Last Modified Date: 10/27/2025
// .NET Framework version: 4.8.2
// Thorlabs DLL version: Kinesis 1.14.56
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs UDXC Benchtop controllers.

using System;
using System.Collections.Generic;
using System.Threading;
using System.Timers;
using Thorlabs.MotionControl.Benchtop.PiezoCLI.UDXC;
using Thorlabs.MotionControl.DeviceManagerCLI;

namespace UDXC_CSharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Uncomment this line (and SimulationManager.Instance.UninitializeSimulations() at the end on Main)
            // If you are using a simulated device
            // SimulationManager.Instance.InitializeSimulations();

            // Enter the serial number for your device
            string serialNo = "122000001";

            try
            {
                // Tell the device manager to get the list of all devices connected to the computer
                DeviceManagerCLI.BuildDeviceList();
            }
            catch (Exception ex)
            {
                // An error occurred - see ex for details
                Console.WriteLine("Exception raised by BuildDeviceList {0}", ex);
                Console.ReadKey();
                return;
            }

            // Get available UDXC and check out serial number is correct - by using the device prefix
            // (i.e. for serial number 122000123, the device prefix is 122)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(InertialStageController.DevicePrefix_UDXC);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a UDXC or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device
            InertialStageController device = InertialStageController.CreateInertialStageController(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a UDXC Controller", serialNo);
                Console.ReadKey();
                return;
            }

            // Open a connection to the device.
            try
            {
                Console.WriteLine("Opening device {0}", serialNo);
                device.Connect(serialNo);
            }
            catch (Exception)
            {
                // Connection failed
                Console.WriteLine("Failed to open device {0}", serialNo);
                Console.ReadKey();
                return;
            }

            // Wait for the device settings to initialize - timeout 5000ms
            if (!device.IsSettingsInitialized())
            {
                try
                {
                    device.WaitForSettingsInitialized(5000);
                }
                catch (Exception)
                {
                    Console.WriteLine("Settings failed to initialize");
                }
            }

            // Display info about device
            DeviceInfo deviceInfo = device.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Start the device polling
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
            device.StartPolling(200);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the device otherwise any move is ignored 
            device.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Call GetUDXCConfiguration on the device to initialize the settings
            UDXCConfiguration udxcConfiguration = device.GetUDXCConfiguration(serialNo, DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings);
            UDXCSettings currentDeviceSettings = UDXCSettings.GetSettings(udxcConfiguration);
            device.SetSettings(currentDeviceSettings, true, true);

            // Performance Optimize
            device.PulseParamsAcquireStart();
            Thread.Sleep(500);
            Console.WriteLine("Optimizing performance, please wait...");
            // When IsPulseParamsAcquired is true, it indicates the optimization has finished
            while (device.Status.IsPulseParamsAcquired == false)
                Thread.Sleep(500);

            //Home the stage - timeout 60000ms
            Console.WriteLine("Home the device");
            device.Home(60000);

            //Optionally move the stage to target position (position is set in "nm")
            int closeLoopPosition = 0;
            if (closeLoopPosition != 0)
            {
                // Set the target position
                device.SetClosedLoopTarget(closeLoopPosition);

                // Get and Set the velocity and acceleration
                UDXCClosedLoopParams closedLoopParams = device.GetClosedLoopParameters();
                closedLoopParams.RefSpeed = 10000000; // velocity is set in nm/s
                closedLoopParams.Acceleration = 10000000; // acceleration is set in nm/s^2
                device.SetClosedLoopParameters(closedLoopParams);

                try
                {
                    // Move the stage
                    device.MoveStart();
                    Console.WriteLine("Moving the device to {0} nm", closeLoopPosition);
                    
                    // Monitor the position
                    int posCheckCnt = 0, newPos = 0;
                    for(int i = 0; i < 100; i++)
                    {
                        newPos = device.GetCurrentPosition();
                        if (Math.Abs(closeLoopPosition - newPos) < 6000)
                            if (posCheckCnt > 3)
                                break;
                            else
                            {
                                Thread.Sleep(200);
                                posCheckCnt++;
                            }
                        else 
                            Thread.Sleep(200);
                    }

                    // Print the current position
                    Console.WriteLine("Device moved to {0} nm", newPos);
                }
                catch (Exception)
                {
                    Console.WriteLine("Fail to move to the position");
                }
            }

            // Tidy up and exit
            device.StopPolling();
            device.Disconnect(true);
            Console.WriteLine("Program finished");

            // Uncomment this line if you are using Simulations
            // SimulationManager.Instance.UninitializeSimulations();
            Console.ReadKey();
        }
    }
}
