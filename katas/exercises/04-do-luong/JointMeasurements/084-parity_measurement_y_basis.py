# ══════════════════════════════════════════════════════════════════════════════
# BÀI 084/350  ·  Bậc 4 · Đo lường
# JointMeasurements/5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/5
#   Gợi ý:      python qk.py hint JointMeasurements/5
#   Lời giải:   python qk.py solution JointMeasurements/5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 5. Parity measurement in Y basis
# Input: A quantum circuit qc and two qubit indices.
# Goal: Measure the parity of two qubits in the Y basis.
# Returns True if odd parity, False if even parity.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np

def parity_measurement_y_basis(qc: QuantumCircuit, q1: int, q2: int) -> bool:
    """
    Measure Y⊗Y parity of two qubits.

    Args:
        qc: Quantum circuit
        q1: First qubit index
        q2: Second qubit index

    Returns:
        True if odd parity, False if even parity
    """
    # Your code here
    pass
