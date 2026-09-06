# ══════════════════════════════════════════════════════════════════════════════
# BÀI 088/350  ·  Bậc 4 · Đo lường
# JointMeasurements/9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/9
#   Gợi ý:      python qk.py hint JointMeasurements/9
#   Lời giải:   python qk.py solution JointMeasurements/9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 9. GHZ state measurement
# Input: A quantum circuit with three qubits in a GHZ state.
# Goal: Measure all three qubits and verify the GHZ correlation.
# GHZ state: (|000⟩ + |111⟩)/√2
# Returns True if measurement shows GHZ correlation (all same), False otherwise.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def ghz_measurement(qc: QuantumCircuit, qubits: list) -> bool:
    """
    Measure GHZ state and verify correlation.

    Args:
        qc: Quantum circuit with GHZ state
        qubits: List of three qubit indices

    Returns:
        True if all qubits measure the same value
    """
    # Your code here
    pass
