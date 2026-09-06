# ══════════════════════════════════════════════════════════════════════════════
# BÀI 017/350  ·  Bậc 2 · Qubit đầu tiên
# BasicGates/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/1.2
#   Gợi ý:      python qk.py hint BasicGates/1.2
#   Lời giải:   python qk.py solution BasicGates/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. Basis change: |0⟩ to |+⟩ and |1⟩ to |-⟩ (and vice versa)
# Input: A qubit in state |Ψ⟩ = α |0⟩ + β |1⟩.
# Goal: Change the state of the qubit as follows:
#        If the qubit is in state |0⟩, change its state to |+⟩ = (|0⟩ + |1⟩) / sqrt(2).
#        If the qubit is in state |1⟩, change its state to |-⟩ = (|0⟩ - |1⟩) / sqrt(2).
#        If the qubit is in superposition, change its state according to the effect on basis vectors.
# Note: |+⟩ and |-⟩ form a different basis for single-qubit states, called X basis.
# |0⟩ and |1⟩ are called Z basis.

from qiskit import QuantumCircuit

def basis_change(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply basis change from Z basis to X basis.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply basis change

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
