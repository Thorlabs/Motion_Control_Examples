% Title: KDC101 Native C
% Modification Date: 08/24/2026
% Example Description:
% This example demonstrates how to set-up the communication for the Thorlabs
% KDC101 controllers, home it, and move it by 1 mm or degrees.

% Set these to your XA native DLL and this header
dllPath    = 'C:\Program Files\Thorlabs XA\SDK\Native (C, C++)\Libraries\x64\tlmc_xa_native.dll';
headerPath = 'C:\Program Files\Thorlabs XA\SDK\Native (C, C++)\tlmc_xa_native_api.h';
lib = 'tlmc_xa_native';

TLMC_Success               = 0;
TLMC_OperatingMode_Default = 256;   % 0x100 (Apt)
TLMC_Enabled               = 1;
TLMC_ScaleType_Distance    = 1;
TLMC_MoveMode_Relative     = 2;

% Change this line to match the serial number on your device
serialNo = '27268055';

if ~libisloaded(lib)
    loadlibrary(dllPath, headerPath);
end

% Start up
if calllib(lib, 'TLMC_Startup', []) ~= TLMC_Success
    fprintf('SDK Startup failed.\n');
    unloadlibrary(lib); return;
end

% Open the device
pHandle = libpointer('uint32Ptr', 0);
if calllib(lib, 'TLMC_Open', serialNo, [], TLMC_OperatingMode_Default, pHandle) ~= TLMC_Success
    fprintf('Failed to open device %s\n', serialNo);
    clear pHandle; calllib(lib, 'TLMC_Shutdown'); unloadlibrary(lib); return;
end
hDevice = pHandle.Value;
fprintf('Device %s opened successfully\n', serialNo);

try
    % Enable the device
    check(calllib(lib, 'TLMC_SetEnableState', hDevice, TLMC_Enabled, 1000));

    % Get the hardware information
    hwInfo = libstruct('TLMC_HardwareInfo');
    check(calllib(lib, 'TLMC_GetHardwareInfo', hDevice, hwInfo, 1000));
    name = char(double(hwInfo.partNumber(:)'));
    EndLineChar = find(name == 0, 1);
    if ~isempty(EndLineChar)
        name = name(1:EndLineChar-1);
    end
    name = strtrim(name);
    if ~isempty(name)
        fprintf('Device Name: %s\n', name);
    end
    
    % Home the device
    fprintf('Homing\n');
    check(calllib(lib, 'TLMC_Home', hDevice, 60000));
    fprintf('Homing completed\n');

    % Set the distance. Unit: millimeters or degrees depending on the actuator
    distance = 1;

    % Get the actuator's unit
    pPhys0 = libpointer('doublePtr', 0);
    pUnit0 = libpointer('uint16Ptr', 0);
    check(calllib(lib, 'TLMC_ConvertFromDeviceToPhysical', hDevice, ...
        TLMC_ScaleType_Distance, int64(0), pPhys0, pUnit0));
    deviceUnit = pUnit0.Value;

    % Distance to device units 
    pValue = libpointer('int64Ptr', 0);
    check(calllib(lib, 'TLMC_ConvertFromPhysicalToDevice', hDevice, ...
        TLMC_ScaleType_Distance, deviceUnit, distance, pValue));

    % Move the device
    fprintf('Moving to %g %s\n', distance, unitName(deviceUnit));
    check(calllib(lib, 'TLMC_Move', hDevice, TLMC_MoveMode_Relative, int32(pValue.Value), 60000));
    efprintf('Moving completed\n');

    % Get the current position
    pPos = libpointer('int32Ptr', 0);
    check(calllib(lib, 'TLMC_GetPositionCounter', hDevice, pPos, 1000));

    % Device units back to distance
    pPhysical = libpointer('doublePtr', 0);
    pUnit     = libpointer('uint16Ptr', 0);
    check(calllib(lib, 'TLMC_ConvertFromDeviceToPhysical', hDevice, ...
        TLMC_ScaleType_Distance, int64(pPos.Value), pPhysical, pUnit));
    fprintf('Current Position: %g %s\n', pPhysical.Value, unitName(pUnit.Value));

catch ex
    fprintf('Exception: %s\n', ex.message);
end

% Close shut down release object references so we can unload
calllib(lib, 'TLMC_Close', hDevice);
calllib(lib, 'TLMC_Shutdown');
clear pHandle hwInfo pPhys0 pUnit0 pValue pPos pPhysical pUnit
unloadlibrary(lib);

function check(rc)
    if rc ~= 0
        error('TLMC call failed with result code %d', double(rc));
    end
end


function s = unitName(code)
    switch double(code)
        case 1, s = 'Millimetres';
        case 2, s = 'Degrees';
        case 3, s = 'Radians';
        otherwise, s = sprintf('unit %d', double(code));
    end
end
