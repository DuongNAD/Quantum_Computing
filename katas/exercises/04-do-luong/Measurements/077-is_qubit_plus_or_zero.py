# ══════════════════════════════════════════════════════════════════════════════
# BÀI 077/350  ·  Bậc 4 · Đo lường
# Measurements/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/2.1
#   Gợi ý:      python qk.py hint Measurements/2.1
#   Lời giải:   python qk.py solution Measurements/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1*. |0⟩ or |+⟩ ?
# (quantum hypothesis testing or state discrimination with minimum error)
# Input: a qubit which is guaranteed to be in either the |0⟩ or the |+⟩ state with equal probability.
# Output: true if qubit was in the |0⟩ state, or false if it was in the |+⟩ state.
# The state of the qubit at the end of the operation does not matter.
# Note: in this task you have to get accuracy of at least 80%.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np

def is_qubit_plus_or_zero(qc: QuantumCircuit, q: int) -> bool:
    """
    Distinguish |0⟩ from |+⟩ with minimum error (optimal measurement).

    Args:
        qc: Quantum circuit containing the qubit
        q: Index of qubit to measure

    Returns:
        True if qubit was in |0⟩, False if it was in |+⟩
    """
    # Your code here
    pass
