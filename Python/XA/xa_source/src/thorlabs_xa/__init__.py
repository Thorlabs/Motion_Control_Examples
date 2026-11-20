#from thorlabs_xa.native_sdks.c_native_functions import CNativeFunctions

# This ensures that the native DLL is loaded from the thorlabs_xa folder, which is compatible with circumstances where
# the python SDK is installed as a package via PIP. Note this script is automatically executed by the interpreter
# when this, or child packages, are imported by a script. It is only executed once over the lifetime of a script.
#CNativeFunctions.try_load_library(__file__)