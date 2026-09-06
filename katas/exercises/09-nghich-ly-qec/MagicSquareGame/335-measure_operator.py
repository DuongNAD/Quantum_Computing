# ══════════════════════════════════════════════════════════════════════════════
# BÀI 335/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/2.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/2.5
#   Gợi ý:      python qk.py hint MagicSquareGame/2.5
#   Lời giải:   python qk.py solution MagicSquareGame/2.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.5. Measure an operator
# Inputs:
#      1) A quantum operation that acts on 2 qubits, has eigenvalues +1 and -1, and can be controlled.
#      2) A 2-qubit register to measure the operator on.
#         The register is guaranteed to be in one of the eigenstates of the operator.
# Output: The result of measuring the operator on the given register:
#         0 if eigenvalue +1 has been measured, 1 if eigenvalue -1 has been measured.
# The state of the qubits at the end of the operation does not matter.
#
# Hint: Applying the operator to an eigenstate will introduce a global phase equal to the eigenvalue.
#       Is there a way to convert this global phase into a relative phase?
# Hint: Remember that you can allocate extra qubits.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import Callable

def measure_operator(op_func: Callable[[QuantumCircuit, list[int]], QuantumCircuit],
                    target: list[int]) -> int:
    """
    Measure an operator on a 2-qubit register.

    Args:
        op_func: Function that applies the operator to a circuit and qubit list
        target: List of 2 target qubit indices (already in eigenstate)

    Returns:
        0 if eigenvalue +1 measured, 1 if eigenvalue -1 measured
    """
    # Your code here
    pass
