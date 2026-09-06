# ══════════════════════════════════════════════════════════════════════════════
# BÀI 300/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/1.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/1.6
#   Gợi ý:      python qk.py hint BoundedKnapsack/1.6
#   Lời giải:   python qk.py solution BoundedKnapsack/1.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.6. Verify total weight constraint
# Input: Item weights, selection, weight register, and capacity.
# Goal: Check if total weight of selected items <= capacity.

from qiskit import QuantumCircuit
from typing import List

def verify_total_weight_constraint(qc: QuantumCircuit, weights: List[int], selection: List[int], weight_reg: List[int], capacity: int, target: int) -> QuantumCircuit:
    """
    Verify that selected items' total weight <= capacity.

    Args:
        qc: Quantum circuit to modify
        weights: List of item weights
        selection: List of selection qubit indices
        weight_reg: List of weight register qubit indices
        capacity: Maximum allowed weight
        target: Target qubit to flip if constraint satisfied

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
