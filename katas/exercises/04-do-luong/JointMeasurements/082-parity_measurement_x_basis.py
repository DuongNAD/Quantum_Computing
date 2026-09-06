# ══════════════════════════════════════════════════════════════════════════════
# BÀI 082/350  ·  Bậc 4 · Đo lường
# JointMeasurements/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/3
#   Gợi ý:      python qk.py hint JointMeasurements/3
#   Lời giải:   python qk.py solution JointMeasurements/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3. Parity measurement in X basis
# Input: A quantum circuit qc and two qubit indices.
# Goal: Measure the parity of two qubits in the X basis without collapsing individual qubits.
# Returns True if odd parity (different X eigenvalues), False if even parity.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def parity_measurement_x_basis(qc: QuantumCircuit, q1: int, q2: int) -> bool:
    """
    Measure X⊗X parity of two qubits.

    Args:
        qc: Quantum circuit
        q1: First qubit index
        q2: Second qubit index

    Returns:
        True if odd parity, False if even parity
    """
    # Your code here
    pass
