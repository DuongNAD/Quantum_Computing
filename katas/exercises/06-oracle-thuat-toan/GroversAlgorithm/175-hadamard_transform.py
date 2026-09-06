# ══════════════════════════════════════════════════════════════════════════════
# BÀI 175/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# GroversAlgorithm/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GroversAlgorithm/2.1
#   Gợi ý:      python qk.py hint GroversAlgorithm/2.1
#   Lời giải:   python qk.py solution GroversAlgorithm/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. The Hadamard transform
# Input: A register of N qubits in an arbitrary state
# Goal: Apply the Hadamard transform to each of the qubits in the register.
# Note: If the register started in |0...0⟩, this will create equal superposition of all 2^N basis states.

from qiskit import QuantumCircuit

def hadamard_transform(qc: QuantumCircuit, register: list[int]) -> QuantumCircuit:
    """
    Apply Hadamard gate to all qubits in the register.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
