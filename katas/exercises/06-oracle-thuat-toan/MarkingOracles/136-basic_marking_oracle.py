# ══════════════════════════════════════════════════════════════════════════════
# BÀI 136/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/1
#   Gợi ý:      python qk.py hint MarkingOracles/1
#   Lời giải:   python qk.py solution MarkingOracles/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1. Basic marking oracle
# Input: A quantum circuit qc, query register qubits, and a target qubit.
# Goal: Implement an oracle that marks the |11...1⟩ state by flipping the target qubit.
# The target qubit is flipped if and only if all query qubits are in state |1⟩.

from qiskit import QuantumCircuit
from typing import List

def basic_marking_oracle(qc: QuantumCircuit, query: List[int], target: int) -> QuantumCircuit:
    """
    Oracle that marks the all-ones state |11...1⟩.

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices
        target: Target qubit index to flip

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
