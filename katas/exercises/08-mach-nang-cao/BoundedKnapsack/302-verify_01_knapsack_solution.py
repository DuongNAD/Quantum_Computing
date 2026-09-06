# ══════════════════════════════════════════════════════════════════════════════
# BÀI 302/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/1.8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/1.8
#   Gợi ý:      python qk.py hint BoundedKnapsack/1.8
#   Lời giải:   python qk.py solution BoundedKnapsack/1.8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.8. Verify 0/1 knapsack solution
# Input: Item values, weights, selection, and constraints.
# Goal: Verify complete knapsack solution (weight and profit constraints).

from qiskit import QuantumCircuit
from typing import List

def verify_01_knapsack_solution(qc: QuantumCircuit, values: List[int], weights: List[int], selection: List[int], capacity: int, min_profit: int, target: int) -> QuantumCircuit:
    """
    Verify complete 0/1 knapsack solution.

    Args:
        qc: Quantum circuit to modify
        values: List of item values/profits
        weights: List of item weights
        selection: List of selection qubit indices
        capacity: Maximum weight capacity
        min_profit: Minimum required profit
        target: Target qubit to flip if valid solution

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
