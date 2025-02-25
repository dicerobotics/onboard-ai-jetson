# onboard-ai-jetson
This repository programs an Autonomous Mobile Robot (AMR) for educational purpose and implement on-board machine learning models using Nvidia Jetson NX Xavier to test in real-life scenarios.

Note: This project is temporarily halted because of personal commitments.

## Hardware
1. Single Board Computer: [Nvidia Jetson Xavier NX Development Kit](https://amzn.to/2ZHWoJB) or Raspberry Pi
2. Board: [OpenCR 1.0](https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_opencr1_0/) low level control board
3. Memory: SD Card or [M.2 NVMe SSD](https://amzn.to/3btqbYN)
4. Sensor: Raspberry Pi Camera Module v2.1 with associated CSI cables (x2)
5. Sensor: [Logitech C920 WEB cam](https://amzn.to/2H4dPd0)
6. Senosr: 	360 Laser Distance Sensor LDS-02 with USB2LDS interface embedded board
7. Sensor: Intel RealSense Depth Camera D435
8. Actuator: DYNAMIXEL (XM430-W210-T) for wheels (x2) 
9. Actuator: HiTec HS-645MG (x2) for camera Tilt/Pan assembly
10. Actuator: Robotis 5DoF Open Manipulator (Dynamixel XM430-W350-T, 500grams payload, 46 rpm joint speed, 0.7 kg, TTL bus)
11. Remote Controller: RC-100B + BT-410 Set (Bluetooth 4, BLE)
12. Power: [Simple low-cost power adapter](https://amzn.to/3f4CLPN) or SMPS 12V5A DVE DSA-60PFE-12 12V~5A (output), A/C Cord
13. Power: LiPo battery 11.1V 1800mAh
14. Power: LiPo Charger (Yuntong Intelligent Lithium Balance Charger) for 2S/3S Cells
15. Power: [U2D2](https://emanual.robotis.com/docs/en/parts/interface/u2d2_power_hub/) power hub board for manipulator
16. Cables: SBC power cable, Li-Po battery extension cable, Dynamixel to OpenCR cables, USB Cable, etc.
17. Assembly: Tilt Platform for Pi Camera (x2)
18. Chasis: [TurtleBot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/)

![Hardware setup](https://github.com/user-attachments/assets/052fab94-2d74-434a-89f3-c9a757cf0646)

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

## Performance

| Resource      | Availability  | Utilization   |
| ------------- | ------------- | ------------- |
| CPU-1 to CPU-6| 1.4 GHz each  | 98%           |
| Memory        | 6.7 GB        | 5.9 GB        |
| GPU           |               | 23%           |
| Disk          | 116 GB        | 17.7 GB       |
| Power Mode    | 20 W, 6-Core  |               |

Running Hardware
| Hardware                | Specs.                                                                                 |
| ----------------------- | ---------------------------------------------------------------------------------------|
| Nvidia Jetson Xavier NX | 384 CUDA Cores, 48 Tensor Cores, 3 power modes (10W-800MHz, 15W-1100MHz, 20W-1100MHz)  |
| PiCAM v2.1              | Sony IMX219 8-MP sensor, Supports 1080p30, 720p60, and VGA90.                          |
|C920 HD Pro Webcam       | 78 degree FoV, Supports 1080p30 - 720p30, USB Port-A connectivity.                     |

![image](https://github.com/user-attachments/assets/3a4b3718-9bb1-4fc7-a7be-9d7f36e76c38)


## Operational Videos
### Manipulator commanding
https://github.com/user-attachments/assets/94449342-15be-4c6c-90fd-a6d75797d7f9
### Manipulator target alignment
https://github.com/user-attachments/assets/19cf6044-ba3b-4795-8b4d-693bf015cf75
### Platform's remote operation
https://github.com/user-attachments/assets/1529cb57-b22e-4dbb-b87a-03b9ebc5477a
### Object Detection
https://github.com/user-attachments/assets/649676e5-7fa3-48b6-96f8-d21fbfeb584a
### Point cloud data acquisition
https://github.com/user-attachments/assets/52c2b7a0-fc49-47f6-b259-82c364f654a0

## Progress [Completed tasks: Phase 1 (1-6), Phase 2 (1-2), Phase 3 ()]

Phase 1:
1. Setup and run TurtleBot3 with the software provided with Robotis.
2. Jetpack Configuration with software setup.
3. Configuration and running of Webcam (over USB port) with GPU accelerated support at Nvidia Jetson using Gstreamer framework.
4. Configuration and running PiCAM v2.1 over CSI communication using Nvidia’s Multimedia API’s Gstreamer framework.
5. Installed face-recognition and identification libraries onto Jetson Xavier GPUs.
6. Implementation and testing of trained machine learning deep network on GPU – (Network has been implemented and tested on known dataset for known images).
7. Training custom dataset to recognized custom faces (will test with ASCL members) [Work in progress].

Phase 2: Use Jetson boards to work with IMU’s, Servos, etc. and explore serial interfaces (UART, SPI, etc. ) to get ready for complete robotic system
1. Connecting and controlling Dynamixel servos with OpenCR board.
2. Connecting and controlling Remote Controller with OpenCR board.
3. Connecting and controlling servos with GPIOs on Nvidia Jetson.
4. Controlling dual Pan/Tilt cameras assembly with GPIOs and CSI communication with Nvidia Jetson GPU.
5. Object detection and tracking with Camera/Server Tilt/Pan assembly.
6. Extended above configuration for multi-camera, multi-servo, multi-object-tracking configurations.
7. Installing and configuring general purpose IMU with Nvidia Jetson.
8. Implementing complete software configuration using IMU, Servos, CSI cameras, webcams to use in object detection, tracking, and following applications.

Phase 3: Update hardware and software for synchronous data readout from cameras and IMUs for better Visual Inertial Odometry (VIO) and Simultanous Localization and Mapping (SLAM) performance.
1. Design and develop hardware architecture for synchronous sensor data readout.
2. Test the performance of state-of-the-art VIO and SLAM models with synchronous data readout hardware using GPUs.
3. If performance with GPUs is not satisfactory, consider changing SBC with FPGA SoCs (possible setups may include Xilinx/AMDs Kria or Microchip's PolarFire). Conceptual diagram provided below.
![sensor_readout_synch_arch](https://github.com/user-attachments/assets/5629f56f-1537-4591-8b5b-08236a07bab4)

