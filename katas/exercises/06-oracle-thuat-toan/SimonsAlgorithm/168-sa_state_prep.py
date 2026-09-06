# ══════════════════════════════════════════════════════════════════════════════
# BÀI 168/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SimonsAlgorithm/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SimonsAlgorithm/2.1
#   Gợi ý:      python qk.py hint SimonsAlgorithm/2.1
#   Lời giải:   python qk.py solution SimonsAlgorithm/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. State preparation for Simon's algorithm
# Inputs:
#      1) N qubits in |0⟩ state (query register)
# Goal: create an equal superposition of all basis vectors from |0...0⟩ to |1...1⟩ on query register
# (i.e. the state (|0...0⟩ + ... + |1...1⟩) / sqrt(2ᴺ)).

from qiskit import QuantumCircuit

def sa_state_prep(qc: QuantumCircuit, query: list[int]) -> QuantumCircuit:
    """
    Prepare equal superposition state for Simon's algorithm.

    Args:
        qc: Quantum circuit to modify
        query: List of query register qubit indices

    Returns:
        Modified quantum circuit with superposition state
    """
    # Your code here
    pass
