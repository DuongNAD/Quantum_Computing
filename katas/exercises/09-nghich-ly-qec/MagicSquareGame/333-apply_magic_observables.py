# ══════════════════════════════════════════════════════════════════════════════
# BÀI 333/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/2.3
#   Gợi ý:      python qk.py hint MagicSquareGame/2.3
#   Lời giải:   python qk.py solution MagicSquareGame/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. Apply magic square observables
# Inputs:
#      1) A tuple representing an observable in a cell of a magic square, in the same format as in task 2.2.
#      2) A list of 2 qubit indices.
# Goal:   Apply the observable described by this tuple to the given qubits.
#
# For example, if the given tuple is (-1, [PauliX, PauliY]), you have to
# apply X to the first qubit, Y to the second qubit, and a global phase of -1 to the two-qubit state.

from qiskit import QuantumCircuit
from enum import Enum

class Pauli(Enum):
    I = "I"
    X = "X"
    Y = "Y"
    Z = "Z"

def apply_magic_observables(qc: QuantumCircuit, observable: tuple[int, list[Pauli]], qs: list[int]) -> QuantumCircuit:
    """
    Apply magic square observable to qubits.

    Args:
        qc: Quantum circuit to modify
        observable: Tuple of (sign, [pauli1, pauli2])
        qs: List of 2 qubit indices to apply observables to

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
