# ══════════════════════════════════════════════════════════════════════════════
# BÀI 310/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/2.8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/2.8
#   Gợi ý:      python qk.py hint BoundedKnapsack/2.8
#   Lời giải:   python qk.py solution BoundedKnapsack/2.8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.8. Verify bounded profit constraint
# Input: Quantity registers, profits, and minimum profit.
# Goal: Check if total profit >= minimum for bounded quantities.

from qiskit import QuantumCircuit
from typing import List

def verify_bounded_profit_constraint(qc: QuantumCircuit, profits: List[int], jagged: List[List[int]], min_profit: int, target: int) -> QuantumCircuit:
    """
    Verify bounded knapsack profit constraint.

    Args:
        qc: Quantum circuit to modify
        profits: List of item profits
        jagged: Jagged array of quantity qubit indices
        min_profit: Minimum required profit
        target: Target qubit to flip if satisfied

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
