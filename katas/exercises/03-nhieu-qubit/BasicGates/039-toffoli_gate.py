# ══════════════════════════════════════════════════════════════════════════════
# BÀI 039/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# BasicGates/2.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/2.5
#   Gợi ý:      python qk.py hint BasicGates/2.5
#   Lời giải:   python qk.py solution BasicGates/2.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.5. Toffoli gate
# Input: Three qubits (stored in an array of length 3) in an arbitrary three-qubit state
#        α|000⟩ + β|001⟩ + γ|010⟩ + δ|011⟩ + ε|100⟩ + ζ|101⟩ + η|110⟩ + θ|111⟩.
# Goal: Flip the state of the third qubit if the state of the first two is |11⟩:
#        i.e., change the three-qubit state to
#        α|000⟩ + β|001⟩ + γ|010⟩ + δ|011⟩ + ε|100⟩ + ζ|101⟩ + θ|110⟩ + η|111⟩.

from qiskit import QuantumCircuit

def toffoli_gate(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Apply Toffoli (CCNOT) gate: flip third qubit if first two are |11⟩.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices [control1, control2, target]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
