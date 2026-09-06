# ══════════════════════════════════════════════════════════════════════════════
# BÀI 197/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/2.1
#   Gợi ý:      python qk.py hint QFT/2.1
#   Lời giải:   python qk.py solution QFT/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. Prepare an equal superposition of all basis states
# Input: A register of n qubits in state |0...0⟩.
# Goal: Prepare an equal superposition of all basis vectors from |0...0⟩ to |1...1⟩
#       (i.e., state (|0...0⟩ + ... + |1...1⟩) / sqrt(2ⁿ) ).

from qiskit import QuantumCircuit
from typing import List

def prepare_equal_superposition(qc: QuantumCircuit, register: List[int]) -> QuantumCircuit:
    """
    Prepare equal superposition of all basis states using QFT.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
