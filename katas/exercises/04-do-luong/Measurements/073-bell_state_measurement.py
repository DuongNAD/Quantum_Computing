# ══════════════════════════════════════════════════════════════════════════════
# BÀI 073/350  ·  Bậc 4 · Đo lường
# Measurements/1.12
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.12
#   Gợi ý:      python qk.py hint Measurements/1.12
#   Lời giải:   python qk.py solution Measurements/1.12
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.12. Distinguish four Bell states
# Input: two qubits (stored in an array) which are guaranteed to be in one of the four Bell states:
#         |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2)
#         |φ⁻⟩ = (|00⟩ - |11⟩) / sqrt(2)
#         |Ψ⁺⟩ = (|01⟩ + |10⟩) / sqrt(2)
#         |Ψ⁻⟩ = (|01⟩ - |10⟩) / sqrt(2)
# Output: 0 if the qubits were in |φ⁺⟩ state,
#         1 if they were in |φ⁻⟩ state,
#         2 if they were in |Ψ⁺⟩ state,
#         3 if they were in |Ψ⁻⟩ state.
# The state of the qubits at the end of the operation does not matter.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def bell_state_measurement(qc: QuantumCircuit, qs: list) -> int:
    """
    Distinguish between four Bell states using Bell measurement.

    Args:
        qc: Quantum circuit containing the Bell state
        qs: List of two qubit indices

    Returns:
        0 for |φ⁺⟩, 1 for |φ⁻⟩, 2 for |Ψ⁺⟩, 3 for |Ψ⁻⟩
    """
    # Your code here
    pass
