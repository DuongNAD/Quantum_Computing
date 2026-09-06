# ══════════════════════════════════════════════════════════════════════════════
# BÀI 053/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.13
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.13
#   Gợi ý:      python qk.py hint Superposition/1.13
#   Lời giải:   python qk.py solution Superposition/1.13
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.13*. Superposition of four bit strings
# Inputs:
#      1) N qubits in |0...0⟩ state
#      2) four bit string represented as Bool[][] bits
#         bits is an array of size 4 x N array which describes the bit strings as follows:
#         bits[i] describes the i-th bit string and has N elements.
#         All four bit strings will be distinct.
#
# Goal: create an equal superposition of the four basis states given by the bit strings.
#
# Example: for N = 3 and bits = [[False, True, False], [True, False, False], [False, False, True], [True, True, False]]
#          the state you need to prepare is (|010⟩ + |100⟩ + |001⟩ + |110⟩) / 2.

from qiskit import QuantumCircuit

def four_bitstring_superposition(qc: QuantumCircuit, qubits: list, bits: list) -> QuantumCircuit:
    """
    Create equal superposition of four basis states given by bit strings.

    Args:
        qc: Quantum circuit to modify
        qubits: List of qubit indices
        bits: List of 4 bit strings, each represented as list of bool

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
