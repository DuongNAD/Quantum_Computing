# ══════════════════════════════════════════════════════════════════════════════
# BÀI 234/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/13
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/13
#   Gợi ý:      python qk.py hint UnitaryPatterns/13
#   Lời giải:   python qk.py solution UnitaryPatterns/13
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 13. Composite gate pattern
# Input: A quantum circuit qc and a qubit index q.
# Goal: Apply a composite operation: H followed by S followed by H.
# This creates the transformation equivalent to Rx(π/2) (up to global phase).

from qiskit import QuantumCircuit

def composite_pattern(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply composite H-S-H pattern to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
