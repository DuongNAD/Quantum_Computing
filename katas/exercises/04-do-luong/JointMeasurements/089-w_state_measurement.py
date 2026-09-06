# ══════════════════════════════════════════════════════════════════════════════
# BÀI 089/350  ·  Bậc 4 · Đo lường
# JointMeasurements/10
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/10
#   Gợi ý:      python qk.py hint JointMeasurements/10
#   Lời giải:   python qk.py solution JointMeasurements/10
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 10. W state measurement
# Input: A quantum circuit with three qubits in a W state.
# Goal: Measure and verify W state properties.
# W state: (|001⟩ + |010⟩ + |100⟩)/√3 - exactly one qubit is |1⟩
# Returns True if exactly one qubit measures |1⟩.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def w_state_measurement(qc: QuantumCircuit, qubits: list) -> bool:
    """
    Measure W state and verify exactly one |1⟩.

    Args:
        qc: Quantum circuit with W state
        qubits: List of three qubit indices

    Returns:
        True if exactly one qubit is |1⟩
    """
    # Your code here
    pass
