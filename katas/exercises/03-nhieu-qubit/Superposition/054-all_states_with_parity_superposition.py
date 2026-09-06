# ══════════════════════════════════════════════════════════════════════════════
# BÀI 054/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.14
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.14
#   Gợi ý:      python qk.py hint Superposition/1.14
#   Lời giải:   python qk.py solution Superposition/1.14
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.14. Superposition of all bit strings of the given parity
# Inputs:
#      1) N qubits in |0..0⟩ state (stored in an array of length N).
#      2) An int "parity".
# Goal: change the state to an equal superposition of all basis states that have
#       an even number of 1s in them if "parity" = 0, or
#       an odd number of 1s in them if "parity" = 1.
# Example: for N = 2, the goal state would be (|00⟩ + |11⟩) / sqrt(2) if "parity" = 0,
#       and (|01⟩ + |10⟩) / sqrt(2) if "parity" = 1.

from qiskit import QuantumCircuit
from typing import List

def all_states_with_parity_superposition(qc: QuantumCircuit, qs: List[int], parity: int) -> QuantumCircuit:
    """
    Create superposition of all basis states with given parity.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices
        parity: 0 for even parity, 1 for odd parity

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
