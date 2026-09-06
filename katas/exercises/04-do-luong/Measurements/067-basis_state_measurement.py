# ══════════════════════════════════════════════════════════════════════════════
# BÀI 067/350  ·  Bậc 4 · Đo lường
# Measurements/1.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.6
#   Gợi ý:      python qk.py hint Measurements/1.6
#   Lời giải:   python qk.py solution Measurements/1.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.6. Distinguish four basis states
# Input: two qubits (stored in an array) which are guaranteed to be
#        in one of the four basis states (|00⟩, |01⟩, |10⟩ or |11⟩).
# Output: 0 if the qubits were in |00⟩ state,
#         1 if they were in |01⟩ state,
#         2 if they were in |10⟩ state,
#         3 if they were in |11⟩ state.
# In this task and the subsequent ones the order of qubit states
# in task description matches the order of qubits in the array
# (i.e., |10⟩ state corresponds to qs[0] in state |1⟩ and qs[1] in state |0⟩).
# The state of the qubits at the end of the operation does not matter.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def basis_state_measurement(qc: QuantumCircuit, qs: list) -> int:
    """
    Distinguish between four computational basis states.

    Args:
        qc: Quantum circuit containing the qubits
        qs: List of two qubit indices

    Returns:
        0 for |00⟩, 1 for |01⟩, 2 for |10⟩, 3 for |11⟩
    """
    # Your code here
    pass
