# onboard-ai-jetson
Implement machine learning models on Jetson Xavier NX Developer Kit

## Hardware
1. Nvidia Jetson Xavier NX
2. TBD

## Software Setup
1. Use NVIDIA SDK Manager to flash Jetson with Ubuntu OS (Follow instructions in [Jetson Xavier NX Developer Kit User Guide](https://developer.nvidia.com/jetson-xavier-nx-developer-kit-user-guide) at [Jetson Download Center](https://developer.nvidia.com/embedded/downloads#?search=Developer%20Kit%20User%20Guide).
2. Update Ubuntu followed by installing 'pip' and 'jetson-stats' modules

```shell
sudo apt-get update
sudo apt upgrade
sudo apt-get install python3-pip
sudo -H pip3 install -U jetson-stats
sudo jtop # run jetson-stats as a standalone application to assess system performance
```
jetson-stats may also be integrated with the software as below
```shell
from jtop import jtop
with jtop() as jetson:
    # jetson.ok() will provide the proper update frequency
    while jetson.ok():
        # Read tegra stats
        print(jetson.stats)
```
Check cameras
```shell
cheese #check webcam
gst-launch-1.0 nvarguscamerasrc ! nvoverlaysink #Take signal from raspberry pi camera and overlay over the screen
```

3. Install Curl and VS Code
```shell
sudo apt-get update
sudo apt-get install curl
curl -L https://github.com/toolboc/vscode/releases/download/1.32.3/code-oss_1.32.3-arm64.deb -o code-oss_1.32.3-arm64.deb
sudo dpkg -i code-oss_1.32.3-arm64.deb
```
4. Install opencv, numpy, and dependencies
```shell
sudo apt-get update
# sudo apt-get install -y cmake git pkg-config #install if required
sudo apt-get install -y build-essential libgtk2.0-dev libavformat-dev libswscale-dev
# sudo apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
# sudo apt-get install -y python3.8-dev python-dev python-numpy python3-numpy
# sudo apt-get install -y libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev
sudo apt-get install -y libv4l-dev v4l-utils qv4l2 v4l2ucp
sudo apt-get install -y curl

mkdir folder
cd folder
curl -L https://github.com/opencv/opencv/archive/4.6.0.zip -o opencv-4.6.0.zip
curl -L https://github.com/opencv/opencv_contrib/archive/4.6.0.zip -o opencv_contrib-4.6.0.zip

unzip opencv-4.6.0.zip
unzip opencv_contrib-4.6.0.zip
rm opencv-4.6.0.zip opencv_contrib-4.6.0.zip
cd opencv-4.6.0/
```

   
