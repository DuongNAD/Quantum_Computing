# ══════════════════════════════════════════════════════════════════════════════
# BÀI 090/350  ·  Bậc 4 · Đo lường
# JointMeasurements/11
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/11
#   Gợi ý:      python qk.py hint JointMeasurements/11
#   Lời giải:   python qk.py solution JointMeasurements/11
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 11. Multi-qubit parity measurement
# Input: A quantum circuit and a list of qubit indices.
# Goal: Measure the parity of all specified qubits in Z basis.
# Returns True if odd number of |1⟩s, False if even number.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def multi_qubit_parity(qc: QuantumCircuit, qubits: list) -> bool:
    """
    Measure Z-basis parity of multiple qubits.

    Args:
        qc: Quantum circuit
        qubits: List of qubit indices

    Returns:
        True if odd parity, False if even parity
    """
    # Your code here
    pass
