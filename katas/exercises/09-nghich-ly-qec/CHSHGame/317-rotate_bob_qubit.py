# ══════════════════════════════════════════════════════════════════════════════
# BÀI 317/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# CHSHGame/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run CHSHGame/2.3
#   Gợi ý:      python qk.py hint CHSHGame/2.3
#   Lời giải:   python qk.py solution CHSHGame/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. Rotate Bob's qubit
# Inputs:
#      1) The direction to rotate: True for clockwise, False for counterclockwise,
#      2) Bob's qubit index.
# Goal: Rotate the qubit π/8 radians around the Y axis in the given direction.
#
# This rotation is part of Bob's quantum strategy. The Ry operation applies
# a rotation by a given angle in counterclockwise direction by default.

from qiskit import QuantumCircuit
import numpy as np

def rotate_bob_qubit(qc: QuantumCircuit, clockwise: bool, qubit: int) -> QuantumCircuit:
    """
    Rotate Bob's qubit π/8 radians around the Y axis.

    Args:
        qc: Quantum circuit to modify
        clockwise: True for clockwise rotation, False for counterclockwise
        qubit: Index of Bob's qubit to rotate

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
