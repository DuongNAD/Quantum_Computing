# ══════════════════════════════════════════════════════════════════════════════
# BÀI 305/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/2.3
#   Gợi ý:      python qk.py hint BoundedKnapsack/2.3
#   Lời giải:   python qk.py solution BoundedKnapsack/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. Verify limits satisfaction
# Input: Quantity qubits and item limits.
# Goal: Check if all quantities are within their limits.

from qiskit import QuantumCircuit
from typing import List

def verify_limits_satisfaction(qc: QuantumCircuit, jagged: List[List[int]], limits: List[int], target: int) -> QuantumCircuit:
    """
    Verify all item quantities are within limits.

    Args:
        qc: Quantum circuit to modify
        jagged: Jagged array of quantity qubit indices
        limits: Maximum quantity for each item
        target: Target qubit to flip if all limits satisfied

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
