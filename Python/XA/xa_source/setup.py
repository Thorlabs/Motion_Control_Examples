from setuptools import setup, find_packages, Distribution
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
import platform
import shutil
import os
from pathlib import Path

# Open the readme content for including as the long description of the package
with open("ReadMe.md", "r") as file:
    read_me_content = file.read()

# The wheel is NOT pure python (contains native files).
class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True
    def is_pure(self):
        return False

# Force tags py3-none-<plat>. This is specifically OK in our case, because we don't have any
# CPython dependent Python extensions being shipped with the package, just our native library
class bdist_wheel(_bdist_wheel):
    def get_tag(self):
        _, _, plat = super().get_tag()
        return "py3", "none", plat

included_native_library = ""

if platform.system() == "Windows":
    included_native_library = "tlmc_xa_native.dll"
elif platform.system() == "Linux":
    included_native_library = "libtlmc_xa_native.so"
else:
    print("ERROR: Current system operating system not recognised for Python SDK package.")
    exit -1

# Read the version from the VERSION file
sdk_version = ""

version_file = Path("VERSION")

with open("VERSION", "r") as versionfile:
    sdk_version = versionfile.readline().strip()

print ("Building for {} {}.".format(platform.system(), platform.machine()))

setup(
    name="thorlabs_xa",
    version = sdk_version,
    include_package_data=True,
    author = "Thorlabs",
    author_email = "techsupport@thorlabs.com",
    description = "Thorlabs XA Python SDK",
    project_urls={
        "Changelog": "https://github.com/Thorlabs/Motion_Control_Examples/blob/main/Python/XA/CHANGELOG.md"
    },
    long_description = read_me_content,
    long_description_content_type="text/markdown",
    package_data={"thorlabs_xa": [included_native_library]},
    package_dir={"": "src"},
    distclass=BinaryDistribution,
    cmdclass={"bdist_wheel": bdist_wheel},
    license="BSD-3-Clause",
    license_files=["LICENSE"],
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='>=3.10, <4',
    install_requires=[],
)
