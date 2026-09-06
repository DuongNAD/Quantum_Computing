# ══════════════════════════════════════════════════════════════════════════════
# BÀI 306/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/2.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/2.4
#   Gợi ý:      python qk.py hint BoundedKnapsack/2.4
#   Lời giải:   python qk.py solution BoundedKnapsack/2.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.4. Increment register by product
# Input: A quantity register, coefficient, and result register.
# Goal: Add (quantity * coefficient) to result register.

from qiskit import QuantumCircuit
from typing import List

def increment_by_product(qc: QuantumCircuit, quantity: List[int], coefficient: int, result: List[int]) -> QuantumCircuit:
    """
    Add quantity * coefficient to result register.

    Args:
        qc: Quantum circuit to modify
        quantity: Qubit indices for quantity value
        coefficient: Classical coefficient to multiply
        result: Result register qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
