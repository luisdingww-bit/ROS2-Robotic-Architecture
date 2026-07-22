# ROS2-Robotic-Architecture 🤖🏗️

> Robotic fabrication and ROS2 integration for architectural construction.

---

## Overview

Exploring ROS2 (Robot Operating System 2) for robotic fabrication in architecture, including robotic arm control, path planning, and sensor integration.

---

## Repository Structure

```
ROS2-Robotic-Architecture/
├── src/        ← ROS2 packages
├── config/     ← Robot & tool configuration
├── launch/     ← Launch files
└── docs/       ← Documentation
```

---

## Hardware

- **Robotic Arm:** Universal Robots UR5 / ABB IRB 120
- **End Effector:** 3D-printed custom gripper
- **Sensors:** Intel RealSense D435, Force Torque Sensor
- **Controller:** Raspberry Pi 4 + RPLidar

---

## Capabilities

- 🔄 **Toolpath Planning** — Automated G-code generation from Rhino
- 🎯 **Pick & Place** — Material handling for assembly
- 🖨 **3D Printing** — Robotic arm extrusion printing
- 📷 **Vision** — RealSense-based object detection
- 📊 **Monitoring** — Real-time robot state visualization

---

## Getting Started

```bash
# Install ROS2 Humble
sudo apt install ros-humble-desktop

# Clone and build
colcon build
source install/setup.bash

# Launch robot control
ros2 launch robotic_architecture robot.launch.py
```

---

## License

MIT
