# ══════════════════════════════════════════════════════════════════════════════
# BÀI 069/350  ·  Bậc 4 · Đo lường
# Measurements/1.8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.8
#   Gợi ý:      python qk.py hint Measurements/1.8
#   Lời giải:   python qk.py solution Measurements/1.8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.8. Distinguish two superposition states given by two arrays of bit strings - 1 measurement
# Inputs:
#     1) N qubits which are guaranteed to be
#        in one of the two superposition states described by the given arrays of bit strings.
#     2) two arrays of bit strings represented as lists of lists of booleans.
#        The arrays have dimensions M₁ × N and M₂ × N respectively, where N is the number of
#        qubits and M₁ and M₂ are the numbers of bit strings in each array. Note that in general M₁ ≠ M₂.
#        An array of bit strings [b₁, ..., bₘ] defines a state that is
#        an equal superposition of all basis states defined by bit strings b₁, ..., bₘ.
#        For example, an array of bit strings [[False, True, False], [False, True, True]]
#        defines a superposition state (|010⟩ + |011⟩) / sqrt(2).
#
# Output: 0 if qubits were in the superposition state described by the first array,
#         1 if they were in the superposition state described by the second array.
# The state of the qubits at the end of the operation does not matter.
#
# You are allowed to use exactly one measurement.
# You are guaranteed that there exists an index of a qubit Q for which
#  - all the bit strings in the first array have the same value in this position (all bits1[j][Q] are the same),
#  - all the bit strings in the second array have the same value in this position (all bits2[j][Q] are the same),
#  - these values are different for the first and the second arrays.
#
# Example: for arrays [[False, True, False], [False, True, True]] and [[True, False, True], [False, False, True]]
#          return 0 corresponds to state (|010⟩ + |011⟩) / sqrt(2),
#          return 1 corresponds to state (|101⟩ + |001⟩) / sqrt(2),
#          and you can distinguish these states perfectly by measuring the second qubit.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def superposition_one_measurement(qc: QuantumCircuit, qs: list, bits1: list, bits2: list) -> int:
    """
    Distinguish between two superposition states using one measurement.

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
