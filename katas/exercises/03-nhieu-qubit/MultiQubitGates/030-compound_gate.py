# ══════════════════════════════════════════════════════════════════════════════
# BÀI 030/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# tutorials/MultiQubitGates/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/MultiQubitGates/1
#   Gợi ý:      python qk.py hint tutorials/MultiQubitGates/1
#   Lời giải:   python qk.py solution tutorials/MultiQubitGates/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 1: Compound Gate
# Input: Three qubits in state |000⟩.
# Goal: Apply a compound operation: S gate to first qubit and Y gate to third qubit.

from qiskit import QuantumCircuit

def compound_gate(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Apply S gate to first qubit and Y gate to third qubit.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices [q0, q1, q2]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
