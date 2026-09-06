# ══════════════════════════════════════════════════════════════════════════════
# BÀI 311/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/2.9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/2.9
#   Gợi ý:      python qk.py hint BoundedKnapsack/2.9
#   Lời giải:   python qk.py solution BoundedKnapsack/2.9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.9. Verify bounded knapsack solution
# Input: Complete bounded knapsack problem parameters.
# Goal: Verify solution satisfies all constraints.

from qiskit import QuantumCircuit
from typing import List
from itertools import product

def verify_bounded_knapsack_solution(qc: QuantumCircuit, values: List[int], weights: List[int], jagged: List[List[int]], capacity: int, min_profit: int, target: int) -> QuantumCircuit:
    """
    Verify complete bounded knapsack solution.

    Args:
        qc: Quantum circuit to modify
        values: List of item values/profits
        weights: List of item weights
        jagged: Jagged array of quantity qubit indices
        capacity: Maximum weight capacity
        min_profit: Minimum required profit
        target: Target qubit to flip if valid

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
