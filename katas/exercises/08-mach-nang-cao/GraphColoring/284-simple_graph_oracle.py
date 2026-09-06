# ══════════════════════════════════════════════════════════════════════════════
# BÀI 284/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/7
#   Gợi ý:      python qk.py hint GraphColoring/7
#   Lời giải:   python qk.py solution GraphColoring/7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 7. Graph coloring oracle for simple graph
# Input: A quantum circuit with vertex colors for a 2-vertex graph.
# Goal: Check if entire graph coloring is valid (all edges satisfied).

from qiskit import QuantumCircuit
from typing import List, Tuple

def simple_graph_oracle(qc: QuantumCircuit, vertex_colors: dict, edges: List[Tuple[int, int]], target: int) -> QuantumCircuit:
    """
    Oracle that marks valid graph colorings for a simple graph with a single edge. (For multi-edge graphs, use the ancilla-based construction in task 17.)

    Args:
        qc: Quantum circuit to modify
        vertex_colors: Dict mapping vertex index to color qubit indices
        edges: List of edges as (v1, v2) tuples
        target: Target qubit to flip if all constraints satisfied

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
