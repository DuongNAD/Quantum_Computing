# ══════════════════════════════════════════════════════════════════════════════
# BÀI 233/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/12
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/12
#   Gợi ý:      python qk.py hint UnitaryPatterns/12
#   Lời giải:   python qk.py solution UnitaryPatterns/12
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 12. Parametric gate pattern
# Input: A quantum circuit qc, qubit index q, and three rotation angles.
# Goal: Apply a general single-qubit rotation U3(theta, phi, lambda).
# U3 is the most general single-qubit gate.

from qiskit import QuantumCircuit
import numpy as np

def parametric_pattern(qc: QuantumCircuit, q: int, theta: float, phi: float, lam: float) -> QuantumCircuit:
    """
    Apply U3 gate with parameters theta, phi, lambda.

    Args:
        qc: Quantum circuit to modify
        q: Qubit index
        theta: Rotation angle theta
        phi: Rotation angle phi
        lam: Rotation angle lambda

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
