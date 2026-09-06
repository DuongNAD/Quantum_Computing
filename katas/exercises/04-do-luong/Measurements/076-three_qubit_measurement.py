# ══════════════════════════════════════════════════════════════════════════════
# BÀI 076/350  ·  Bậc 4 · Đo lường
# Measurements/1.15
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.15
#   Gợi ý:      python qk.py hint Measurements/1.15
#   Lời giải:   python qk.py solution Measurements/1.15
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.15**. Distinguish two orthogonal states on three qubits
# Input: Three qubits (stored in an array) which are guaranteed to be in either one of the
#        following two states:
#        1/sqrt(3) ( |100⟩ + ω |010⟩ + ω² |001⟩ ),
#        1/sqrt(3) ( |100⟩ + ω² |010⟩ + ω |001⟩ ).
#        Here ω = exp(2π i/3) denotes a primitive 3rd root of unity.
# Output: 0 if the qubits were in the first superposition,
#         1 if they were in the second superposition.
# The state of the qubits at the end of the operation does not matter.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np

def three_qubit_measurement(qc: QuantumCircuit, qs: list) -> int:
    """
    Distinguish between two orthogonal 3-qubit states with complex phases.

    Args:
        qc: Quantum circuit containing the 3-qubit state
        qs: List of three qubit indices

    Returns:
        0 for first state, 1 for second state
    """
    # Your code here
    pass
