# ══════════════════════════════════════════════════════════════════════════════
# BÀI 066/350  ·  Bậc 4 · Đo lường
# Measurements/1.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.5
#   Gợi ý:      python qk.py hint Measurements/1.5
#   Lời giải:   python qk.py solution Measurements/1.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.5. |00⟩ or |11⟩ ?
# Input: two qubits (stored in an array of length 2) which are guaranteed to be in either the |00⟩ or the |11⟩ state.
# Output: 0 if the qubits were in the |00⟩ state, 1 if they were in |11⟩ state.
# The state of the qubits at the end of the operation does not matter.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def zero_zero_or_one_one(qc: QuantumCircuit, qs: list) -> int:
    """
    Distinguish between |00⟩ and |11⟩ states.

    Args:
        qc: Quantum circuit containing the qubits
        qs: List of two qubit indices

    Returns:
        0 if qubits were in |00⟩, 1 if they were in |11⟩
    """
    # Your code here
    pass
