"""Unit tests for the ROS2-Robotic-Architecture slicer (toolpath_planner.py).

Pure stdlib + pytest only — no ROS2 required, so this runs in CI.
"""
import os
import sys

import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from toolpath_planner import ToolpathPlanner  # noqa: E402


SQUARE = [(0.0, 0.0), (50.0, 0.0), (50.0, 50.0), (0.0, 50.0)]


def test_boundary_contour_matches_input():
    planner = ToolpathPlanner()
    pts = planner.slice_layer(2.0, SQUARE)
    assert len(pts) >= len(SQUARE)
    for i, (x, y) in enumerate(SQUARE):
        assert pts[i].x == x
        assert pts[i].y == y
        assert pts[i].z == 2.0


def test_boundary_closes_to_start():
    planner = ToolpathPlanner()
    pts = planner.slice_layer(2.0, SQUARE)
    # After the contour, a point returns to the first vertex.
    closure = pts[len(SQUARE)]
    assert (closure.x, closure.y) == SQUARE[0]


def test_infill_count_and_spacing():
    planner = ToolpathPlanner()
    spacing = 5.0
    pts = planner.slice_layer(2.0, SQUARE, infill_spacing=spacing)
    min_y = 0.0
    max_y = 50.0
    rows = int((max_y - min_y) // spacing) - 1  # 9 rows for a 50mm square @5mm
    # total = contour(4) + closure(1) + infill(2 points/row)
    assert len(pts) == len(SQUARE) + 1 + 2 * rows

    infill = pts[len(SQUARE) + 1 :]
    assert len(infill) == 2 * rows
    ys = [pt.y for pt in infill]
    # MOVE and PRINT of a row share the same y
    assert ys[0::2] == ys[1::2]
    # consecutive rows step by `spacing`
    for i in range(2, len(ys), 2):
        assert math.isclose(ys[i] - ys[i - 2], spacing)


def test_infill_direction_alternates():
    planner = ToolpathPlanner()
    pts = planner.slice_layer(2.0, SQUARE, infill_spacing=5.0)
    infill = pts[len(SQUARE) + 1 :]
    move_xs = [pt.x for pt in infill if pt.command == "MOVE"]
    # direction flips each row: starts at min_x, then max_x, then min_x ...
    assert move_xs[0] == 0.0
    assert move_xs[1] == 50.0
    assert move_xs[2] == 0.0


def test_export_gcode_format(tmp_path):
    planner = ToolpathPlanner()
    for z in range(1, 4):
        planner.paths.append(planner.slice_layer(z * 2.0, SQUARE))
    out = tmp_path / "sample.gcode"
    planner.export_gcode(str(out))
    text = out.read_text()
    assert "G21" in text  # mm units
    assert "G90" in text  # absolute positioning
    assert "G91" not in text  # not relative
    assert "G0" in text  # travel moves
    assert "G1" in text  # print moves
