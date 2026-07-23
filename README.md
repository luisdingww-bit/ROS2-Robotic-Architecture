# ROS2-Robotic-Architecture

Toolpath planning and G-code generation for robotic / 3D-printing fabrication of architectural components.

> ⚠️ **Status: standalone Python tool (partial).** The slicer + G-code exporter work. Full ROS2 integration is planned but not yet wired up.

## What's implemented

- **`toolpath_planner.py`**
  - `slice_layer()` — generates a boundary contour + **zigzag infill** with configurable spacing.
  - `export_gcode()` — writes valid G-code (`G0` / `G1`, absolute positioning, mm units).
  - Pure Python, no external dependencies.

## Honest notes

- **No ROS2 stack is present yet.** The code is framework-agnostic Python; it does **not** import `rclpy` or launch any nodes.
- `launch/robot_launch.py` is a **template** referencing packages (`ur_robot_driver`, `robotic_fabrication`, `realsense_ros`) that are not included here.
- Pick-and-place and vision-guided routines described in the old README are **not implemented**.

## Roadmap

- Wrap the planner as a ROS2 node (`rclpy`) with an action-server interface.
- UR5 trajectory execution + RealSense surface scanning.

## Run

```bash
python toolpath_planner.py   # generates layer paths + exports sample G-code
```

## License

MIT
