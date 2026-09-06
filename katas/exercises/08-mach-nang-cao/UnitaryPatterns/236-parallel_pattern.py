# ══════════════════════════════════════════════════════════════════════════════
# BÀI 236/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/15
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/15
#   Gợi ý:      python qk.py hint UnitaryPatterns/15
#   Lời giải:   python qk.py solution UnitaryPatterns/15
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 15. Parallel gate pattern
# Input: A quantum circuit qc and a list of qubit indices.
# Goal: Apply Hadamard gates to all specified qubits in parallel.
# In quantum circuits, gates on different qubits can be applied simultaneously.

from qiskit import QuantumCircuit
from typing import List

def parallel_pattern(qc: QuantumCircuit, qubits: List[int]) -> QuantumCircuit:
    """
    Apply H gates to all qubits in parallel.

    Args:
        qc: Quantum circuit to modify
        qubits: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
