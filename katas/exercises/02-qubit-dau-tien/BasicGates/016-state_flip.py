# ══════════════════════════════════════════════════════════════════════════════
# BÀI 016/350  ·  Bậc 2 · Qubit đầu tiên
# BasicGates/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/1.1
#   Gợi ý:      python qk.py hint BasicGates/1.1
#   Lời giải:   python qk.py solution BasicGates/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. State flip: |0⟩ to |1⟩ and vice versa
# Input: A qubit in state |Ψ⟩ = α |0⟩ + β |1⟩.
# Goal: Change the state of the qubit to α |1⟩ + β |0⟩.
# Example:
#     If the qubit is in state |0⟩, change its state to |1⟩.
#     If the qubit is in state |1⟩, change its state to |0⟩.
# Note that this operation is self-adjoint: applying it for a second time
# returns the qubit to the original state.

from qiskit import QuantumCircuit, QuantumRegister

def state_flip(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply a state flip operation to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to flip

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
