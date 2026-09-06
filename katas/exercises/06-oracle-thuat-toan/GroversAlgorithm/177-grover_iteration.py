# ══════════════════════════════════════════════════════════════════════════════
# BÀI 177/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# GroversAlgorithm/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GroversAlgorithm/2.3
#   Gợi ý:      python qk.py hint GroversAlgorithm/2.3
#   Lời giải:   python qk.py solution GroversAlgorithm/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. The Grover iteration
# Inputs:
#      1) N qubits in an arbitrary state |x⟩ (input/query register)
#      2) a phase-flipping oracle that takes an N-qubit register and flips
#         the phase of the state if the register is in the desired state.
# Goal:  Perform one Grover iteration.
#
# Hint: A Grover iteration consists of 4 steps:
#    1) apply the oracle
#    2) apply the Hadamard transform
#    3) perform a conditional phase shift
#    4) apply the Hadamard transform again

from qiskit import QuantumCircuit
from typing import List, Callable

def grover_iteration(qc: QuantumCircuit, register: List[int], oracle_func: Callable[[QuantumCircuit, List[int]], QuantumCircuit]) -> QuantumCircuit:
    """
    Perform one Grover iteration.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices
        oracle_func: Function that applies the phase-flipping oracle

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
