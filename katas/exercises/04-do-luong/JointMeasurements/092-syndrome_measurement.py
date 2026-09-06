# ══════════════════════════════════════════════════════════════════════════════
# BÀI 092/350  ·  Bậc 4 · Đo lường
# JointMeasurements/13
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/13
#   Gợi ý:      python qk.py hint JointMeasurements/13
#   Lời giải:   python qk.py solution JointMeasurements/13
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 13. Syndrome measurement for bit flip code
# Input: A quantum circuit with 3 data qubits and 2 ancilla qubits.
# Goal: Measure the syndrome to detect single bit flip errors.
# Returns a tuple (s1, s2) indicating the syndrome bits.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from typing import Tuple

def syndrome_measurement(qc: QuantumCircuit, data: list, ancilla: list) -> Tuple[bool, bool]:
    """
    Measure bit flip error syndrome.

    Args:
        qc: Quantum circuit
        data: List of 3 data qubit indices
        ancilla: List of 2 ancilla qubit indices

    Returns:
        Tuple of syndrome bits (s1, s2)
    """
    # Your code here
    pass
