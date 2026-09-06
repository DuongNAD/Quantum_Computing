# ══════════════════════════════════════════════════════════════════════════════
# BÀI 298/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/1.4
#   Gợi ý:      python qk.py hint BoundedKnapsack/1.4
#   Lời giải:   python qk.py solution BoundedKnapsack/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. Compare qubit array greater than integer
# Input: A qubit register encoding a number and a classical threshold.
# Goal: Flip target if register value > threshold.

from qiskit import QuantumCircuit
from typing import List

def compare_qubit_array_greater_than_int(qc: QuantumCircuit, register: List[int], threshold: int, target: int) -> QuantumCircuit:
    """
    Oracle that marks when register value > threshold.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices (little-endian)
        threshold: Integer threshold to compare against
        target: Target qubit to flip if condition met

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
