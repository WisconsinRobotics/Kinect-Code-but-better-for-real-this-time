
# Kinect-Code-but-better-for-real-this-time
# May need to run the bypass policy below if .\Scripts\Activate.ps1 doesn't work
# Try Ethan's branch if main don't work

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


Install Kinect SDK Driver
windows sdk 2.0 kinect

Also, The site package woraround, make sure it is actually running.
(The site packages was in the python36 file path not in the one insisde the virtual environment) (Only happen for Nico)

Nico: I had to download this:
Download and install the latest Microsoft Visual C++ Redistributable here (choose the x64 version unless you're on 32-bit Python):
👉 https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist

# Typical Installation (This has worked out of box in 2 new laptops):
- install python 3.6.8
- run pip install -r requirements.txt (may have to add python_path -m if 3.6.8 is not the default python installation)
- download the files in this path: https://github.com/Kinect/PyKinect2/tree/master/pykinect2
- go to python_path/Lib/site-packages/pykinect2 and overwrite the files with files just downloaded (you might have to also delete the __pycache__ folder if any)
- run the "Kinect Multi Display.py" file
- MAGIC
