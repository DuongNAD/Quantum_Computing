# ══════════════════════════════════════════════════════════════════════════════
# BÀI 095/350  ·  Bậc 5 · Giao thức lượng tử
# examples/GroverSearch2Qubits
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run examples/GroverSearch2Qubits
#   Gợi ý:      python qk.py hint examples/GroverSearch2Qubits
#   Lời giải:   python qk.py solution examples/GroverSearch2Qubits
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Grover's Algorithm for 2 Qubits
# Goal: Implement Grover's search algorithm for finding a marked state in 2-qubit space.
#       Search for the state |11⟩ among {|00⟩, |01⟩, |10⟩, |11⟩}.

from qiskit import QuantumCircuit

def grover_search_2qubits(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Implement Grover's algorithm to find |11⟩ state.

    Args:
        qc: Quantum circuit
        qubits: List of 2 qubit indices [q0, q1]

    Returns:
        Modified quantum circuit after Grover iteration
    """
    # Your code here
    pass
