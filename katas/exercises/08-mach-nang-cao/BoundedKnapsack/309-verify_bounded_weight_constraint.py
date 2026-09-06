# ══════════════════════════════════════════════════════════════════════════════
# BÀI 309/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/2.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/2.7
#   Gợi ý:      python qk.py hint BoundedKnapsack/2.7
#   Lời giải:   python qk.py solution BoundedKnapsack/2.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.7. Verify bounded weight constraint
# Input: Quantity registers, weights, and capacity.
# Goal: Check if total weight <= capacity for bounded quantities.

from qiskit import QuantumCircuit
from typing import List

def verify_bounded_weight_constraint(qc: QuantumCircuit, weights: List[int], jagged: List[List[int]], capacity: int, target: int) -> QuantumCircuit:
    """
    Verify bounded knapsack weight constraint.

    Args:
        qc: Quantum circuit to modify
        weights: List of item weights
        jagged: Jagged array of quantity qubit indices
        capacity: Maximum weight capacity
        target: Target qubit to flip if satisfied

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
