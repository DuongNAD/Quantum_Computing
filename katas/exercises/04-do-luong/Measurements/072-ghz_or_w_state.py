# ══════════════════════════════════════════════════════════════════════════════
# BÀI 072/350  ·  Bậc 4 · Đo lường
# Measurements/1.11
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.11
#   Gợi ý:      python qk.py hint Measurements/1.11
#   Lời giải:   python qk.py solution Measurements/1.11
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.11. GHZ state or W state ?
# Input: N >= 2 qubits (stored in an array) which are guaranteed to be
#        either in the GHZ state (https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state)
#        or in the W state (https://en.wikipedia.org/wiki/W_state).
# Output: 0 if the qubits were in the GHZ state,
#         1 if they were in the W state.
# The state of the qubits at the end of the operation does not matter.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import List

def ghz_or_w_state(qc: QuantumCircuit, qs: List[int]) -> int:
    """
    Distinguish between GHZ state and W state.

    Args:
        qc: Quantum circuit containing the qubits
        qs: List of qubit indices

    Returns:
        0 if qubits were in GHZ state, 1 if they were in W state
    """
    # Your code here
    pass
