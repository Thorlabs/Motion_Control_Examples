using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.GenericMotorCLI;
using Thorlabs.MotionControl.KCube.DCServoCLI;

namespace KDC101Console
{
    class Program
    {
        static void Main(string[] args)
        {
            string serialNo = "27000423";
            // This instructs the DeviceManager to build and maintain the list of 
            // devices connected. 
            SimulationManager.Instance.InitializeSimulations();
            DeviceManagerCLI.BuildDeviceList();


            // This creates an instance of KCubeDCServo class, passing in the Serial 
            //Number parameter.  
            KCubeDCServo device = KCubeDCServo.CreateKCubeDCServo(serialNo);

            // We tell the user that we are opening connection to the device. 
            Console.WriteLine("Opening device {0}", serialNo);

            // This connects to the device. 
            device.Connect(serialNo);

            // Wait for the device settings to initialize. We ask the device to 
            // throw an exception if this takes more than 5000ms (5s) to complete. 
            device.WaitForSettingsInitialized(5000);

            // This calls LoadMotorConfiguration on the device to initialize the 
            // DeviceUnitConverter object required for real world unit parameters.
            MotorConfiguration motorSettings = device.LoadMotorConfiguration(serialNo,
            DeviceConfiguration.DeviceSettingsUseOptionType.UseFileSettings);

            // This starts polling the device at intervals of 250ms (0.25s). 

            device.StartPolling(250);

            // We are now able to Enable the device otherwise any move is ignored. 
            // You should see a physical response from your controller. 
            device.EnableDevice();
            Console.WriteLine("Device Enabled");


            // Needs a delay to give time for the device to be enabled. 
            Thread.Sleep(500);

            // Home the stage/actuator.  

            Console.WriteLine("Actuator is Homing");
            device.Home(60000);

            // Move the stage/actuator to 5mm (or degrees depending on the device 
            // connected). 
            Console.WriteLine("Actuator is Moving");
            device.MoveTo(5, 60000);

            //Stop polling device
            device.StopPolling();

            // Shut down controller using Disconnect() to close comms
            // Then the used library
            device.ShutDown();
            SimulationManager.Instance.InitializeSimulations();
            Console.WriteLine("Complete. Press any key to exit");
            Console.ReadKey();

        }
    }
}
