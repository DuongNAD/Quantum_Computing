# ══════════════════════════════════════════════════════════════════════════════
# BÀI 227/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/6
#   Gợi ý:      python qk.py hint UnitaryPatterns/6
#   Lời giải:   python qk.py solution UnitaryPatterns/6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 6. Phase gate pattern
# Input: A quantum circuit qc and a qubit index q.
# Goal: Apply the S gate (phase gate, π/2 rotation around Z).
# The S gate transforms |0⟩ → |0⟩ and |1⟩ → i|1⟩.

from qiskit import QuantumCircuit

def phase_pattern(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply S (phase) gate to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply S gate

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
