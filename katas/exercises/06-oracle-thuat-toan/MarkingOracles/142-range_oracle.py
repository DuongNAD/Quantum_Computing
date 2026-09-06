# ══════════════════════════════════════════════════════════════════════════════
# BÀI 142/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/7
#   Gợi ý:      python qk.py hint MarkingOracles/7
#   Lời giải:   python qk.py solution MarkingOracles/7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 7. Range oracle
# Input: A quantum circuit, query register, and range bounds [low, high].
# Goal: Mark states where low <= query_value <= high.

from qiskit import QuantumCircuit
from typing import List

def range_oracle(qc: QuantumCircuit, query: List[int], target: int, low: int, high: int) -> QuantumCircuit:
    """
    Oracle that marks states in range [low, high].

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices (little-endian)
        target: Target qubit index
        low: Lower bound (inclusive)
        high: Upper bound (inclusive)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
