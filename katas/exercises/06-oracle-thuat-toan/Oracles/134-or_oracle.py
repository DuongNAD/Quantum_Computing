# ══════════════════════════════════════════════════════════════════════════════
# BÀI 134/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# tutorials/Oracles/3.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/Oracles/3.1
#   Gợi ý:      python qk.py hint tutorials/Oracles/3.1
#   Lời giải:   python qk.py solution tutorials/Oracles/3.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.1: OR Oracle
# Input: Query qubits and target qubit.
# Goal: Implement OR oracle that flips target if any query qubit is |1⟩.
#       Transform |x,y⟩ to |x, y ⊕ (x₀ ∨ x₁ ∨ ... ∨ xₙ)⟩.

from qiskit import QuantumCircuit

def or_oracle(qc: QuantumCircuit, x: list, y: int) -> QuantumCircuit:
    """
    OR oracle that flips target if any query qubit is |1⟩.

    Args:
        qc: Quantum circuit to modify
        x: List of query qubit indices
        y: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
