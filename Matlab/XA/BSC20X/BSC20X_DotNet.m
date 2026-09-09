% Title: BSC20X
% Modification Date: 09/09/2026
% Example Description:
% This example demonstrates how to connect to a BSC20X device and channel,
% home it, and perform an absolute move of 5 mm.

% Load the XA dll
NET.addAssembly('C:\Program Files\Thorlabs XA\SDK\.NET Framework (C#)\Libraries\x64\tlmc_xa_dotnet.dll');

import Thorlabs.MotionControl.XA.*
import Thorlabs.MotionControl.XA.Products.*

% Change this line to match the serial number on your device.
deviceId = '1234';
% Select the channel to control ("1", "2", or "3").
channelNumber = '1';

% Start up XA.
systemManager = SystemManager.Create();
systemManager.Startup();

% Get the device list.
devicelist = systemManager.GetDeviceList();
if isempty(devicelist)
    fprintf('Connected devices: %d\n', 0);
else
    fprintf('Connected devices: %d\n', devicelist.Count);
end
if ~isempty(devicelist) && devicelist.Count > 0
    index = 1;
    for k = 1:devicelist.Count
        d = devicelist.Item(k-1);
        fprintf('Device %d: ', index);
        try
            fprintf('%s, Serial Number: %s\n', char(d.DeviceType.ToString()), char(d.Device));
        catch
            if ~isempty(d)
                fprintf('%s\n', char(d.ToString()));
            else
                fprintf('<null device>\n');
            end
        end
        index = index + 1;
    end
else
    fprintf('No devices found.\n');
end

% Open the BSC20X base device.
[ret, device] = systemManager.TryOpenDevice(deviceId, '', OperatingModes.Default);
if ~ret
    fprintf('\nFail to open base unit %s\n', deviceId);
    systemManager.Shutdown();
    return;
end
fprintf('\nBase Unit %s opened successfully\n', deviceId);

% Open the channel.
channelId = [deviceId '-' channelNumber];
[ret, channel] = systemManager.TryOpenDevice(channelId, '', OperatingModes.Default);
if ~ret
    fprintf('Fail to open channel %s\n', channelId);
    device.Close();
    systemManager.Shutdown();
    return;
end
fprintf('Channel %s opened successfully\n', char(channel.DeviceId));

try
    % Enable the channel.
    channel.SetEnableState(EnableState.Enabled, System.TimeSpan.FromSeconds(60));
    fprintf('Channel enabled successfully.\n');

    % Get hardware info.
    hardwareInfo = channel.GetHardwareInfo(System.TimeSpan.FromSeconds(1));
    fprintf('Channel %s Device Name: %s\n', char(channel.DeviceId), char(hardwareInfo.PartNumber));

    % Get the connected stage info.
    connectedProductInfo = channel.GetConnectedProductInfo();
    fprintf('Channel %s Stage Name: %s\n', char(channel.DeviceId), char(connectedProductInfo.ProductName));

    % Home the channel.
    fprintf('Homing...\n');
    channel.Home(System.TimeSpan.FromSeconds(60));
    fprintf('Homing successful.\n');

    % Distance to move.
    distance = 5.0;

    % Get the unit type from the connected actuator.
    deviceUnit = connectedProductInfo.UnitType;

    % Convert the physical distance to device units.
    valueInDeviceUnits = channel.FromPhysicalToDeviceUnit(ScaleType.Distance, deviceUnit, distance);
    fprintf('Conversion from %g mm successful. Value in device units: %d\n', distance, valueInDeviceUnits);

    % Absolute move to 5 mm.
    fprintf('Moving to %g %s\n', distance, char(deviceUnit.ToString()));
    channel.Move(MoveMode.Absolute, int32(valueInDeviceUnits), System.TimeSpan.FromSeconds(60));
    fprintf('Absolute move successful.\n');

    % Get the current position.
    currentPosInDeviceUnits = channel.GetPositionCounter(System.TimeSpan.FromSeconds(60));
    fprintf('New current position is: %d\n', currentPosInDeviceUnits);

    % Convert the device units back to physical units.
    currentPos = channel.FromDeviceUnitToPhysical(ScaleType.Distance, currentPosInDeviceUnits);
    fprintf('Current Position: %g %s\n', currentPos.Value, char(currentPos.UnitType.ToString()));

catch ex
    fprintf('Exception: %s\n', ex.message);
end

% Close the channel.
if ~isempty(channel)
    channel.Close();
end
% Close the device.
if ~isempty(device)
    device.Disconnect();
    device.Close();
end
fprintf('Channel closed.\n');
% Shutdown XA.
systemManager.Shutdown();
