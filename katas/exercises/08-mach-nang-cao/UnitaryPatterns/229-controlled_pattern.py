# ══════════════════════════════════════════════════════════════════════════════
# BÀI 229/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/8
#   Gợi ý:      python qk.py hint UnitaryPatterns/8
#   Lời giải:   python qk.py solution UnitaryPatterns/8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 8. Controlled gate pattern
# Input: A quantum circuit qc, control qubit index c, and target qubit index t.
# Goal: Apply a controlled-X (CNOT) gate.
# The CNOT flips the target qubit if and only if the control qubit is |1⟩.

from qiskit import QuantumCircuit

def controlled_pattern(qc: QuantumCircuit, c: int, t: int) -> QuantumCircuit:
    """
    Apply CNOT gate with control c and target t.

    Args:
        qc: Quantum circuit to modify
        c: Control qubit index
        t: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
