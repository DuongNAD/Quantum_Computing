# ══════════════════════════════════════════════════════════════════════════════
# BÀI 231/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/10
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/10
#   Gợi ý:      python qk.py hint UnitaryPatterns/10
#   Lời giải:   python qk.py solution UnitaryPatterns/10
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 10. Toffoli gate pattern
# Input: A quantum circuit qc, two control qubits c1 and c2, and target qubit t.
# Goal: Apply the Toffoli gate (CCX, controlled-controlled-X).
# The target is flipped only if both control qubits are |1⟩.

from qiskit import QuantumCircuit

def toffoli_pattern(qc: QuantumCircuit, c1: int, c2: int, t: int) -> QuantumCircuit:
    """
    Apply Toffoli (CCX) gate.

    Args:
        qc: Quantum circuit to modify
        c1: First control qubit index
        c2: Second control qubit index
        t: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
