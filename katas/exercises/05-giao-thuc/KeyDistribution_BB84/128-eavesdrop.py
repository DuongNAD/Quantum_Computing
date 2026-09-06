# ══════════════════════════════════════════════════════════════════════════════
# BÀI 128/350  ·  Bậc 5 · Giao thức lượng tử
# KeyDistribution_BB84/3.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run KeyDistribution_BB84/3.1
#   Gợi ý:      python qk.py hint KeyDistribution_BB84/3.1
#   Lời giải:   python qk.py solution KeyDistribution_BB84/3.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.1. Eavesdrop!
# In this task you implement an eavesdropper, Eve. Eve intercepts a qubit from
# the quantum channel between Alice and Bob. She measures it in either the
# |0⟩/|1⟩ basis or the |+⟩/|-⟩ basis, and prepares a new qubit in the state
# she measured. Then she sends the new qubit to Bob.
#
# Eve hopes that if she guesses the basis correctly, Bob won't detect an error.
#
# Inputs:
#      1) "qc": quantum circuit with a qubit in one of: |0⟩, |1⟩, |+⟩ or |-⟩,
#      2) "qubit": index of the qubit to eavesdrop on,
#      3) "basis": Eve's guess of the basis (False for |0⟩/|1⟩, True for |+⟩/|-⟩).
# Output: the bit encoded in the qubit (False for |0⟩/|+⟩ states, True for |1⟩/|-⟩ states).
# Note: In this simplified version, you're guaranteed the basis matches the qubit's
#       preparation basis. In reality, Eve has to guess.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def eavesdrop(qc: QuantumCircuit, qubit: int, basis: bool) -> bool:
    """
    Eve's eavesdropping operation on a single qubit.

    Args:
        qc: Quantum circuit containing the qubit to eavesdrop
        qubit: Index of qubit to eavesdrop on
        basis: Eve's chosen measurement basis (False=computational, True=diagonal)

    Returns:
        Measured bit value (False=0, True=1)
    """
    # Your code here
    pass
