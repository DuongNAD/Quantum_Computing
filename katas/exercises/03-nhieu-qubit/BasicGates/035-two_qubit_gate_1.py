# ══════════════════════════════════════════════════════════════════════════════
# BÀI 035/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# BasicGates/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/2.1
#   Gợi ý:      python qk.py hint BasicGates/2.1
#   Lời giải:   python qk.py solution BasicGates/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. Two-qubit gate - 1
# Input: Two unentangled qubits (stored in an array of length 2).
#        The first qubit will be in state |Ψ⟩ = α |0⟩ + β |1⟩, the second - in state |0⟩
#        (this can be written as two-qubit state (α|0⟩ + β|1⟩) ⊗ |0⟩).
# Goal: Change the two-qubit state to α |00⟩ + β |11⟩.
# Note that unless the starting state of the first qubit was |0⟩ or |1⟩,
# the resulting two-qubit state can not be represented as a tensor product
# of the states of individual qubits any longer; thus the qubits become entangled.

from qiskit import QuantumCircuit

def two_qubit_gate_1(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Create entanglement: (α|0⟩ + β|1⟩) ⊗ |0⟩ -> α|00⟩ + β|11⟩

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices [control, target]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
