# ══════════════════════════════════════════════════════════════════════════════
# BÀI 278/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/1
#   Gợi ý:      python qk.py hint GraphColoring/1
#   Lời giải:   python qk.py solution GraphColoring/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1. Read color from qubit register
# Input: A quantum circuit with qubits encoding a color (2 qubits per vertex for 4 colors).
# Goal: Understand how colors are encoded in the qubit register.
# Colors 0-3 are encoded as: 00, 01, 10, 11 in binary.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def read_color(qc: QuantumCircuit, color_qubits: list) -> int:
    """
    Read and return the color encoded in the qubit register.

    Args:
        qc: Quantum circuit with color qubits
        color_qubits: List of 2 qubit indices encoding the color

    Returns:
        Integer color value (0-3)
    """
    # Your code here
    pass
