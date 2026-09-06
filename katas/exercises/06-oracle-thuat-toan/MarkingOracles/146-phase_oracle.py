# ══════════════════════════════════════════════════════════════════════════════
# BÀI 146/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/11
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/11
#   Gợi ý:      python qk.py hint MarkingOracles/11
#   Lời giải:   python qk.py solution MarkingOracles/11
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 11. Phase oracle
# Input: A quantum circuit, query register, and pattern to mark.
# Goal: Apply a phase flip (-1) to the marked state instead of using a target qubit.
# This is the phase kickback version of marking oracles used in Grover's algorithm.

from qiskit import QuantumCircuit
from typing import List
import numpy as np

def phase_oracle(qc: QuantumCircuit, query: List[int], pattern: List[bool]) -> QuantumCircuit:
    """
    Phase oracle that applies -1 phase to the marked pattern.

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices
        pattern: Boolean list representing the pattern to mark

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
