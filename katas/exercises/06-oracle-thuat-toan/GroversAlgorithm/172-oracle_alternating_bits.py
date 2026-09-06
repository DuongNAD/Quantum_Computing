# ══════════════════════════════════════════════════════════════════════════════
# BÀI 172/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# GroversAlgorithm/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GroversAlgorithm/1.2
#   Gợi ý:      python qk.py hint GroversAlgorithm/1.2
#   Lời giải:   python qk.py solution GroversAlgorithm/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. The |1010...⟩ oracle
# Inputs:
#     1) N qubits in an arbitrary state |x⟩ (input/query register)
#     2) a qubit in an arbitrary state |y⟩ (target qubit)
# Goal: Flip the state of the target qubit if the query register is in the |1010...⟩ state;
#       that is, the state with alternating 1 and 0 values, with any number of qubits.
#       Leave the query register unchanged.
# Example: If register is |10101⟩, flip the target qubit.

from qiskit import QuantumCircuit

def oracle_alternating_bits(qc: QuantumCircuit, query_qubits: list[int], target: int) -> QuantumCircuit:
    """
    Oracle that flips target if query register is in alternating |1010...⟩ pattern.

    Args:
        qc: Quantum circuit to modify
        query_qubits: List of qubit indices for the query register
        target: Index of target qubit

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
