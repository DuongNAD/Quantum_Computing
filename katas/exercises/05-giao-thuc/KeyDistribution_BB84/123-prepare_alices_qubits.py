# ══════════════════════════════════════════════════════════════════════════════
# BÀI 123/350  ·  Bậc 5 · Giao thức lượng tử
# KeyDistribution_BB84/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run KeyDistribution_BB84/2.2
#   Gợi ý:      python qk.py hint KeyDistribution_BB84/2.2
#   Lời giải:   python qk.py solution KeyDistribution_BB84/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Prepare Alice's qubits
# Now Alice uses random bits to prepare her sequence of qubits to send to Bob.
# Inputs:
#      1) "qc": quantum circuit with N qubits in the |0⟩ states,
#      2) "qubits": list of N qubit indices,
#      3) "bases": a bool list of length N;
#         bases[i] indicates the basis to prepare the i-th qubit in:
#         - False: use |0⟩/|1⟩ (computational) basis
#         - True: use |+⟩/|-⟩ (Hadamard/diagonal) basis
#      4) "bits": a bool list of length N;
#         bits[i] indicates the bit to encode in the i-th qubit: False = 0, True = 1.
# Goal: Prepare the qubits in the described state.
#
# Alice's preparation is the encoding step of BB84 protocol.

from qiskit import QuantumCircuit
from typing import List

def prepare_alices_qubits(qc: QuantumCircuit, qubits: List[int], bases: List[bool], bits: List[bool]) -> QuantumCircuit:
    """
    Prepare Alice's qubits according to her chosen bases and bits.

    Args:
        qc: Quantum circuit to modify
        qubits: List of qubit indices to prepare
        bases: List indicating basis choice (False=computational, True=diagonal)
        bits: List indicating bit values to encode (False=0, True=1)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
