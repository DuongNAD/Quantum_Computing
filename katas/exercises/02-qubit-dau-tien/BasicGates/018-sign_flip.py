# ══════════════════════════════════════════════════════════════════════════════
# BÀI 018/350  ·  Bậc 2 · Qubit đầu tiên
# BasicGates/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/1.3
#   Gợi ý:      python qk.py hint BasicGates/1.3
#   Lời giải:   python qk.py solution BasicGates/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. Sign flip: |+⟩ to |-⟩ and vice versa.
# Input: A qubit in state |Ψ⟩ = α |0⟩ + β |1⟩.
# Goal: Change the qubit state to α |0⟩ - β |1⟩ (flip the sign of |1⟩ component of the superposition).

from qiskit import QuantumCircuit

def sign_flip(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply sign flip to the |1⟩ component of the qubit state.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply sign flip

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
