# ══════════════════════════════════════════════════════════════════════════════
# BÀI 063/350  ·  Bậc 4 · Đo lường
# Measurements/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.2
#   Gợi ý:      python qk.py hint Measurements/1.2
#   Lời giải:   python qk.py solution Measurements/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. Set qubit to |0⟩ state
# Input: a qubit in an arbitrary state.
# Goal: change the state of the qubit to |0⟩.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def initialize_qubit(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Initialize a qubit to |0⟩ state by measurement and conditional flip.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to initialize

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
