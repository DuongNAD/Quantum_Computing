# ══════════════════════════════════════════════════════════════════════════════
# BÀI 288/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/11
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/11
#   Gợi ý:      python qk.py hint GraphColoring/11
#   Lời giải:   python qk.py solution GraphColoring/11
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 11. Single Grover iteration for graph coloring
# Input: A quantum circuit with colors and graph structure.
# Goal: Perform one complete Grover iteration (oracle + diffusion).

from qiskit import QuantumCircuit

def grover_iteration(qc: QuantumCircuit, colors: list, edges: list) -> QuantumCircuit:
    """
    Perform one Grover iteration for graph coloring search.

    Args:
        qc: Quantum circuit with color superposition
        colors: List of color register lists for each vertex
        edges: List of edges as (v1, v2) tuples

    Returns:
        Modified quantum circuit after one iteration
    """
    # Your code here
    pass
