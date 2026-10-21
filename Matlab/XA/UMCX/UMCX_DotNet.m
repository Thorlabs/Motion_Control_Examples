% Title: UMCX
% Modification Date: 09/09/2026
% Example Description:
% This example demonstrates how to set-up the communication for the Thorlabs
% UMCX controllers with a brushless stage, home it, and move it by 1 mm or degrees.

% Load the XA dll
NET.addAssembly('C:\Program Files\Thorlabs XA\SDK\.NET Framework (C#)\Libraries\x64\tlmc_xa_dotnet.dll');

import Thorlabs.MotionControl.XA.*
import Thorlabs.MotionControl.XA.Products.*

% Change this line to match the serial number on your device (format: 121XXXXXX)
deviceId = '121000020';
% Select the channel to control ("1", "2", or "3")
channelNumber = '1';

% Start up XA
systemManager = SystemManager.Create();
systemManager.Startup();

% Get the device list
devicelist = systemManager.GetDeviceList();

% Print all connected devices
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

% Open the UMCx device
[ret, device] = systemManager.TryOpenDevice(deviceId, '', OperatingModes.Default);
if ~ret
    fprintf('\nFail to open base unit %s\n', deviceId);
    systemManager.Shutdown();
    return;
end
fprintf('\nBase Unit %s opened successfully\n', deviceId);

% Open the channel
channelId = [deviceId '-' channelNumber];
[ret, channel] = systemManager.TryOpenDevice(channelId, '', OperatingModes.Default);
if ~ret
    fprintf('Fail to open channel %s\n', char(channel.DeviceId));
    systemManager.Shutdown();
    return;
end
fprintf('Channel %s opened successfully\n', char(channel.DeviceId));

try
    % Enable the device
    channel.SetEnableState(EnableState.Enabled, System.TimeSpan.FromSeconds(1));

    % Get the stage information
    connectedProductInfo = channel.GetConnectedProductInfo();
    fprintf('Channel %s Stage Name:%s\n', char(channel.DeviceId), char(connectedProductInfo.ProductName));

    % Home the device
    fprintf('Homing\n');
    channel.Home(System.TimeSpan.FromSeconds(60));
    fprintf('Home completed\n');

    % Set the distance. Unit: millimeters or degrees depending on the actuator
    distance = 1;

    % Get the unit type of the actuator
    deviceUnit = connectedProductInfo.UnitType;

    % Convert the distance to device unit
    posInDeviceUnits = channel.FromPhysicalToDeviceUnit(ScaleType.Distance, deviceUnit, distance);
    System.Threading.Thread.Sleep(500);

    % Move the device
    fprintf('Moving to %g %s\n', distance, char(deviceUnit.ToString()));
    channel.Move(MoveMode.Absolute, int32(posInDeviceUnits), System.TimeSpan.FromSeconds(60));
    fprintf('Move completed\n');

    % Get the current position
    currentPosInDeviceUnits = channel.GetPositionCounter(System.TimeSpan.FromSeconds(1));

    % Convert the device unit to physical unit
    currentPos = channel.FromDeviceUnitToPhysical(ScaleType.Distance, currentPosInDeviceUnits);
    fprintf('Current Position: %g %s\n', currentPos.Value, char(currentPos.UnitType.ToString()));

catch ex
    fprintf('Exception: %s\n', ex.message);
end

% Close the channel
if ~isempty(channel)
    channel.Close();
end
% Close the device
if ~isempty(device)
    device.Disconnect();
    device.Close();
end
% Shutdown XA
systemManager.Shutdown();
