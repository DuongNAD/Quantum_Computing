# ══════════════════════════════════════════════════════════════════════════════
# BÀI 324/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# GHZGame/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GHZGame/2.1
#   Gợi ý:      python qk.py hint GHZGame/2.1
#   Lời giải:   python qk.py solution GHZGame/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. Entangled triple
# Input: A quantum circuit and three qubits initially in the |000⟩ state.
# Goal: Create the entangled state |Ψ⟩ = (|000⟩ - |011⟩ - |101⟩ - |110⟩) / 2 on these qubits.
#
# This is the GHZ-type entangled state that enables the quantum advantage.
# It's a superposition of states where an even number of qubits are in |1⟩.

from qiskit import QuantumCircuit
import numpy as np

def create_entangled_triple(qc: QuantumCircuit, qubits: list[int]) -> QuantumCircuit:
    """
    Create the GHZ-type entangled state |Ψ⟩ = (|000⟩ - |011⟩ - |101⟩ - |110⟩) / 2.

    Args:
        qc: Quantum circuit to modify
        qubits: List of three qubit indices [q0, q1, q2]

    Returns:
        Modified quantum circuit with entangled triple
    """
    # Your code here
    pass
