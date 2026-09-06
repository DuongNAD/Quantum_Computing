# ══════════════════════════════════════════════════════════════════════════════
# BÀI 141/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/6
#   Gợi ý:      python qk.py hint MarkingOracles/6
#   Lời giải:   python qk.py solution MarkingOracles/6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 6. Divisibility oracle
# Input: A quantum circuit, query register encoding a number, and divisor d.
# Goal: Mark states where the query value is divisible by d.

from qiskit import QuantumCircuit
from typing import List

def divisibility_oracle(qc: QuantumCircuit, query: List[int], target: int, divisor: int) -> QuantumCircuit:
    """
    Oracle that marks states divisible by divisor.

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices (little-endian)
        target: Target qubit index
        divisor: The divisor to check

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
