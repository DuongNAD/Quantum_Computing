# ══════════════════════════════════════════════════════════════════════════════
# BÀI 308/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/2.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/2.6
#   Gợi ý:      python qk.py hint BoundedKnapsack/2.6
#   Lời giải:   python qk.py solution BoundedKnapsack/2.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.6. Calculate total value for bounded knapsack
# Input: Quantity registers, values, and result register.
# Goal: Calculate total value = sum(quantity[i] * value[i]).

from qiskit import QuantumCircuit
from typing import List

def calculate_total_value_bounded(qc: QuantumCircuit, values: List[int], jagged: List[List[int]], result: List[int]) -> QuantumCircuit:
    """
    Calculate total value from quantities and values.

    Args:
        qc: Quantum circuit to modify
        values: List of item values
        jagged: Jagged array of quantity qubit indices
        result: Result register qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
