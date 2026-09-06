# ══════════════════════════════════════════════════════════════════════════════
# BÀI 173/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# GroversAlgorithm/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GroversAlgorithm/1.3
#   Gợi ý:      python qk.py hint GroversAlgorithm/1.3
#   Lời giải:   python qk.py solution GroversAlgorithm/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. Arbitrary bit pattern oracle
# Inputs:
#     1) N qubits in an arbitrary state |x⟩ (input/query register)
#     2) a qubit in an arbitrary state |y⟩ (target qubit)
#     3) a bit pattern of length N represented as list of bools
# Goal: Flip the state of the target qubit if the query register is in the state described
#       by the given bit pattern (True represents |1⟩, False represents |0⟩).
#       Leave the query register unchanged.
# Example: If pattern is [True, False], flip target iff qubits are in |10⟩ state.

from qiskit import QuantumCircuit

def oracle_arbitrary_pattern(qc: QuantumCircuit, query_register: list[int], target: int, pattern: list[bool]) -> QuantumCircuit:
    """
    Oracle that flips target if query register matches the given bit pattern.

    Args:
        qc: Quantum circuit to modify
        query_register: List of qubit indices for the query register
        target: Index of target qubit
        pattern: List of bools representing the target pattern (True=|1⟩, False=|0⟩)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
