# ══════════════════════════════════════════════════════════════════════════════
# BÀI 147/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# tutorials/ExploringDeutschJozsaAlgorithm/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/ExploringDeutschJozsaAlgorithm/1
#   Gợi ý:      python qk.py hint tutorials/ExploringDeutschJozsaAlgorithm/1
#   Lời giải:   python qk.py solution tutorials/ExploringDeutschJozsaAlgorithm/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 1: Balanced Function Oracle
# Goal: Implement an oracle for a balanced function (outputs 0 for half inputs, 1 for other half).
#       Create an oracle that implements f(x) = x₀ ⊕ x₁ (XOR of two bits).

from qiskit import QuantumCircuit

def balanced_function_oracle(qc: QuantumCircuit, x: list, y: int) -> QuantumCircuit:
    """
    Oracle for balanced function f(x) = x₀ ⊕ x₁.

    Args:
        qc: Quantum circuit to modify
        x: List of input qubit indices [x0, x1]
        y: Output qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
