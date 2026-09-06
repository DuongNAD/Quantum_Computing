# ══════════════════════════════════════════════════════════════════════════════
# BÀI 087/350  ·  Bậc 4 · Đo lường
# JointMeasurements/8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/8
#   Gợi ý:      python qk.py hint JointMeasurements/8
#   Lời giải:   python qk.py solution JointMeasurements/8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 8. Distinguish all four Bell states
# Input: A quantum circuit with two qubits in one of the four Bell states.
# Goal: Identify which Bell state it is.
# Returns: 0 for |Φ+⟩, 1 for |Φ-⟩, 2 for |Ψ+⟩, 3 for |Ψ-⟩

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def distinguish_all_bell_states(qc: QuantumCircuit, q1: int, q2: int) -> int:
    """
    Identify which of the four Bell states the qubits are in.

    Args:
        qc: Quantum circuit with Bell state
        q1: First qubit index
        q2: Second qubit index

    Returns:
        0: |Φ+⟩, 1: |Φ-⟩, 2: |Ψ+⟩, 3: |Ψ-⟩
    """
    # Your code here
    pass
