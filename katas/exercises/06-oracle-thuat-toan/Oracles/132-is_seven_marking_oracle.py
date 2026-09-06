# ══════════════════════════════════════════════════════════════════════════════
# BÀI 132/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# tutorials/Oracles/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/Oracles/1.3
#   Gợi ý:      python qk.py hint tutorials/Oracles/1.3
#   Lời giải:   python qk.py solution tutorials/Oracles/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3: IsSeven Marking Oracle
# Input:
#   - 3 qubits in an arbitrary superposition |x⟩ = Σ αᵢ|i⟩ (query register)
#   - 1 qubit in an arbitrary state |y⟩ (target qubit)
# Goal: Transform the qubits to the state Σ αᵢ|i⟩|y ⊕ f(i)⟩, where f(i) = 1 if i = 7, and 0 otherwise.
#       In other words, flip the target qubit if and only if the query register is in state |111⟩ (which represents 7 in binary).

from qiskit import QuantumCircuit

def is_seven_marking_oracle(qc: QuantumCircuit, query_qubits: list, target: int) -> QuantumCircuit:
    """
    Marking oracle that flips target qubit if query register represents 7.

    Args:
        qc: Quantum circuit to modify
        query_qubits: List of query register qubit indices [x0, x1, x2]
        target: Index of target qubit

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
