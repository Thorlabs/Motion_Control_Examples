%%
%Title: ELL14.m
%Date of Creation(YYYY-MM-DD): 2024-02-08
%Date of Last Modification on Github: 2024-02-08
%Version of Matlab used for Testing: R2023b
%Version of the Thorlabs SDK used: ELLO 1.5.0
%Example Description


%% 

% Add assembly
ELLO = NET.addAssembly('C:\Program Files\Thorlabs\Elliptec\Thorlabs.Elliptec.ELLO_DLL.dll');

% Connect to the correct COM port (using ELLO is the easiest way)
Thorlabs.Elliptec.ELLO_DLL.ELLDevicePort.Connect("COM5");

% Addresses to scan between
min_address = char("0");
max_address = char("F");

ellDevices = Thorlabs.Elliptec.ELLO_DLL.ELLDevices();
devices = ellDevices.ScanAddresses(min_address, max_address);

for device_ind = devices.Count()
    device = devices.Item(device_ind-1);
    ellDevices.Configure(device);
    device_ID = char(device);
    address = ellDevices.AddressedDevice(device_ID(1));
    fprintf(string(address.DeviceInfo.DeviceType) + " connected on address: " + string(address.DeviceInfo.Address) + ".\n")

    direction_enum_handle = ELLO.AssemblyHandle.GetType('Thorlabs.Elliptec.ELLO_DLL.ELLBaseDevice+DeviceDirection');
    direction_enum = direction_enum_handle.GetEnumValues();
    fprintf("Homing...\n")
    address.Home(direction_enum(1));
    pause(3);

    address.SetJogstepSize(100);
    
    fprintf("Jogging...\n")
    address.JogForward();
    pause(1);
    address.JogBackward();
    pause(1);

end
fprintf("Disconnecting.\n")
Thorlabs.Elliptec.ELLO_DLL.ELLDevicePort.Disconnect();