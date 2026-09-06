# ══════════════════════════════════════════════════════════════════════════════
# BÀI 133/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# tutorials/Oracles/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/Oracles/2.1
#   Gợi ý:      python qk.py hint tutorials/Oracles/2.1
#   Lời giải:   python qk.py solution tutorials/Oracles/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1: Convert Marking Oracle to Phase Oracle
# Input: A marking oracle and qubits to apply it to.
# Goal: Use phase kickback to convert a marking oracle into a phase oracle.
#       Apply the marking oracle using an ancilla in |-⟩ state to achieve phase kickback.

from qiskit import QuantumCircuit

def apply_marking_oracle_as_phase_oracle(qc: QuantumCircuit, qubits: list, marking_oracle_func) -> QuantumCircuit:
    """
    Convert marking oracle to phase oracle using phase kickback.

    Args:
        qc: Quantum circuit to modify
        qubits: List of query qubit indices
        marking_oracle_func: Function that applies marking oracle

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
