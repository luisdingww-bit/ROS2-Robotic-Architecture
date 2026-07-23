"""Generate a preview image of the planner's toolpath (layer 1).

Run:  python examples/preview_toolpath.py
Output: docs/sample_toolpath.png

Reproduces the same 50x50 mm square used by `src/toolpath_planner.py`'s
`__main__`, just for visualization. matplotlib is the only extra dep.
"""
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from toolpath_planner import ToolpathPlanner  # noqa: E402


def main():
    planner = ToolpathPlanner()
    boundary = [(0.0, 0.0), (50.0, 0.0), (50.0, 50.0), (0.0, 50.0)]
    layer = planner.slice_layer(2.0, boundary)  # layer 1

    xs = [p.x for p in layer]
    ys = [p.y for p in layer]
    n = len(boundary)

    fig, ax = plt.subplots(figsize=(6, 6))
    # contour (first n points) + closure back to start
    ax.plot(xs[:n] + [xs[0]], ys[:n] + [ys[0]], "b-", lw=2, label="contour")
    # infill points: MOVE = travel (light), PRINT = extrusion (dark)
    for i in range(n + 1, len(layer)):
        p = layer[i]
        if p.command == "MOVE":
            ax.plot(p.x, p.y, "o", color="lightgray", ms=4)
        else:
            ax.plot(p.x, p.y, "s", color="darkred", ms=4)
    ax.set_aspect("equal")
    ax.set_title("Toolpath preview — layer 1 (50x50 mm square, zigzag infill)")
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)

    out = os.path.join(os.path.dirname(__file__), "..", "docs", "sample_toolpath.png")
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
