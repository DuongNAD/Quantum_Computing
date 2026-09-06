# ══════════════════════════════════════════════════════════════════════════════
# BÀI 020/350  ·  Bậc 2 · Qubit đầu tiên
# BasicGates/1.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/1.5
#   Gợi ý:      python qk.py hint BasicGates/1.5
#   Lời giải:   python qk.py solution BasicGates/1.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.5. Phase flip
# Input: A qubit in state |Ψ⟩ = α |0⟩ + β |1⟩.
# Goal: Change the qubit state to α |0⟩ + iβ |1⟩ (flip the phase of |1⟩ component of the superposition).

from qiskit import QuantumCircuit

def phase_flip(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply phase flip to the |1⟩ component of the qubit state.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply phase flip

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
