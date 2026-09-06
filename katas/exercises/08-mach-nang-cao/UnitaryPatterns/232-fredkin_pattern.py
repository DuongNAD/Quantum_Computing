# ══════════════════════════════════════════════════════════════════════════════
# BÀI 232/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/11
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/11
#   Gợi ý:      python qk.py hint UnitaryPatterns/11
#   Lời giải:   python qk.py solution UnitaryPatterns/11
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 11. Fredkin gate pattern
# Input: A quantum circuit qc, control qubit c, and two target qubits t1 and t2.
# Goal: Apply the Fredkin gate (CSWAP, controlled-SWAP).
# Swaps t1 and t2 only if control qubit c is |1⟩.

from qiskit import QuantumCircuit

def fredkin_pattern(qc: QuantumCircuit, c: int, t1: int, t2: int) -> QuantumCircuit:
    """
    Apply Fredkin (CSWAP) gate.

    Args:
        qc: Quantum circuit to modify
        c: Control qubit index
        t1: First target qubit index
        t2: Second target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
