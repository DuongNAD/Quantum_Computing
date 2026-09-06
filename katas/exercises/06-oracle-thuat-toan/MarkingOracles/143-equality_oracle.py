# ══════════════════════════════════════════════════════════════════════════════
# BÀI 143/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/8
#   Gợi ý:      python qk.py hint MarkingOracles/8
#   Lời giải:   python qk.py solution MarkingOracles/8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 8. Equality oracle
# Input: A quantum circuit, two query registers, and a target qubit.
# Goal: Mark states where the two registers contain equal values.

from qiskit import QuantumCircuit
from typing import List

def equality_oracle(qc: QuantumCircuit, reg_a: List[int], reg_b: List[int], target: int) -> QuantumCircuit:
    """
    Oracle that marks states where reg_a == reg_b.

    Args:
        qc: Quantum circuit to modify
        reg_a: First register qubit indices
        reg_b: Second register qubit indices
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
