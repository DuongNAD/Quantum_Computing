# ══════════════════════════════════════════════════════════════════════════════
# BÀI 283/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/6
#   Gợi ý:      python qk.py hint GraphColoring/6
#   Lời giải:   python qk.py solution GraphColoring/6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 6. Edge constraint oracle
# Input: A quantum circuit with vertex colors and an edge definition.
# Goal: Check if an edge satisfies the graph coloring constraint (endpoints have different colors).

from qiskit import QuantumCircuit
from typing import Tuple

def edge_constraint_oracle(qc: QuantumCircuit, vertex_colors: dict, edge: Tuple[int, int], target: int) -> QuantumCircuit:
    """
    Oracle that marks valid edge colorings (different colors at endpoints).

    Args:
        qc: Quantum circuit to modify
        vertex_colors: Dict mapping vertex index to list of color qubit indices
        edge: Tuple of (vertex1, vertex2) indices
        target: Target qubit to flip if constraint satisfied

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
