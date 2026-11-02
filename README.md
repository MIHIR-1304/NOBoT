# 🤖 NOBoT — AI-Integrated Autonomous Quadruped Robot

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8%20Edge%20AI-00FFFF?logo=ultralytics&logoColor=black)](https://ultralytics.com/)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-5-C51A4A?logo=raspberrypi&logoColor=white)](https://www.raspberrypi.com/)
[![Arduino](https://img.shields.io/badge/Arduino-Dual%20MCU-00979D?logo=arduino&logoColor=white)](https://www.arduino.cc/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

**NOBoT** is an autonomous AI-driven quadruped spider robot built for navigation in hazardous terrains and search-and-rescue environments. Designed with a dual-microcontroller orchestration architecture combining a **Raspberry Pi 5** for edge computer vision and deep learning inference with an **Arduino** for real-time 3-DOF inverse kinematics locomotion gait execution.

---

## 🌟 Key Architecture & Highlights

- **Edge AI Vision Pipeline**: Real-time object and hazard detection utilizing **YOLOv8** and **OpenCV** with bounding box tracking at 30+ FPS on edge hardware.
- **Dual-Microcontroller Architecture**: Decoupled control where the Raspberry Pi 5 runs neural models and telemetry streaming, while the Arduino handles sub-millisecond servo PWM pulse generation.
- **3-DOF Quadruped Inverse Kinematics**: Trigonometric coordinate mapping (Coxa, Femur, Tibia) calculating joint angles for dynamic gaits (Trot, Wave, Crawl).
- **Sensor Fusion & Hazard Avoidance**: Integration of 6-axis MPU6050 IMU gyro stabilization with ultrasonic distance radar for real-time terrain compensation.
- **Live Telemetry & Wireless HUD**: Bidirectional video telemetry stream and cockpit control interface.

---

## 🦾 Hardware Architecture

```
[ Raspberry Pi 5: Edge Compute ] ─── USB / CSI Camera (Live Video)
        │
        ├── YOLOv8 / OpenCV Inference
        ├── Fast video telemetry stream
        │
        ▼ (UART Serial Packet Protocol)
[ Arduino Controller: Real-Time MCU ]
        │
        ├── MPU6050 6-Axis Gyro / Accelerometer
        ├── HC-SR04 Ultrasonic Distance Sensor
        └── I2C Bus ──► [ PCA9685 16-Channel 12-Bit PWM Driver ]
                                │
                                └──► 12x MG996R / SG90 Metal Gear Servos
                                      (3 Servos per Leg × 4 Legs)
```

---

## 📐 Inverse Kinematics (3-DOF Leg Geometry)

For each leg with segment lengths $L_1$ (Coxa), $L_2$ (Femur), and $L_3$ (Tibia), the target foot tip position $(X, Y, Z)$ translates to joint angles $(\theta_1, \theta_2, \theta_3)$:

$$\theta_1 = \arctan2(Y, X)$$

$$R = \sqrt{X^2 + Y^2} - L_1, \quad D = \sqrt{R^2 + Z^2}$$

$$\theta_3 = \arccos\left(\frac{L_2^2 + L_3^2 - D^2}{2 \cdot L_2 \cdot L_3}\right)$$

$$\theta_2 = \arctan2(Z, R) + \arccos\left(\frac{L_2^2 + D^2 - L_3^2}{2 \cdot L_2 \cdot D}\right)$$

---

## 🚀 Quickstart

```bash
# Clone the repository
git clone https://github.com/MIHIR-1304/NOBoT.git
cd NOBoT

# Install Python dependencies
pip install -r requirements.txt

# Run Edge AI Vision & Telemetry Server
python telemetry/stream_server.py
```

---

## 👨‍💻 Author

**Mihir Mahato**  
Software Developer | B.Tech CSE 2026  
GitHub: [@MIHIR-1304](https://github.com/MIHIR-1304)  
LinkedIn: [Mihir Mahato](https://www.linkedin.com/in/mihir-mahato-btech)  
Email: mihirmahato1304@gmail.com
