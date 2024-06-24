// Title: MMR601
// Created Date: 05/18/2022
// Last Modified Date: 05/18/2022
// .NET Framework version: 4.7.2
// Thorlabs DLL version: 1.14.37
// Example Description: 
// This example demonstrates how to set-up the communication for the Thorlabs 
// MMR601 modular rack controllers.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.GenericMotorCLI.Settings;
using Thorlabs.MotionControl.GenericNanoTrakCLI;
using Thorlabs.MotionControl.GenericPiezoCLI.Piezo;
using Thorlabs.MotionControl.ModularRackCLI.NanoTrak;
using Thorlabs.MotionControl.ModularRackCLI.Piezo;
using Thorlabs.MotionControl.ModularRackCLI.Rack;
using StepperMotorChannel = Thorlabs.MotionControl.ModularRackCLI.StepperMotor.StepperMotorChannel;

namespace MMR_Console_net_managed
{
    class Program
    {
        static void Main(string[] args)
        {
            // Get parameters from command line
            int argc = args.Count();
            if (argc < 1)
            {
                Console.WriteLine("Usage: MMR_Console_net_managed module_serial_number");
                Console.ReadKey();
                return;
            }

            // Get the serial number (e.g 50000123 for MST601, 51000123 for MPZ601, 52000123 for MNA601)
            string serialNo = args[0];

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

            // Get Stepper, Piezo and NanoTRAK devices, and check serial numbers correct - by using the device prefix
            // (i.e. for serial number 51000123, the device prefix is 51)
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(new List<int> { ModularRack.DevicePrefix_Stepper, ModularRack.DevicePrefix_Piezo, ModularRack.DevicePrefix_NanoTrak });
            if (!serialNumbers.Contains(serialNo))
            {
                // The requested serial number is not a valid module or is not connected
                Console.WriteLine("{0} is not a valid serial number", serialNo);
                Console.ReadKey();
                return;
            }

            // Get the device info for the bay (The rack has 6 bays - physical slots)
            StaticDeviceInfo deviceInfo = DeviceFactory.GetDeviceInfo(serialNo);
            // Create a rack device for the bay
            ModularRack rack = ModularRack.CreateModularRack((int)deviceInfo.GetTypeID(), serialNo);
            // Get the channel (NanoTrak has 1 channel, but Piezo and StepperMotor have 2)
            // just use 1st channel here
            IGenericDeviceCLI device = rack[1];

            // Open a connection to the device.
            try
            {
                Console.WriteLine("Opening device {0}", serialNo);
                rack.Connect(serialNo);
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

            // Start the device polling
            // The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
            device.StartPolling(250);
            // Needs a delay so that the current enabled state can be obtained
            Thread.Sleep(500);
            // Enable the channel otherwise any move is ignored 
            device.EnableDevice();
            // Needs a delay to give time for the device to be enabled
            Thread.Sleep(500);

            // Convert to correct device type (the parameter identifies channel number - but this is superfluous for a bay ? (TBC))
            switch (rack.BayDeviceType(1))
            {
                case ChannelDefinitions.ModularRackDevices.ModularRackPiezo:
                    {
                        PiezoChannel piezo = rack.GetPiezoChannel(1);
                        if (piezo != null)
                        {
                            // NOTE the Modular Piezo supports most of the features of the Benchtop Piezo so the code base builds on the Benchtop Piezo module
                            // and uses many classes from the Benchtop Piezo library
                            // i.e. Thorlabs.MotionControl.Benchtop.PiezoCLI.ThorlabsBenchtopPiezoSettings which uses the same settings
                            PiezoConfiguration piezoConfiguration = piezo.GetPiezoConfiguration(piezo.DeviceID, DeviceConfiguration.DeviceSettingsUseOptionType.UseConfiguredSettings);
                            Thorlabs.MotionControl.Benchtop.PiezoCLI.ThorlabsBenchtopPiezoSettings currentDeviceSettings = piezo.PiezoDeviceSettings as Thorlabs.MotionControl.Benchtop.PiezoCLI.ThorlabsBenchtopPiezoSettings;

                            // set voltage to 5v
                            Decimal voltage = 5;
                            Decimal maxVolts = piezo.GetMaxOutputVoltage();

                            // update velocity if required using real world methods
                            piezo.SetOutputVoltage(voltage);

                            Decimal newVolts = piezo.GetOutputVoltage();
                            Console.WriteLine("Voltage set to {0}", newVolts);
                        }
                    }
                    break;
                case ChannelDefinitions.ModularRackDevices.ModularRackStepperMotor:
                    {
                        StepperMotorChannel stepperMotor = rack.GetStepperChannel(1);
                        if (stepperMotor != null)
                        {
                            // NOTE the Modular Stepper Motor supports most of the features of the Benchtop Stepper Motor so the code base builds on the Benchtop Stepper Motor module
                            // and uses many classes from the Benchtop Stepper Motor library
                            // i.e. Thorlabs.MotionControl.Benchtop.StepperMotorCLI.ThorlabsBenchtopStepperMotorSettings which uses the same settings
                            MotorConfiguration motorConfiguration = stepperMotor.LoadMotorConfiguration(stepperMotor.DeviceID);
                            Thorlabs.MotionControl.Benchtop.StepperMotorCLI.ThorlabsBenchtopStepperMotorSettings currentDeviceSettings = stepperMotor.MotorDeviceSettings as Thorlabs.MotionControl.Benchtop.StepperMotorCLI.ThorlabsBenchtopStepperMotorSettings;

                            try
                            {
                                Console.WriteLine("Homing device");
                                stepperMotor.Home(60000);
                            }
                            catch (Exception)
                            {
                                Console.WriteLine("Failed to home device");
                                Console.ReadKey();
                                return;
                            }
                            Console.WriteLine("Device Homed");
                            bool homed = stepperMotor.Status.IsHomed;

                            // move to 5mm
                            decimal position = 5.0m;
                            try
                            {
                                Console.WriteLine("Moving Device to {0}", position);
                                stepperMotor.MoveTo(position, 60000);
                            }
                            catch (Exception)
                            {
                                Console.WriteLine("Failed to move to position");
                                Console.ReadKey();
                                return;
                            }
                            Console.WriteLine("Device Moved");

                            Decimal newPos = stepperMotor.Position;
                            Console.WriteLine("Device Moved to {0}", newPos);
                        }
                    }
                    break;
                case ChannelDefinitions.ModularRackDevices.ModularRackNanoTrak:
                    {
                        NanoTrakChannel nanoTrak = rack.GetNanoTrakChannel(1);
                        if (nanoTrak != null)
                        {
                            // NOTE the Modular NanoTrak supports most of the features of the Benchtop NanoTrak so the code base builds on the Benchtop NanoTrak module
                            // and uses many classes from the Benchtop NanoTrak library
                            // i.e. Thorlabs.MotionControl.Benchtop.NanoTrakCLI.ThorlabsNanoTrakSettings which uses the same settings
                            NanoTrakConfiguration nanoTrakConfiguration = nanoTrak.GetNanoTrakConfiguration(serialNo, DeviceConfiguration.DeviceSettingsUseOptionType.UseConfiguredSettings);
                            Thorlabs.MotionControl.Benchtop.NanoTrakCLI.ThorlabsNanoTrakSettings currentDeviceSettings = nanoTrak.NanoTrakDeviceSettings as Thorlabs.MotionControl.Benchtop.NanoTrakCLI.ThorlabsNanoTrakSettings;
                            nanoTrak.SetSettings(currentDeviceSettings, false);
                            //
                            // Change some parameters here
                            // ...
                            // Need to read back the updated parameters back to the settings
                            nanoTrak.GetSettings(currentDeviceSettings);

                            // Scan circle - sine/cosine output voltages result in circular positioning
                            // HomeCircle() - Move the scan circle to the defined home position
                            // HVPosition - structure containing Hor/Vert pos.
                            // TIA : Transient Impedence Amplifier - automatic range selected
                            nanoTrak.SetMode(NanoTrakStatusBase.OperatingModes.Tracking);
                            nanoTrak.SetCircleHomePosition(new HVPosition(5, 5));
                            nanoTrak.HomeCircle();
                            nanoTrak.SetTIARangeMode(TIARangeModes.AutoRangeAtSelected, TIAOddOrEven.All);

                            Thread.Sleep(500);
                            TIAReading reading = nanoTrak.GetReading();
                            Console.WriteLine("Voltage set to {0}", reading);
                        }
                    }
                    break;
            }

            device.StopPolling();
            rack.Disconnect(true);

            Console.ReadKey();
        }

    }
}
