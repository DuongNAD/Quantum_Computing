# ══════════════════════════════════════════════════════════════════════════════
# BÀI 064/350  ·  Bậc 4 · Đo lường
# Measurements/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.3
#   Gợi ý:      python qk.py hint Measurements/1.3
#   Lời giải:   python qk.py solution Measurements/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. |+⟩ or |-⟩ ?
# Input: a qubit which is guaranteed to be in either the |+⟩ or the |-⟩ state
#        (|+⟩ = (|0⟩ + |1⟩) / sqrt(2), |-⟩ = (|0⟩ - |1⟩) / sqrt(2)).
# Output: true if the qubit was in the |+⟩ state, or false if it was in the |-⟩ state.
# The state of the qubit at the end of the operation does not matter.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def is_qubit_plus(qc: QuantumCircuit, q: int) -> bool:
    """
    Distinguish between |+⟩ and |-⟩ states.

    Args:
        qc: Quantum circuit containing the qubit
        q: Index of qubit to measure

    Returns:
        True if qubit was in |+⟩, False if it was in |-⟩
    """
    # Your code here
    pass
