# ══════════════════════════════════════════════════════════════════════════════
# BÀI 121/350  ·  Bậc 5 · Giao thức lượng tử
# KeyDistribution_BB84/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run KeyDistribution_BB84/1.2
#   Gợi ý:      python qk.py hint KeyDistribution_BB84/1.2
#   Lời giải:   python qk.py solution KeyDistribution_BB84/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. Equal superposition
# Input: A qubit in the |0⟩ state.
# Goal: Change the qubit state to a superposition state
#       that has equal probabilities of measuring 0 and 1.
# Note: This is not the same as keeping the qubit in the |0⟩ state with 50% probability
# and converting it to the |1⟩ state with 50% probability!
#
# Creating equal superposition is a fundamental operation in quantum computing
# and is essential for many quantum protocols including BB84.

from qiskit import QuantumCircuit

def equal_superposition(qc: QuantumCircuit, qubit: int) -> QuantumCircuit:
    """
    Create equal superposition state from |0⟩.

    Args:
        qc: Quantum circuit to modify
        qubit: Index of qubit to put in superposition

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
