# ══════════════════════════════════════════════════════════════════════════════
# BÀI 038/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# BasicGates/2.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/2.4
#   Gợi ý:      python qk.py hint BasicGates/2.4
#   Lời giải:   python qk.py solution BasicGates/2.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.4. Two-qubit gate - 4
# Input: Two qubits (stored in an array of length 2) in an arbitrary
#        two-qubit state α|00⟩ + β|01⟩ + γ|10⟩ + δ|11⟩.
# Goal: Change the two-qubit state to β|00⟩ + α|01⟩ + γ|10⟩ + δ|11⟩.
# Hint: This task can be solved using one library function;
# as an exercise, try to express the solution using several
# (possibly controlled) Pauli gates.

from qiskit import QuantumCircuit

def two_qubit_gate_4(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Swap amplitudes: α|00⟩+β|01⟩+γ|10⟩+δ|11⟩ -> β|00⟩+α|01⟩+γ|10⟩+δ|11⟩

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices [q0, q1]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
