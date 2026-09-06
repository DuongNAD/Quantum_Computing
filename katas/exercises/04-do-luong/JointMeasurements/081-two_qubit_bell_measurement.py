# ══════════════════════════════════════════════════════════════════════════════
# BÀI 081/350  ·  Bậc 4 · Đo lường
# JointMeasurements/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run JointMeasurements/2
#   Gợi ý:      python qk.py hint JointMeasurements/2
#   Lời giải:   python qk.py solution JointMeasurements/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2. Two qubit Bell measurement
# Input: A quantum circuit qc with two qubits in a Bell state.
# Goal: Perform a Bell measurement to distinguish the four Bell states.
# Returns an integer 0-3 indicating which Bell state: |Φ+⟩, |Φ-⟩, |Ψ+⟩, |Ψ-⟩.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def two_qubit_bell_measurement(qc: QuantumCircuit, q1: int, q2: int) -> int:
    """
    Perform Bell measurement on two qubits.

    Args:
        qc: Quantum circuit with Bell state
        q1: First qubit index
        q2: Second qubit index

    Returns:
        Integer 0-3 identifying the Bell state
    """
    # Your code here
    pass
