# ══════════════════════════════════════════════════════════════════════════════
# BÀI 282/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/5
#   Gợi ý:      python qk.py hint GraphColoring/5
#   Lời giải:   python qk.py solution GraphColoring/5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 5. Check if two colors are different
# Input: A quantum circuit with two color registers and a target qubit.
# Goal: Flip target if the two colors are different (valid edge coloring).

from qiskit import QuantumCircuit

def colors_different_oracle(qc: QuantumCircuit, color1: list, color2: list, target: int) -> QuantumCircuit:
    """
    Oracle that marks when two colors are different.

    Args:
        qc: Quantum circuit to modify
        color1: List of 2 qubit indices for first color
        color2: List of 2 qubit indices for second color
        target: Target qubit to flip if colors different

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
