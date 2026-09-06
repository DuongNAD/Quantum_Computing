# ══════════════════════════════════════════════════════════════════════════════
# BÀI 342/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/4
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/4
#   Lời giải:   python qk.py solution QEC_BitFlipCode/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4. Measure syndrome
# Input: A quantum circuit with 3 data qubits and 2 syndrome qubits.
# Goal: Measure the error syndrome without collapsing the logical state.
# Syndrome (0,0): no error, (1,0): error on q0, (1,1): error on q1, (0,1): error on q2

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from typing import Tuple

def measure_syndrome(qc: QuantumCircuit, data: list, syndrome: list) -> Tuple[bool, bool]:
    """
    Measure error syndrome for bit flip code.

    Args:
        qc: Quantum circuit with encoded state
        data: List of 3 data qubit indices
        syndrome: List of 2 syndrome qubit indices

    Returns:
        Tuple of syndrome bits (s0, s1)
    """
    # Your code here
    pass
