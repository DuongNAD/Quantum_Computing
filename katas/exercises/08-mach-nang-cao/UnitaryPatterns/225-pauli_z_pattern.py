# ══════════════════════════════════════════════════════════════════════════════
# BÀI 225/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/4
#   Gợi ý:      python qk.py hint UnitaryPatterns/4
#   Lời giải:   python qk.py solution UnitaryPatterns/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4. Pauli Z pattern
# Input: A quantum circuit qc and a qubit index q.
# Goal: Apply the Pauli Z gate (phase flip) to the qubit.
# The Z gate transforms |0⟩ → |0⟩ and |1⟩ → -|1⟩.

from qiskit import QuantumCircuit

def pauli_z_pattern(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply Pauli Z gate to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply Z gate

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
