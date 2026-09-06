# ══════════════════════════════════════════════════════════════════════════════
# BÀI 036/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# BasicGates/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/2.2
#   Gợi ý:      python qk.py hint BasicGates/2.2
#   Lời giải:   python qk.py solution BasicGates/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Two-qubit gate - 2
# Input: Two unentangled qubits (stored in an array of length 2)
#        in state |+⟩ ⊗ |+⟩ = (|00⟩ + |01⟩ + |10⟩ + |11⟩) / 2.
# Goal: Change the two-qubit state to (|00⟩ + |01⟩ + |10⟩ - |11⟩) / 2.
# Note that while the starting state can be represented as a tensor product of single-qubit states,
# the resulting two-qubit state can not be represented in such a way.

from qiskit import QuantumCircuit

def two_qubit_gate_2(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Transform |+⟩⊗|+⟩ to (|00⟩ + |01⟩ + |10⟩ - |11⟩)/2

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices [q0, q1]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
