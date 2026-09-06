# ══════════════════════════════════════════════════════════════════════════════
# BÀI 086/350  ·  Bậc 4 · Đo lường
# JointMeasurements/7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/7
#   Gợi ý:      python qk.py hint JointMeasurements/7
#   Lời giải:   python qk.py solution JointMeasurements/7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 7. Distinguish Bell states |Ψ+⟩ and |Ψ-⟩
# Input: A quantum circuit with two qubits in either |Ψ+⟩ or |Ψ-⟩.
# Goal: Determine which Bell state it is.
# |Ψ+⟩ = (|01⟩ + |10⟩)/√2, |Ψ-⟩ = (|01⟩ - |10⟩)/√2
# Returns True for |Ψ+⟩, False for |Ψ-⟩.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def distinguish_psi_plus_minus(qc: QuantumCircuit, q1: int, q2: int) -> bool:
    """
    Distinguish |Ψ+⟩ from |Ψ-⟩ Bell states.

    Args:
        qc: Quantum circuit with Bell state
        q1: First qubit index
        q2: Second qubit index

    Returns:
        True for |Ψ+⟩, False for |Ψ-⟩
    """
    # Your code here
    pass
