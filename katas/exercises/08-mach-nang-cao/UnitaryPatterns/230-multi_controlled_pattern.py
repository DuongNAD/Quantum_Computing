# ══════════════════════════════════════════════════════════════════════════════
# BÀI 230/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/9
#   Gợi ý:      python qk.py hint UnitaryPatterns/9
#   Lời giải:   python qk.py solution UnitaryPatterns/9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 9. Multi-controlled gate pattern
# Input: A quantum circuit qc, list of control qubit indices, and target qubit index.
# Goal: Apply a multi-controlled X gate (MCX/Toffoli generalization).
# The target is flipped only if ALL control qubits are |1⟩.

from qiskit import QuantumCircuit
from typing import List

def multi_controlled_pattern(qc: QuantumCircuit, controls: List[int], target: int) -> QuantumCircuit:
    """
    Apply multi-controlled X gate.

    Args:
        qc: Quantum circuit to modify
        controls: List of control qubit indices
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
