# ══════════════════════════════════════════════════════════════════════════════
# BÀI 148/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# tutorials/ExploringDeutschJozsaAlgorithm/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/ExploringDeutschJozsaAlgorithm/2
#   Gợi ý:      python qk.py hint tutorials/ExploringDeutschJozsaAlgorithm/2
#   Lời giải:   python qk.py solution tutorials/ExploringDeutschJozsaAlgorithm/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 2: Constant Function Oracle
# Goal: Implement an oracle for a constant function (always outputs 0 or always outputs 1).
#       Create an oracle that implements f(x) = 0 for all x.

from qiskit import QuantumCircuit

def constant_function_oracle(qc: QuantumCircuit, x: list, y: int) -> QuantumCircuit:
    """
    Oracle for constant function f(x) = 0.

    Args:
        qc: Quantum circuit to modify
        x: List of input qubit indices
        y: Output qubit index

    Returns:
        Modified quantum circuit (unchanged for f(x) = 0)
    """
    # Your code here
    pass
