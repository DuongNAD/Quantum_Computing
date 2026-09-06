# ══════════════════════════════════════════════════════════════════════════════
# BÀI 137/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/2
#   Gợi ý:      python qk.py hint MarkingOracles/2
#   Lời giải:   python qk.py solution MarkingOracles/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2. Multi-target oracle
# Input: A quantum circuit qc, query register, and a pattern to mark.
# Goal: Mark a specific bit pattern by flipping target when query matches pattern.
# Example: pattern [True, False, True] marks |101⟩.

from qiskit import QuantumCircuit
from typing import List

def multi_target_oracle(qc: QuantumCircuit, query: List[int], target: int, pattern: List[bool]) -> QuantumCircuit:
    """
    Oracle that marks a specific bit pattern.

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices
        target: Target qubit index
        pattern: Boolean list representing the pattern to mark

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
