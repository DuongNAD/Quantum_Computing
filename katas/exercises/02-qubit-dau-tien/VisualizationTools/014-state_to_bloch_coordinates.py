# ══════════════════════════════════════════════════════════════════════════════
# BÀI 014/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/VisualizationTools/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/VisualizationTools/1
#   Gợi ý:      python qk.py hint tutorials/VisualizationTools/1
#   Lời giải:   python qk.py solution tutorials/VisualizationTools/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 1: Bloch Sphere Coordinates
# Goal: Convert a qubit state to Bloch sphere coordinates.
#       For state α|0⟩ + β|1⟩, calculate the (x,y,z) coordinates on the Bloch sphere.

import numpy as np
from typing import Tuple

def state_to_bloch_coordinates(alpha: complex, beta: complex) -> Tuple[float, float, float]:
    """
    Convert qubit state to Bloch sphere coordinates.

    Args:
        alpha: Amplitude of |0⟩ component
        beta: Amplitude of |1⟩ component

    Returns:
        Tuple of (x, y, z) coordinates on Bloch sphere
    """
    # Your code here
    pass
