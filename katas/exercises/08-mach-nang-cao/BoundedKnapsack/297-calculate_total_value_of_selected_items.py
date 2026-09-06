# ══════════════════════════════════════════════════════════════════════════════
# BÀI 297/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/1.3
#   Gợi ý:      python qk.py hint BoundedKnapsack/1.3
#   Lời giải:   python qk.py solution BoundedKnapsack/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. Calculate total value of selected items
# Input: Item values, selection qubits, and result register.
# Goal: Add values of selected items to result register.

from qiskit import QuantumCircuit
from typing import List

def calculate_total_value_of_selected_items(qc: QuantumCircuit, values: List[int], selection: List[int], result: List[int]) -> QuantumCircuit:
    """
    Add values of selected items to result register.

    Args:
        qc: Quantum circuit to modify
        values: List of item values
        selection: List of selection qubit indices
        result: List of result register qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
