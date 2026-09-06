# ══════════════════════════════════════════════════════════════════════════════
# BÀI 286/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/9
#   Gợi ý:      python qk.py hint GraphColoring/9
#   Lời giải:   python qk.py solution GraphColoring/9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 9. Phase oracle for graph coloring
# Input: A quantum circuit with vertex color superposition.
# Goal: Apply phase kickback to mark valid colorings with -1 phase.

from qiskit import QuantumCircuit

def graph_coloring_phase_oracle(qc: QuantumCircuit, colors: list, edges: list) -> QuantumCircuit:
    """
    Phase oracle that applies -1 to valid graph colorings.

    Args:
        qc: Quantum circuit with color superposition
        colors: List of color register lists for each vertex
        edges: List of edges as (v1, v2) tuples

    Returns:
        Modified quantum circuit with phase applied
    """
    # Your code here
    pass
