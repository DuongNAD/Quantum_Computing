# ══════════════════════════════════════════════════════════════════════════════
# BÀI 174/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# GroversAlgorithm/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GroversAlgorithm/1.4
#   Gợi ý:      python qk.py hint GroversAlgorithm/1.4
#   Lời giải:   python qk.py solution GroversAlgorithm/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4*. Oracle converter
# Input: A marking oracle that takes a register and target qubit, flipping target if register
#        satisfies a certain condition
# Output: A phase-flipping oracle that takes a register and flips the phase if it satisfies
#         the condition
# Note: Grover's algorithm uses phase-flipping oracles, but marking oracles are easier to write.
#       This converts a marking oracle to a phase-flipping oracle using the phase kickback trick.

from qiskit import QuantumCircuit
from typing import Callable

def oracle_converter(marking_oracle: Callable[[QuantumCircuit, list[int], int], QuantumCircuit]) -> Callable[[QuantumCircuit, list[int]], QuantumCircuit]:
    """
    Convert a marking oracle to a phase-flipping oracle.

    Args:
        marking_oracle: Function that applies marking oracle to (qc, query_register, target)

    Returns:
        Function that applies phase-flipping oracle to (qc, query_register)
    """
    def phase_flip_oracle(qc: QuantumCircuit, query_register: list[int]) -> QuantumCircuit:
        # Your code here
        pass

    return phase_flip_oracle
