# ══════════════════════════════════════════════════════════════════════════════
# BÀI 334/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/2.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/2.4
#   Gợi ý:      python qk.py hint MagicSquareGame/2.4
#   Lời giải:   python qk.py solution MagicSquareGame/2.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.4. Measure observables using joint measurement
# Inputs:
#      1) A tuple representing an observable in a cell of a magic square, in the same format as in task 2.2.
#      2) A 2-qubit register to measure the observable on.
#         The register is guaranteed to be in one of the eigenstates of the observable.
# Output: The result of measuring the observable on the given register:
#         0 if eigenvalue +1 has been measured, 1 if eigenvalue -1 has been measured.
# The state of the qubits at the end of the operation does not matter.
#
# Hint: Use joint measurement to measure the Pauli observables.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from enum import Enum

class Pauli(Enum):
    I = "I"
    X = "X"
    Y = "Y"
    Z = "Z"

def measure_observable(observable: tuple[int, list[Pauli]], qc: QuantumCircuit, target: list[int], classical_reg: list[int]) -> int:
    """
    Measure an observable on a 2-qubit register.

    Args:
        observable: Tuple of (sign, [pauli1, pauli2])
        qc: Quantum circuit to modify
        target: List of 2 target qubit indices
        classical_reg: List of 2 classical bit indices to store results

    Returns:
        0 if eigenvalue +1 measured, 1 if eigenvalue -1 measured
    """
    # Your code here - modify qc and return measurement interpretation
    pass
