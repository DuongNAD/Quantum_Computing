# ══════════════════════════════════════════════════════════════════════════════
# BÀI 171/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# GroversAlgorithm/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GroversAlgorithm/1.1
#   Gợi ý:      python qk.py hint GroversAlgorithm/1.1
#   Lời giải:   python qk.py solution GroversAlgorithm/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. The |11...1⟩ oracle
# Inputs:
#     1) N qubits in an arbitrary state |x⟩ (input/query register)
#     2) a qubit in an arbitrary state |y⟩ (target qubit)
# Goal: Flip the state of the target qubit (apply X gate) if the query register is in |11...1⟩ state,
#       and leave it unchanged otherwise. Leave the query register unchanged.
# Example: If register is |00...0⟩, target unchanged. If register is |11...1⟩, flip target.

from qiskit import QuantumCircuit

def oracle_all_ones(qc: QuantumCircuit, query_register: list[int], target: int) -> QuantumCircuit:
    """
    Oracle that flips target if all qubits in query register are |1⟩.

    Args:
        qc: Quantum circuit to modify
        query_register: List of qubit indices for the query register
        target: Index of target qubit

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
