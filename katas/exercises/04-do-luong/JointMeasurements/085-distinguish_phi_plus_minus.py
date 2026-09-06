# ══════════════════════════════════════════════════════════════════════════════
# BÀI 085/350  ·  Bậc 4 · Đo lường
# JointMeasurements/6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/6
#   Gợi ý:      python qk.py hint JointMeasurements/6
#   Lời giải:   python qk.py solution JointMeasurements/6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 6. Distinguish Bell states |Φ+⟩ and |Φ-⟩
# Input: A quantum circuit with two qubits in either |Φ+⟩ or |Φ-⟩.
# Goal: Determine which Bell state it is.
# |Φ+⟩ = (|00⟩ + |11⟩)/√2, |Φ-⟩ = (|00⟩ - |11⟩)/√2
# Returns True for |Φ+⟩, False for |Φ-⟩.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def distinguish_phi_plus_minus(qc: QuantumCircuit, q1: int, q2: int) -> bool:
    """
    Distinguish |Φ+⟩ from |Φ-⟩ Bell states.

    Args:
        qc: Quantum circuit with Bell state
        q1: First qubit index
        q2: Second qubit index

    Returns:
        True for |Φ+⟩, False for |Φ-⟩
    """
    # Your code here
    pass
