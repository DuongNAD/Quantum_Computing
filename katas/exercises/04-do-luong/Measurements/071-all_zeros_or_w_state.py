# ══════════════════════════════════════════════════════════════════════════════
# BÀI 071/350  ·  Bậc 4 · Đo lường
# Measurements/1.10
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.10
#   Gợi ý:      python qk.py hint Measurements/1.10
#   Lời giải:   python qk.py solution Measurements/1.10
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.10. |0...0⟩ state or W state ?
# Input: N qubits (stored in an array) which are guaranteed to be
#        either in the |0...0⟩ state or in the W state.
# W state: https://en.wikipedia.org/wiki/W_state
# For N qubits: |W⟩ = (|100...0⟩ + |010...0⟩ + ... + |000...1⟩) / sqrt(N)
# Output: 0 if the qubits were in the |0...0⟩ state,
#         1 if they were in the W state.
# The state of the qubits at the end of the operation does not matter.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def all_zeros_or_w_state(qc: QuantumCircuit, qs: list) -> int:
    """
    Distinguish between |0...0⟩ and W state.

    Args:
        qc: Quantum circuit containing the qubits
        qs: List of qubit indices

    Returns:
        0 if qubits were in |0...0⟩ state, 1 if they were in W state
    """
    # Your code here
    pass
