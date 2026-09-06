# ══════════════════════════════════════════════════════════════════════════════
# BÀI 065/350  ·  Bậc 4 · Đo lường
# Measurements/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.4
#   Gợi ý:      python qk.py hint Measurements/1.4
#   Lời giải:   python qk.py solution Measurements/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. |A⟩ or |B⟩ ?
# Inputs:
#      1) angle α, in radians, represented as a Double
#      2) a qubit which is guaranteed to be in either the |A⟩ or the |B⟩ state, where
#         |A⟩ =   cos α |0⟩ + sin α |1⟩,
#         |B⟩ = - sin α |0⟩ + cos α |1⟩.
# Output: true if the qubit was in the |A⟩ state, or false if it was in the |B⟩ state.
# The state of the qubit at the end of the operation does not matter.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def is_qubit_a(qc: QuantumCircuit, alpha: float, q: int) -> bool:
    """
    Determine if a qubit is in state |A⟩ or |B⟩.

    Args:
        qc: Quantum circuit containing the qubit
        alpha: Angle parameter in radians
        q: Index of qubit to measure

    Returns:
        True if qubit was in |A⟩, False if it was in |B⟩
    """
    # Your code here
    pass
