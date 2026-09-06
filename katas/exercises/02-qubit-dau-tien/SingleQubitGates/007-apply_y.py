# ══════════════════════════════════════════════════════════════════════════════
# BÀI 007/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/SingleQubitGates/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/SingleQubitGates/1
#   Gợi ý:      python qk.py hint tutorials/SingleQubitGates/1
#   Lời giải:   python qk.py solution tutorials/SingleQubitGates/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 1: The Y gate
# Input: A qubit in an arbitrary state |Ψ⟩ = α|0⟩ + β|1⟩.
# Goal: Apply the Pauli Y gate to transform the qubit state to iα|1⟩ - iβ|0⟩.

from qiskit import QuantumCircuit

def apply_y(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply the Pauli Y gate to the specified qubit.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply Y gate to

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
