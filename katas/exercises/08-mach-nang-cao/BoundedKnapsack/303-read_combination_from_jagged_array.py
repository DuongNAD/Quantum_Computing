# ══════════════════════════════════════════════════════════════════════════════
# BÀI 303/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/2.1
#   Gợi ý:      python qk.py hint BoundedKnapsack/2.1
#   Lời giải:   python qk.py solution BoundedKnapsack/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. Read combination from jagged array
# Input: A jagged array of qubit indices representing item quantities.
# Goal: Read the quantity values for bounded knapsack.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from typing import List

def read_combination_from_jagged_array(qc: QuantumCircuit, jagged: List[List[int]]) -> List[int]:
    """
    Read quantities from jagged qubit array.

    Args:
        qc: Quantum circuit with quantity qubits set
        jagged: List of qubit index lists for each item's quantity

    Returns:
        List of quantity values for each item
    """
    # Your code here
    pass
