# ══════════════════════════════════════════════════════════════════════════════
# BÀI 301/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/1.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/1.7
#   Gợi ý:      python qk.py hint BoundedKnapsack/1.7
#   Lời giải:   python qk.py solution BoundedKnapsack/1.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.7. Verify total profit constraint
# Input: Item profits, selection, profit register, and minimum profit.
# Goal: Check if total profit of selected items >= minimum.

from qiskit import QuantumCircuit
from typing import List

def verify_total_profit_constraint(qc: QuantumCircuit, profits: List[int], selection: List[int], profit_reg: List[int], min_profit: int, target: int) -> QuantumCircuit:
    """
    Verify that selected items' total profit >= min_profit.

    Args:
        qc: Quantum circuit to modify
        profits: List of item profits
        selection: List of selection qubit indices
        profit_reg: List of profit register qubit indices
        min_profit: Minimum required profit
        target: Target qubit to flip if constraint satisfied

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
