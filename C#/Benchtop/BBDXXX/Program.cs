using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;
using Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI;
// NOTE this example is written for the Benchtop Brushless  Motor but the technique is applicable to all benchtop devices

public class Program
{
    static void Main()
    {
        // The following shows how to create a device and access a channel
        // Simply replace all references to BenchtopBrushlessMotor and BrushlessMotorChannel with
        // Equivenent references to your device type

        // Uncomment this line (and the equivalent Uninitialize statement at the end)
        // If you are using simulations.
        //SimulationManager.Instance.InitializeSimulations();

        // Serial number for Benchtop Brushless Motor (Example)
        // Change this line to match your device
        string serialNo = "73000001";

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
        List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(BenchtopBrushlessMotor.DevicePrefix73);
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
        BrushlessMotorChannel channel = device.GetChannel(1) as BrushlessMotorChannel;
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
        MotorConfiguration motorSettings = channel.LoadMotorConfiguration(serialNo);
        BrushlessMotorSettings currentDeviceSettings = channel.MotorDeviceSettings as BrushlessMotorSettings;

        // Get the device unit converter
        //motorSettings.UpdateCurrentConfiguration();
        //DeviceUnitConverter deviceUnitConverter = channel.;

        // Display info about device
        DeviceInfo di = channel.GetDeviceInfo();
        Console.WriteLine("Device {0} = {1}", di.SerialNumber, di.Name);

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
            Console.WriteLine("Device Moved to {0}({1})", newPos, position);
        }

        // The following applies to all Benchtop devices

        device.ShutDown();

        // Uncomment this line if you are using simulations
        //SimulationManager.Instance.UninitializeSimulations();

        Console.ReadKey();
    }
}
