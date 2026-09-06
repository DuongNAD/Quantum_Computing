# ══════════════════════════════════════════════════════════════════════════════
# BÀI 140/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/5
#   Gợi ý:      python qk.py hint MarkingOracles/5
#   Lời giải:   python qk.py solution MarkingOracles/5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 5. Bit counting oracle
# Input: A quantum circuit, query register, target, and count threshold k.
# Goal: Mark states with exactly k ones in the query register.

from qiskit import QuantumCircuit
from typing import List

def bit_counting_oracle(qc: QuantumCircuit, query: List[int], target: int, k: int) -> QuantumCircuit:
    """
    Oracle that marks states with exactly k ones.

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices
        target: Target qubit index
        k: Number of ones to match

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
