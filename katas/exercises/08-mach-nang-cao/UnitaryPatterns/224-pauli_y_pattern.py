# ══════════════════════════════════════════════════════════════════════════════
# BÀI 224/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/3
#   Gợi ý:      python qk.py hint UnitaryPatterns/3
#   Lời giải:   python qk.py solution UnitaryPatterns/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3. Pauli Y pattern
# Input: A quantum circuit qc and a qubit index q.
# Goal: Apply the Pauli Y gate to the qubit.
# The Y gate transforms |0⟩ → i|1⟩ and |1⟩ → -i|0⟩.

from qiskit import QuantumCircuit

def pauli_y_pattern(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply Pauli Y gate to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply Y gate

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
