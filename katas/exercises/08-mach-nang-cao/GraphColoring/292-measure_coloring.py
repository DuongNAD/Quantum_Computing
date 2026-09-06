# ══════════════════════════════════════════════════════════════════════════════
# BÀI 292/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# GraphColoring/15
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GraphColoring/15
#   Gợi ý:      python qk.py hint GraphColoring/15
#   Lời giải:   python qk.py solution GraphColoring/15
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 15. Measure graph coloring result
# Input: A quantum circuit after Grover search.
# Goal: Measure and decode the vertex colorings.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from typing import List

def measure_coloring(qc: QuantumCircuit, num_vertices: int) -> List[int]:
    """
    Measure and decode graph coloring from quantum circuit.

    Args:
        qc: Quantum circuit with coloring state
        num_vertices: Number of vertices

    Returns:
        List of color values for each vertex
    """
    # Your code here
    pass
