# ══════════════════════════════════════════════════════════════════════════════
# BÀI 070/350  ·  Bậc 4 · Đo lường
# Measurements/1.9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.9
#   Gợi ý:      python qk.py hint Measurements/1.9
#   Lời giải:   python qk.py solution Measurements/1.9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.9. Distinguish two superposition states given by two arrays of bit strings
# Inputs:
#     1) N qubits which are guaranteed to be
#        in one of the two superposition states described by the given arrays of bit strings.
#     2) two arrays of bit strings represented as lists of lists of booleans.
#        The arrays describe the superposition states in the same way as in the previous task,
#        i.e., they have dimensions M₁ × N and M₂ × N respectively, N being the number of qubits.
#
# Output: 0 if qubits were in the superposition state described by the first array,
#         1 if they were in the superposition state described by the second array.
# The state of the qubits at the end of the operation does not matter.
#
# You can use as many measurements as you wish.
# The only constraint on the bit strings is that all bit strings in the two arrays are distinct.
#
# Example: for arrays [[False, True, False], [False, False, True]] and [[True, True, True], [False, True, True]]
#          return 0 corresponds to state (|010⟩ + |001⟩) / sqrt(2),
#          return 1 corresponds to state (|111⟩ + |011⟩) / sqrt(2)

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def superposition_measurement(qc: QuantumCircuit, qs: list, bits1: list, bits2: list) -> int:
    """
    Distinguish between two superposition states using multiple measurements.

    Args:
        qc: Quantum circuit containing the superposition state
        qs: List of qubit indices
        bits1: First array of bit strings (list of lists of booleans)
        bits2: Second array of bit strings (list of lists of booleans)

    Returns:
        0 if qubits were in superposition described by bits1,
        1 if qubits were in superposition described by bits2
    """
    # Your code here
    pass
