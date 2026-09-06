# ══════════════════════════════════════════════════════════════════════════════
# BÀI 062/350  ·  Bậc 4 · Đo lường
# Measurements/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.1
#   Gợi ý:      python qk.py hint Measurements/1.1
#   Lời giải:   python qk.py solution Measurements/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. |0⟩ or |1⟩ ?
# Input: a qubit which is guaranteed to be in either the |0⟩ or the |1⟩ state.
# Output: true if the qubit was in the |1⟩ state, or false if it was in the |0⟩ state.
# The state of the qubit at the end of the operation does not matter.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def is_qubit_one(qc: QuantumCircuit, q: int) -> bool:
    """
    Measure a qubit and return True if it was in |1⟩ state.

    Args:
        qc: Quantum circuit containing the qubit
        q: Index of qubit to measure

    Returns:
        True if qubit was in |1⟩, False if it was in |0⟩
    """
    # Your code here
    pass
