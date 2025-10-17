
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

