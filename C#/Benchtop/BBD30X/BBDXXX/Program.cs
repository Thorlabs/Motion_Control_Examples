// Title: BBDXXX
// Created Date: 04/19/2024
// Last Modified Date: 02/06/2025
// .NET Framework version: 4.8.2
// Thorlabs DLL version: 1.14.50
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// BBD Benchtop controllers and setting triggers.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.DeviceManagerCLI.ControlParameters;
// NOTE this example is written for the Benchtop Brushless  Motor but the technique is applicable to all benchtop devices

public class Program
{
    static void Main()
    {
        // Uncomment this line (and the equivalent Uninitialize statement at the end)
        // If you are using simulations.
        // SimulationManager.Instance.InitializeSimulations();

        // Serial number for Benchtop Brushless Motor (Example)
        // Change this line to match your device
        string serialNo = "103000001";

        try
        {
            // Build device list
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

        // Get channel 1
        Brushless30XMotorChannel channel = device.GetChannel(1) as Brushless30XMotorChannel;
        if (channel == null)
        {
            Console.WriteLine("channel 1 is not a BenchtopBrushlessMotor");
            Console.ReadKey();
            return;
        }

        // Wait for settings to initialize
        channel.WaitForSettingsInitialized(5000);
        if (!channel.IsSettingsInitialized())
        {
            Console.WriteLine("Settings failed to initialize");
        }

        // The following shows how to access the settings for a Brushless Motor
        // Replace the references to MotorConfiguration and BrushlessMotorSettings with the class appropriate for your device

        // Call LoadMotorConfiguration on the device to initialize the DeviceUnitConverter object required for real unit parameters
        MotorConfiguration motorSettings = channel.LoadMotorConfiguration(channel.DeviceID);
        MotorDeviceSettings currentDeviceSettings = channel.MotorDeviceSettings;

        // Get the device unit converter
        motorSettings.UpdateCurrentConfiguration();

        channel.SetSettings(currentDeviceSettings, false); // false won't persist settings to device

        // Display info about device
        Console.WriteLine("Device {0} = {1}", channel.SerialNo, channel.DeviceName);

        // Start the device polling
        // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
        channel.StartPolling(250);
        // Needs a delay so that the current enabled state can be obtained
        Thread.Sleep(500);
        // Enable the channel otherwise any move is ignored 
        channel.EnableDevice();
        // Needs a delay to give time for the device to be enabled
        Thread.Sleep(500);

        // The following shows how to control a motor it only applies to motors
        try
        {
            Action<UInt64> workDone = channel.InitializeWaitHandler();
            channel.Home(workDone);
            channel.Wait(60000);
        }
        catch (DeviceException ex)
        {
            Console.WriteLine("Failed to home");
            Console.ReadKey();
            return;
        }

        // Get and Set Triggers
        TriggerIOConfigParameters trigIOParams = channel.GetTriggerIOConfigParameters();
        trigIOParams.TriggerOutMode = TriggerOutModeType.TrigOutput_AtPositionFwd;
        trigIOParams.StartPositionFwd = 0.0m; // 0mm start
        trigIOParams.IntervalFwd = 0.1m; // 0.1mm intervals

        channel.SetTriggerIOConfigParams(trigIOParams);
        Thread.Sleep(200);

        int position = 50;
        int velocity = 10;

        // If position is set
        if (position != 0)
        {
            // Update velocity if required using real world methods
            if (velocity != 0)
            {
                VelocityParameters velPars = channel.GetVelocityParams();
                velPars.MaxVelocity = velocity;
                channel.SetVelocityParams(velPars);
            }

            try
            {
                Action<UInt64> workDone = channel.InitializeWaitHandler();
                channel.MoveTo(position, workDone);
                channel.Wait(60000);
            }
            catch (DeviceException ex)
            {
                Console.WriteLine("Failed to set position");
                Console.ReadKey();
                return;
            }

            Decimal newPos = channel.Position;
            Console.WriteLine("Device Moved to {0}", newPos);
        }

        // Close the channel and the device
        channel.StopPolling();
        channel.DisableDevice();
        device.Disconnect(false);

        // Uncomment this line if you are using simulations
        //SimulationManager.Instance.UninitializeSimulations();

        Console.ReadKey();
    }
}
