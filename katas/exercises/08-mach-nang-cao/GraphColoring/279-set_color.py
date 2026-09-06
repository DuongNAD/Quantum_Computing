# ══════════════════════════════════════════════════════════════════════════════
# BÀI 279/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/2
#   Gợi ý:      python qk.py hint GraphColoring/2
#   Lời giải:   python qk.py solution GraphColoring/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2. Set vertex color
# Input: A quantum circuit and a color value to set.
# Goal: Set the color qubits to represent the specified color.

from qiskit import QuantumCircuit

def set_color(qc: QuantumCircuit, color_qubits: list, color: int) -> QuantumCircuit:
    """
    Set qubit register to represent the given color.

    Args:
        qc: Quantum circuit to modify
        color_qubits: List of 2 qubit indices for the color
        color: Color value (0-3)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
