# ══════════════════════════════════════════════════════════════════════════════
# BÀI 223/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/2
#   Gợi ý:      python qk.py hint UnitaryPatterns/2
#   Lời giải:   python qk.py solution UnitaryPatterns/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2. Pauli X pattern
# Input: A quantum circuit qc and a qubit index q.
# Goal: Apply the Pauli X gate (NOT gate, bit flip) to the qubit.
# The X gate transforms |0⟩ → |1⟩ and |1⟩ → |0⟩.

from qiskit import QuantumCircuit

def pauli_x_pattern(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply Pauli X gate to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply X gate

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
