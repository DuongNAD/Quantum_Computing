# ══════════════════════════════════════════════════════════════════════════════
# BÀI 079/350  ·  Bậc 4 · Đo lường
# Measurements/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/2.3
#   Gợi ý:      python qk.py hint Measurements/2.3
#   Lời giải:   python qk.py solution Measurements/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3**. Unambiguous state discrimination of 3 non-orthogonal states on one qubit
#             (a.k.a. the Peres/Wootters game)
# Input: a qubit which is guaranteed to be in one of the three states with equal probability:
#        |A⟩ = 1/sqrt(2) (|0⟩ + |1⟩),
#        |B⟩ = 1/sqrt(2) (|0⟩ + ω |1⟩),
#        |C⟩ = 1/sqrt(2) (|0⟩ + ω² |1⟩),
#          where ω = exp(2iπ/3) denotes a primitive, complex 3rd root of unity.
# Output: 1 or 2 if the qubit was in the |A⟩ state,
#         0 or 2 if the qubit was in the |B⟩ state,
#         0 or 1 if the qubit was in the |C⟩ state.
# The state of the qubit at the end of the operation does not matter.
# You can use extra qubit(s) in your solution.
# Note: in this task you have to succeed with probability 1, i.e., you are never allowed
#       to give an incorrect answer.

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator
import numpy as np

def is_qubit_not_in_abc(qc: QuantumCircuit, q: int) -> int:
    """
    Unambiguous state discrimination of three non-orthogonal states.

    Args:
        qc: Quantum circuit containing the qubit
        q: Index of qubit to measure

    Returns:
        1 or 2 if qubit was in |A⟩,
        0 or 2 if qubit was in |B⟩,
        0 or 1 if qubit was in |C⟩
    """
    # Your code here
    pass
