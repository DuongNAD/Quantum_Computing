# ══════════════════════════════════════════════════════════════════════════════
# BÀI 120/350  ·  Bậc 5 · Giao thức lượng tử
# KeyDistribution_BB84/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run KeyDistribution_BB84/1.1
#   Gợi ý:      python qk.py hint KeyDistribution_BB84/1.1
#   Lời giải:   python qk.py solution KeyDistribution_BB84/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. Diagonal Basis
# Try converting qubits from the computational basis to the diagonal basis.
# Input: N qubits (stored in a list of length N).
#        Each qubit is either in |0⟩ or in |1⟩ state.
# Goal: Convert the qubits to diagonal polarization:
#       if qs[i] was in state |0⟩, it should become |+⟩ = (|0⟩ + |1⟩) / sqrt(2),
#       if qs[i] was in state |1⟩, it should become |-⟩ = (|0⟩ - |1⟩) / sqrt(2).
#
# The diagonal basis (also called X basis or Hadamard basis) is crucial for BB84
# quantum key distribution protocol.

from qiskit import QuantumCircuit

def diagonal_basis(qc: QuantumCircuit, qubits: list[int]) -> QuantumCircuit:
    """
    Convert qubits from computational basis to diagonal basis.

    Args:
        qc: Quantum circuit to modify
        qubits: List of qubit indices to convert

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
