# ══════════════════════════════════════════════════════════════════════════════
# BÀI 295/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# BoundedKnapsack/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BoundedKnapsack/1.1
#   Gợi ý:      python qk.py hint BoundedKnapsack/1.1
#   Lời giải:   python qk.py solution BoundedKnapsack/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. Read combination from a register
# Input: An array of n qubits, which are guaranteed to be in one of the 2ⁿ basis states.
# Output: The item combination that this state represents, expressed as a boolean array of length n.
#         The i-th element of the array should be true (indicating that i-th item is selected)
#         if and only if the i-th qubit of the register is in the |1⟩ state.
#         The operation should not change the state of the qubits.
# Example: For n = 3 and the qubits state |101⟩, return [true, false, true].

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import List

def measure_combination01(selected_items: List[int]) -> List[bool]:
    """
    Read combination from a register of qubits in computational basis states.

    Args:
        selected_items: List of qubit states (0 or 1) representing the register

    Returns:
        Boolean array where True indicates the i-th item is selected (qubit in |1⟩ state)
    """
    # Your code here
    pass
