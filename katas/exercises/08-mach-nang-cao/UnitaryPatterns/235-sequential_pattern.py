# ══════════════════════════════════════════════════════════════════════════════
# BÀI 235/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/14
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/14
#   Gợi ý:      python qk.py hint UnitaryPatterns/14
#   Lời giải:   python qk.py solution UnitaryPatterns/14
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 14. Sequential gate pattern
# Input: A quantum circuit qc, a list of qubit indices, and number of layers.
# Goal: Apply Hadamard gates to all qubits in sequence, repeated for n layers.

from qiskit import QuantumCircuit
from typing import List

def sequential_pattern(qc: QuantumCircuit, qubits: List[int], layers: int) -> QuantumCircuit:
    """
    Apply sequential H gates to all qubits for multiple layers.

    Args:
        qc: Quantum circuit to modify
        qubits: List of qubit indices
        layers: Number of layers to apply

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
