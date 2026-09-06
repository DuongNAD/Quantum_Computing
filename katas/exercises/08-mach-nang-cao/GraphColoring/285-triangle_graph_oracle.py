# ══════════════════════════════════════════════════════════════════════════════
# BÀI 285/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/8
#   Gợi ý:      python qk.py hint GraphColoring/8
#   Lời giải:   python qk.py solution GraphColoring/8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 8. Triangle graph oracle
# Input: A quantum circuit with colors for 3 vertices forming a triangle.
# Goal: Check if the triangle coloring is valid (all 3 edges satisfied).

from qiskit import QuantumCircuit

def triangle_graph_oracle(qc: QuantumCircuit, colors: list, target: int) -> QuantumCircuit:
    """
    Oracle for 3-vertex triangle graph coloring.

    Args:
        qc: Quantum circuit to modify
        colors: List of 3 color register lists [[v0_bits], [v1_bits], [v2_bits]]
        target: Target qubit to flip if valid coloring

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
