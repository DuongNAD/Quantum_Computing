# ══════════════════════════════════════════════════════════════════════════════
# BÀI 228/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/7
#   Gợi ý:      python qk.py hint UnitaryPatterns/7
#   Lời giải:   python qk.py solution UnitaryPatterns/7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 7. Rotation pattern
# Input: A quantum circuit qc, a qubit index q, and an angle theta.
# Goal: Apply rotation gates Rx, Ry, Rz based on the specified axis.
# This implementation applies Rz rotation by angle theta.

from qiskit import QuantumCircuit
import numpy as np

def rotation_pattern(qc: QuantumCircuit, q: int, theta: float) -> QuantumCircuit:
    """
    Apply Rz rotation by angle theta to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to rotate
        theta: Rotation angle in radians

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
