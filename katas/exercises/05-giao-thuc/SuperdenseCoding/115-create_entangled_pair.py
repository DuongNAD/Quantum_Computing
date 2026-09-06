# ══════════════════════════════════════════════════════════════════════════════
# BÀI 115/350  ·  Bậc 5 · Giao thức lượng tử
# SuperdenseCoding/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SuperdenseCoding/1
#   Gợi ý:      python qk.py hint SuperdenseCoding/1
#   Lời giải:   python qk.py solution SuperdenseCoding/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1. Entangled pair
# Input: Two qubits, each in the |0⟩ state.
# Goal: Create a Bell state |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2) on these qubits.
# This is the preparation step for superdense coding protocol.

from qiskit import QuantumCircuit

def create_entangled_pair(qc: QuantumCircuit, q1: int, q2: int) -> QuantumCircuit:
    """
    Create Bell state |φ⁺⟩ for superdense coding.

    Args:
        qc: Quantum circuit to modify
        q1: Index of first qubit
        q2: Index of second qubit

    Returns:
        Modified quantum circuit with qubits in Bell state |φ⁺⟩
    """
    # Your code here
    pass
