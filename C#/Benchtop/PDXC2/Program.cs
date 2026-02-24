// Title: PDXC2
// Created Date: 01/26/2024
// Last Modified Date: 11/17/2025
// .NET Framework version: 4.8.2
// Thorlabs DLL version: 1.14.56
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// PDXC2 Benchtop controllers.



using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Thorlabs.MotionControl.Benchtop.PiezoCLI;
using Thorlabs.MotionControl.Benchtop.PiezoCLI.PDXC2;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericPiezoCLI;

namespace PDXC2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Uncomment this line (and SimulationManager.Instance.UninitializeSimulations() at the end on Main)
            // If you are using a simulated device
            //SimulationManager.Instance.InitializeSimulations();

            // Enter the serial number for your device
            string serialNo = "112000001";

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

            // Get available PDXC2 and check out serial number is correct - by using the device prefix
            // (i.e. for serial number 112000123, the device prefix is 112)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(InertiaStageController.DevicePrefix_PDXC2);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a PDXC2 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device - PDXC2
            InertiaStageController device = InertiaStageController.CreateInertiaStageController(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a PDXC2", serialNo);
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
            // Enable the channel otherwise any move is ignored 
            device.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Call GetPDXC2Configuration on the device to initialize the settings
            PDXC2Configuration pdxc2Configuration = device.GetPDXC2Configuration(serialNo, DeviceConfiguration.DeviceSettingsUseOptionType.UseDeviceSettings);
            PDXC2Settings currentDeviceSettings = PDXC2Settings.GetSettings(pdxc2Configuration);
            device.SetSettings(currentDeviceSettings, true, true);

            //Optionally set the deivce to Open Loop Mode and move the stage to target position (position is set in "steps")
            int openLoopPosition = 0;
            if (openLoopPosition != 0)
            {
                // Set the open loop move paramaters for the PDXC2
                device.SetPositionControlMode(Thorlabs.MotionControl.GenericPiezoCLI.Piezo.PiezoControlModeTypes.OpenLoop);
                OpenLoopMoveParams openLoopParams = new OpenLoopMoveParams{StepSize = openLoopPosition };
                device.SetOpenLoopMoveParameters(openLoopParams);

                try
                {
                    // Move the stage
                    device.MoveStart();
                    Console.WriteLine("Moving the device to {0}.",openLoopPosition);

                    // Wait until the device reaches the target position
                    int newPos = device.GetCurrentPosition();
                    while (openLoopPosition != newPos)
                    {
                        newPos = device.GetCurrentPosition();
                        Thread.Sleep(200);
                    }

                    // Display current position
                    Console.WriteLine("Device Moved to {0}", newPos);
                }
                catch(Exception) 
                {
                    Console.WriteLine("Fail to move to the position.");
                }
            }

            //Optionally set the deivce to Closed Loop Mode and move the stage to target position
            //Close loop mode is only valid for PDX series stages with encoder
            //For linear stages, the position is in nm
            //For rotational stages, 360 degrees corresponds to 14400000 encoder counts
            int closeLoopPosition = 0;
            if (closeLoopPosition != 0)
            {
                // Set the closed loop move paramaters for the PDXC2
                device.SetPositionControlMode(Thorlabs.MotionControl.GenericPiezoCLI.Piezo.PiezoControlModeTypes.CloseLoop);

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

                // Set the target position
                device.SetClosedLoopTarget(closeLoopPosition);

                // Get and Set the velocity and acceleration
                // For linear stages, the unit is in nm/s and nm/s^2
                // For rotational stages, 360 degrees corresponds to 14400000 EnCnt. For example, 30 degrees/s = 1200000 EnCnt/s
                ClosedLoopParams closedLoopParams = device.GetClosedLoopParameters();
                closedLoopParams.RefSpeed = 1200000; 
                closedLoopParams.Acceleration = 10000000; 
                device.SetClosedLoopParameters(closedLoopParams);

                try
                {
                    // Move the stage
                    device.MoveStart();
                    Console.WriteLine("Moving the device to {0}", closeLoopPosition);

                    // Wait until the device reaches the target position
                    int posCheckCnt = 0, newPos = 0;
                    for (int i = 0; i < 200; i++)
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

                    // Display the current position
                    Console.WriteLine("Device moved to {0}", newPos);
                }
                catch (Exception)
                {
                    Console.WriteLine("Fail to move to the position");
                }
            }

            // Tidy up and exit
            device.StopPolling();
            device.Disconnect(true);
            Console.WriteLine("Program finishes");

            // Uncomment this line if you are using Simulations
            //SimulationManager.Instance.UninitializeSimulations();

            Console.ReadKey();
        }
    }
}
