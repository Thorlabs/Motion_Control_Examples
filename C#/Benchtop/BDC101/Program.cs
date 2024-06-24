// Title: BDC101
// Created Date: 02/04/2022
// Last Modified Date: 04/26/2022
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.32
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// BDC Benchtop controllers.



using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.Benchtop.DCServoCLI;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;

namespace BDC_Console_net_managed
{
    class Program
    {
        static void Main()
        { 
        

            // Optionally set the position for a single channel (in real units)
            decimal position = 0m;

            // Get the velocity
            decimal velocity = 0m;
           

            // Enter your device's serial number
            string serialNo = "79000001";

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

            // Get available BDC and check our serial number is correct - by using the device prefix
            // (i.e. for serial number 79000123, the device prefix is 79)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(BenchtopDCServo.DevicePrefix79);
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a BDC103 or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Create the device - DC Servo
            BenchtopDCServo device = BenchtopDCServo.CreateBenchtopDCServo(serialNo);
            if (device == null)
            {
                // An error occured
                Console.WriteLine("{0} is not a BenchtopDCServo", serialNo);
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

            // Get the correct channel - channel 1 for this example
            DCServoChannel channel = device.GetChannel(1);
            if (channel == null)
            {
                // Connection failed
                Console.WriteLine("Channel unavailable {0}", serialNo);
                Console.ReadKey();
                return;
            }

            // Wait for the device settings to initialize - timeout 5000ms
            if (!channel.IsSettingsInitialized())
            {
                try
                {
                    channel.WaitForSettingsInitialized(5000);
                }
                catch (Exception)
                {
                    Console.WriteLine("Settings failed to initialize");
                }
            }

            // Start the device polling
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
            channel.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored 
            channel.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Call LoadMotorConfiguration on the device to initialize the DeviceUnitConverter object required for real world unit parameters
            // - loads configuration information into channel
            // Use the channel.DeviceID "79xxxxxx-1" to get the channel 1 settings. This is different to the serial number
            MotorConfiguration motorConfiguration = channel.LoadMotorConfiguration(channel.DeviceID);

            // Not used directly in example but illustrates how to obtain device settings
            ThorlabsBenchtopDCServoSettings currentDeviceSettings = channel.MotorDeviceSettings as ThorlabsBenchtopDCServoSettings;

            // Display info about device
            DeviceInfo deviceInfo = channel.GetDeviceInfo();
            Console.WriteLine("Device {0} = {1}", deviceInfo.SerialNumber, deviceInfo.Name);

            // Home the channel
            try
            {
                Console.WriteLine("Homing device");
                channel.Home(60000);
            }
            catch (Exception)
            {
                Console.WriteLine("Failed to home device");
                Console.ReadKey();
                return;
            }
            Console.WriteLine("Device Homed");
            bool homed = channel.Status.IsHomed;

            // If a position is requested
            if (position != 0)
            {
                // Update velocity if required using real world methods - using the information obtained from configuration file
                if (velocity != 0)
                {
                    VelocityParameters velPars = channel.GetVelocityParams();
                    velPars.MaxVelocity = velocity;
                    channel.SetVelocityParams(velPars);
                }

                try
                {
                    Console.WriteLine("Moving Device to {0}", position);
                    channel.MoveTo(position, 60000);
                }
                catch (Exception)
                {
                    Console.WriteLine("Failed to move to position");
                    Console.ReadKey();
                    return;
                }
                Console.WriteLine("Device Moved");

                Decimal newPos = channel.Position;
                Console.WriteLine("Device Moved to {0}", newPos);
            }

            channel.StopPolling();
            device.Disconnect(true);

            Console.ReadKey();
        }
    }
}
