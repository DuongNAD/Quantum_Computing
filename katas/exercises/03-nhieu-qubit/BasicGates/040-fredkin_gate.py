# ══════════════════════════════════════════════════════════════════════════════
# BÀI 040/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# BasicGates/2.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/2.6
#   Gợi ý:      python qk.py hint BasicGates/2.6
#   Lời giải:   python qk.py solution BasicGates/2.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.6. Fredkin gate
# Input: Three qubits (stored in an array of length 3) in an arbitrary three-qubit state
#        α|000⟩ + β|001⟩ + γ|010⟩ + δ|011⟩ + ε|100⟩ + ζ|101⟩ + η|110⟩ + θ|111⟩.
# Goal: Swap the states of second and third qubit if and only if the state of the first qubit is |1⟩:
#        α|000⟩ + β|001⟩ + γ|010⟩ + δ|011⟩ + ε|100⟩ + η|101⟩ + ζ|110⟩ + θ|111⟩.

from qiskit import QuantumCircuit

def fredkin_gate(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Apply Fredkin (controlled-SWAP) gate: swap qubits 1 and 2 if qubit 0 is |1⟩.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices [control, target1, target2]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
