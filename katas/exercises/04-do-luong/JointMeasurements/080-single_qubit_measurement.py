# ══════════════════════════════════════════════════════════════════════════════
# BÀI 080/350  ·  Bậc 4 · Đo lường
# JointMeasurements/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/1
#   Gợi ý:      python qk.py hint JointMeasurements/1
#   Lời giải:   python qk.py solution JointMeasurements/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1. Single qubit measurement
# Input: A quantum circuit qc and a qubit index q.
# Goal: Measure the qubit in the computational (Z) basis and return the result.
# Returns True if measured |1⟩, False if measured |0⟩.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def single_qubit_measurement(qc: QuantumCircuit, q: int) -> bool:
    """
    Measure qubit q in computational basis.

    Args:
        qc: Quantum circuit with prepared state
        q: Index of qubit to measure

    Returns:
        True if |1⟩, False if |0⟩
    """
    # Your code here
    pass
