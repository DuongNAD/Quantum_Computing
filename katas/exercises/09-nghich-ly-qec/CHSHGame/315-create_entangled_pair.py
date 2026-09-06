# ══════════════════════════════════════════════════════════════════════════════
# BÀI 315/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# CHSHGame/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run CHSHGame/2.1
#   Gợi ý:      python qk.py hint CHSHGame/2.1
#   Lời giải:   python qk.py solution CHSHGame/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. Entangled pair
# Input: A quantum circuit and two qubits initially in the |00⟩ state.
# Goal: Create a Bell state |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2) on these qubits.
#
# This entangled pair will be shared between Alice and Bob before the quantum CHSH game starts.
# The entanglement enables them to achieve a higher win rate than classical strategies.

from qiskit import QuantumCircuit

def create_entangled_pair(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Create a Bell state |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2).

    Args:
        qc: Quantum circuit to modify
        qubits: List of two qubit indices [q0, q1]

    Returns:
        Modified quantum circuit with entangled qubits
    """
    # Your code here
    pass
