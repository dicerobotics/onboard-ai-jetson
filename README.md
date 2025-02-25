# onboard-ai-jetson
Implement machine learning models on Jetson Xavier NX Developer Kit

## Hardware
1. Single Board Computer: [Nvidia Jetson Xavier NX Development Kit](https://amzn.to/2ZHWoJB)
2. Board: OpenCR 1.0 low level control board
3. Memory: ([SD Card](https://amzn.to/2Ktf8nT) or [M.2 NVMe SSD](https://amzn.to/3btqbYN)
4. Sensor: [Raspberry Pi Camera Module V2](https://amzn.to/31iu5Cp) with associated CSI cables (x2)
5. Sensor: [Logitech C920 WEB cam](https://amzn.to/2H4dPd0)
6. Senosr: LIDAR LDS-01 or LDS-02
7. Actuator: DYNAMIXEL (XM430-W210-T) x2
8. Remote Controller: BT-410 Set (Bluetooth 4,BLE) and RC-100B (Remote Controller)
9. Power: [Simple low-cost power adapter](https://amzn.to/3f4CLPN) or WMPS 12V5A DVE DSA-60PFE-12 12V~5A (output), A/C Cord,
10. Power: LiPo battery 11.1V 1800mAh
11. Power: LiPo Charger (Yuntong Intelligent Lithium Balance Charger) for 2S/3S Cells
12. Cables: SBC power cable, Li-Po battery extension cable, Dynamixel to OpenCR cables, USB Cable, etc.
13. Assembly: [Arducam Pan Tilt Platform for Pi Camera](https://amzn.to/2YtWCTy) (x2)
14. Chasis: [TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/).


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
gst-launch-1.0 nvarguscamerasrc ! nv3dsink   #Take a signal from PiCam and overlay over the screen
```

3. Install Curl and VS Code
```shell
sudo apt-get update
sudo apt-get install curl
curl -L https://github.com/toolboc/vscode/releases/download/1.32.3/code-oss_1.32.3-arm64.deb -o code-oss_1.32.3-arm64.deb
sudo dpkg -i code-oss_1.32.3-arm64.deb
```


   
