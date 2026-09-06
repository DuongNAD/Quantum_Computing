# ══════════════════════════════════════════════════════════════════════════════
# BÀI 281/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/4
#   Gợi ý:      python qk.py hint GraphColoring/4
#   Lời giải:   python qk.py solution GraphColoring/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4. Check if two colors are equal
# Input: A quantum circuit with two color registers and a target qubit.
# Goal: Flip target if the two colors are equal.

from qiskit import QuantumCircuit

def colors_equal_oracle(qc: QuantumCircuit, color1: list, color2: list, target: int) -> QuantumCircuit:
    """
    Oracle that marks when two colors are equal.

    Args:
        qc: Quantum circuit to modify
        color1: List of 2 qubit indices for first color
        color2: List of 2 qubit indices for second color
        target: Target qubit to flip if colors equal

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
