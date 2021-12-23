# KDC101 C\# Programming Guide

This guide will attempt to guide you through the process of setting up a project in visual studio, adding references to the necessary libraries, and using the example provided.

### Prerequisites

  - Microsoft Visual Studio
  - Thorlabs Kinesis
  - A KDC101 Controller
  - A connected instrument
    * e.g. a DDR25/M

## Creating Your Project

Open Visual Studio, and select "Create new project..." from the opening screen. In the resulting "New Project" Window, select "Console App (.NET Framework) from the Visual C# section, choose an appropriate name and location for your project (e.g. KDC101_Console) and press ok. This will create a new folder with your project name

Next, open file explorer and navigate to your Kinesis installation folder ("C:\Program Files\Thorlabs\Kinesis" for 64-bit installations or "C:\Program Files (x86)\Thorlabs\Kinesis" for 32-bit installations). Within this folder is a program named "Thorlabs.MotionControl.Kinesis.DLLutility.exe", which can be used to copy the libraries you need into your project folders Bin\\Debug folder. Alternatively, you can manually copy and paste the files.
