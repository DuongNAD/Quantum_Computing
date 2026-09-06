# ══════════════════════════════════════════════════════════════════════════════
# BÀI 139/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/4
#   Gợi ý:      python qk.py hint MarkingOracles/4
#   Lời giải:   python qk.py solution MarkingOracles/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4. Parity oracle
# Input: A quantum circuit, query register, and target qubit.
# Goal: Mark states with odd parity (odd number of |1⟩s in query register).

from qiskit import QuantumCircuit
from typing import List

def parity_oracle(qc: QuantumCircuit, query: List[int], target: int) -> QuantumCircuit:
    """
    Oracle that marks states with odd parity.

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
