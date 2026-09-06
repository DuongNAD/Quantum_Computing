# ══════════════════════════════════════════════════════════════════════════════
# BÀI 144/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/9
#   Gợi ý:      python qk.py hint MarkingOracles/9
#   Lời giải:   python qk.py solution MarkingOracles/9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 9. OR oracle
# Input: A quantum circuit, query register, and target qubit.
# Goal: Mark states where at least one query qubit is |1⟩ (logical OR).

from qiskit import QuantumCircuit
from typing import List

def or_oracle(qc: QuantumCircuit, query: List[int], target: int) -> QuantumCircuit:
    """
    Oracle that marks states with at least one |1⟩ (OR function).

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
