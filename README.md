# ROS2-Robotic-Architecture 🤖🏗️

> Robotic fabrication and ROS2 integration for architectural construction.

---

## Hardware
- **Robot Arm:** Universal Robots UR5 / ABB IRB 120
- **End Effector:** Custom 3D-printed gripper
- **Sensors:** Intel RealSense D435, Force Torque Sensor
- **Controller:** Raspberry Pi 4

## Structure
```
ROS2-Robotic-Architecture/
├── src/        ← ROS2 packages
│   └── toolpath_planner.py
├── config/     ← Robot & tool config
├── launch/     ← Launch files
│   └── robot_launch.py
└── docs/       ← Documentation
```

## Capabilities
- Toolpath Planning — G-code generation from Rhino geometry
- Pick & Place — Automated material handling
- 3D Printing — Robotic arm extrusion
- Vision — RealSense-based detection
