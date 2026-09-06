# ══════════════════════════════════════════════════════════════════════════════
# BÀI 138/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/3
#   Gợi ý:      python qk.py hint MarkingOracles/3
#   Lời giải:   python qk.py solution MarkingOracles/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3. Arithmetic oracle - less than
# Input: A quantum circuit, query register encoding a number, and a threshold.
# Goal: Mark states where the query register value is less than threshold.
# The query register encodes an integer in little-endian binary.

from qiskit import QuantumCircuit
from typing import List

def arithmetic_oracle(qc: QuantumCircuit, query: List[int], target: int, threshold: int) -> QuantumCircuit:
    """
    Oracle that marks states where query < threshold.

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices (little-endian)
        target: Target qubit index
        threshold: Integer threshold value

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
