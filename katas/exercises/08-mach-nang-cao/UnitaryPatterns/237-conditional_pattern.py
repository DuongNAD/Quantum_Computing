# ══════════════════════════════════════════════════════════════════════════════
# BÀI 237/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/16
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/16
#   Gợi ý:      python qk.py hint UnitaryPatterns/16
#   Lời giải:   python qk.py solution UnitaryPatterns/16
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 16. Conditional gate pattern
# Input: A quantum circuit qc, control qubit c, target qubit t, and a boolean condition.
# Goal: Apply X gate to target if condition is True, otherwise apply Z gate.
# This demonstrates classical conditioning in circuit construction.

from qiskit import QuantumCircuit

def conditional_pattern(qc: QuantumCircuit, q: int, apply_x: bool) -> QuantumCircuit:
    """
    Conditionally apply X or Z gate based on boolean flag.

    Args:
        qc: Quantum circuit to modify
        q: Qubit index
        apply_x: If True apply X, else apply Z

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
