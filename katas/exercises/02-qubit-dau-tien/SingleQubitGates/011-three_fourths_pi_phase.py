# ══════════════════════════════════════════════════════════════════════════════
# BÀI 011/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/SingleQubitGates/5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/SingleQubitGates/5
#   Gợi ý:      python qk.py hint tutorials/SingleQubitGates/5
#   Lời giải:   python qk.py solution tutorials/SingleQubitGates/5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 5: Three-fourths phase
# Input: A qubit in an arbitrary state |Ψ⟩ = α|0⟩ + β|1⟩.
# Goal: Use phase shift gates to apply a 3π/4 phase to the |1⟩ component.
#       Transform the state to α|0⟩ + βe^(3iπ/4)|1⟩.

from qiskit import QuantumCircuit
import numpy as np

def three_fourths_pi_phase(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply 3π/4 phase to |1⟩ component using phase gates.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply phase to

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
