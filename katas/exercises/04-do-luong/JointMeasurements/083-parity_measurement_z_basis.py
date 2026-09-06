# ══════════════════════════════════════════════════════════════════════════════
# BÀI 083/350  ·  Bậc 4 · Đo lường
# JointMeasurements/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/4
#   Gợi ý:      python qk.py hint JointMeasurements/4
#   Lời giải:   python qk.py solution JointMeasurements/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4. Parity measurement in Z basis
# Input: A quantum circuit qc and two qubit indices.
# Goal: Measure the parity of two qubits in the Z basis.
# Returns True if odd parity (|01⟩ or |10⟩), False if even parity (|00⟩ or |11⟩).

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def parity_measurement_z_basis(qc: QuantumCircuit, q1: int, q2: int) -> bool:
    """
    Measure Z⊗Z parity of two qubits.

    Args:
        qc: Quantum circuit
        q1: First qubit index
        q2: Second qubit index

    Returns:
        True if odd parity, False if even parity
    """
    # Your code here
    pass
