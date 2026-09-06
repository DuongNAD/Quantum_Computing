# ══════════════════════════════════════════════════════════════════════════════
# BÀI 078/350  ·  Bậc 4 · Đo lường
# Measurements/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/2.2
#   Gợi ý:      python qk.py hint Measurements/2.2
#   Lời giải:   python qk.py solution Measurements/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2**. |0⟩, |+⟩ or inconclusive?
#             (unambiguous state discrimination)
# Input: a qubit which is guaranteed to be in either the |0⟩ or the |+⟩ state with equal probability.
# Output: 0 if qubit was in the |0⟩ state,
#         1 if it was in the |+⟩ state,
#         -1 if you can't decide, i.e., an "inconclusive" result.
# Your solution:
#  - should never give 0 or 1 answer incorrectly (i.e., identify |0⟩ as 1 or |+⟩ as 0).
#  - may give an inconclusive (-1) answer in at most 80% of the cases.
#  - must correctly identify |0⟩ state as 0 in at least 10% of the cases.
#  - must correctly identify |+⟩ state as 1 in at least 10% of the cases.
#
# The state of the qubit at the end of the operation does not matter.

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator
import numpy as np

def is_qubit_plus_zero_or_inconclusive_simple_usd(qc: QuantumCircuit, q: int) -> int:
    """
    Unambiguous state discrimination between |0⟩ and |+⟩.

    Args:
        qc: Quantum circuit containing the qubit
        q: Index of qubit to measure

    Returns:
        0 if qubit was in |0⟩, 1 if it was in |+⟩, -1 if inconclusive
    """
    # Your code here
    pass
