# ══════════════════════════════════════════════════════════════════════════════
# BÀI 331/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/2.1
#   Gợi ý:      python qk.py hint MagicSquareGame/2.1
#   Lời giải:   python qk.py solution MagicSquareGame/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. Entangled state
# Input: An array of 4 qubits in the |0000⟩ state.
# Goal:
#     Create the entangled state
#     |Ψ⟩ = ((|+⟩₀ ⊗ |+⟩₂ + |-⟩₀ ⊗ |-⟩₂) / sqrt(2)) ⊗ ((|+⟩₁ ⊗ |+⟩₃ + |-⟩₁ ⊗ |-⟩₃) / sqrt(2)),
#     where |Ψ⟩₀ and |Ψ⟩₁ are Alice's qubits and |Ψ⟩₂ and |Ψ⟩₃ are Bob's qubits.
#
# Hint: Can you represent this state as a combination of Bell pairs?

from qiskit import QuantumCircuit

def create_entangled_state(qc: QuantumCircuit, qs: list[int]) -> QuantumCircuit:
    """
    Create the entangled state for the magic square game.

    Args:
        qc: Quantum circuit to modify
        qs: List of 4 qubit indices [alice0, alice1, bob0, bob1]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
