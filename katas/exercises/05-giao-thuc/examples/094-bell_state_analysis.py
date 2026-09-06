# ══════════════════════════════════════════════════════════════════════════════
# BÀI 094/350  ·  Bậc 5 · Giao thức lượng tử
# examples/BellStateAnalysis
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run examples/BellStateAnalysis
#   Gợi ý:      python qk.py hint examples/BellStateAnalysis
#   Lời giải:   python qk.py solution examples/BellStateAnalysis
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Bell State Analysis
# Goal: Analyze which of the four Bell states a given two-qubit state represents.
#       The four Bell states are: |φ+⟩, |φ-⟩, |Ψ+⟩, |Ψ-⟩.

from qiskit import QuantumCircuit

def bell_state_analysis(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Perform Bell state analysis to distinguish between four Bell states.

    Args:
        qc: Quantum circuit with qubits in one of the Bell states
        qubits: List of 2 qubit indices [q0, q1]

    Returns:
        Modified quantum circuit after Bell state analysis
    """
    # Your code here
    pass
