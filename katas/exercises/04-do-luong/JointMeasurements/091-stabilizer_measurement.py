# ══════════════════════════════════════════════════════════════════════════════
# BÀI 091/350  ·  Bậc 4 · Đo lường
# JointMeasurements/12
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/12
#   Gợi ý:      python qk.py hint JointMeasurements/12
#   Lời giải:   python qk.py solution JointMeasurements/12
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 12. Stabilizer measurement
# Input: A quantum circuit and qubit indices for a stabilizer measurement.
# Goal: Measure a ZZ stabilizer on two qubits using an ancilla.
# This is a non-destructive measurement that preserves the logical state.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def stabilizer_measurement(qc: QuantumCircuit, q1: int, q2: int, ancilla: int) -> bool:
    """
    Measure ZZ stabilizer using ancilla qubit.

    Args:
        qc: Quantum circuit
        q1: First data qubit
        q2: Second data qubit
        ancilla: Ancilla qubit for measurement

    Returns:
        Stabilizer measurement result (True for -1 eigenvalue)
    """
    # Your code here
    pass
