# ══════════════════════════════════════════════════════════════════════════════
# BÀI 074/350  ·  Bậc 4 · Đo lường
# Measurements/1.13
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.13
#   Gợi ý:      python qk.py hint Measurements/1.13
#   Lời giải:   python qk.py solution Measurements/1.13
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.13. Distinguish four orthogonal 2-qubit states
# Input: two qubits (stored in an array) which are guaranteed to be in one of the four orthogonal states:
#         |S0⟩ = (|00⟩ + |01⟩ + |10⟩ + |11⟩) / 2
#         |S1⟩ = (|00⟩ - |01⟩ + |10⟩ - |11⟩) / 2
#         |S2⟩ = (|00⟩ + |01⟩ - |10⟩ - |11⟩) / 2
#         |S3⟩ = (|00⟩ - |01⟩ - |10⟩ + |11⟩) / 2
# Output: 0 if qubits were in |S0⟩ state,
#         1 if they were in |S1⟩ state,
#         2 if they were in |S2⟩ state,
#         3 if they were in |S3⟩ state.
# The state of the qubits at the end of the operation does not matter.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def two_qubit_state(qc: QuantumCircuit, qs: list) -> int:
    """
    Distinguish between four orthogonal 2-qubit states.

    Args:
        qc: Quantum circuit containing the 2-qubit state
        qs: List of two qubit indices

    Returns:
        0 for |S0⟩, 1 for |S1⟩, 2 for |S2⟩, 3 for |S3⟩
    """
    # Your code here
    pass
