# ══════════════════════════════════════════════════════════════════════════════
# BÀI 145/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# MarkingOracles/10
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MarkingOracles/10
#   Gợi ý:      python qk.py hint MarkingOracles/10
#   Lời giải:   python qk.py solution MarkingOracles/10
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 10. XOR oracle
# Input: A quantum circuit, two input qubits, and a target qubit.
# Goal: Compute XOR of the two inputs into the target.

from qiskit import QuantumCircuit

def xor_oracle(qc: QuantumCircuit, a: int, b: int, target: int) -> QuantumCircuit:
    """
    Oracle that computes XOR of two qubits into target.

    Args:
        qc: Quantum circuit to modify
        a: First input qubit index
        b: Second input qubit index
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
