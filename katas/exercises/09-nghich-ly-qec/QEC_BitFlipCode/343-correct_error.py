# ══════════════════════════════════════════════════════════════════════════════
# BÀI 343/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/5
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/5
#   Lời giải:   python qk.py solution QEC_BitFlipCode/5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 5. Correct bit flip error
# Input: A quantum circuit and syndrome measurement results.
# Goal: Apply correction based on syndrome to fix the bit flip error.
# Syndrome (0,0): no correction, (1,0): flip q0, (1,1): flip q1, (0,1): flip q2

from qiskit import QuantumCircuit
from typing import Tuple

def correct_error(qc: QuantumCircuit, data: list, syndrome: Tuple[bool, bool]) -> QuantumCircuit:
    """
    Correct bit flip error based on syndrome.

    Args:
        qc: Quantum circuit with encoded state
        data: List of 3 data qubit indices
        syndrome: Tuple of syndrome bits (s0, s1)

    Returns:
        Modified quantum circuit with corrected state
    """
    # Your code here
    pass
