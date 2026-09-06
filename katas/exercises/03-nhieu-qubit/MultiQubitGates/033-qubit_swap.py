# ══════════════════════════════════════════════════════════════════════════════
# BÀI 033/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# tutorials/MultiQubitGates/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/MultiQubitGates/4
#   Gợi ý:      python qk.py hint tutorials/MultiQubitGates/4
#   Lời giải:   python qk.py solution tutorials/MultiQubitGates/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 4: Qubit Swap
# Input: An array of qubits in an arbitrary state.
# Goal: Swap the states of qubits at positions index1 and index2.

from qiskit import QuantumCircuit

def qubit_swap(qc: QuantumCircuit, qs: list, index1: int, index2: int) -> QuantumCircuit:
    """
    Swap the states of two qubits.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices
        index1: Index of first qubit to swap
        index2: Index of second qubit to swap

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
