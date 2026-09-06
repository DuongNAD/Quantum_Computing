# ══════════════════════════════════════════════════════════════════════════════
# BÀI 124/350  ·  Bậc 5 · Giao thức lượng tử
# KeyDistribution_BB84/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run KeyDistribution_BB84/2.3
#   Gợi ý:      python qk.py hint KeyDistribution_BB84/2.3
#   Lời giải:   python qk.py solution KeyDistribution_BB84/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. Measure Bob's qubits
# Bob receives Alice's qubits and measures them by randomly choosing a basis
# for each qubit measurement.
# Inputs:
#      1) "qc": quantum circuit with N qubits;
#         each qubit is in one of the states: |0⟩, |1⟩, |+⟩ or |-⟩.
#      2) "qubits": list of N qubit indices to measure,
#      3) "bases": a bool list of length N;
#         bases[i] indicates the basis to measure the i-th qubit in:
#         - False: use |0⟩/|1⟩ (computational) basis
#         - True: use |+⟩/|-⟩ (Hadamard/diagonal) basis
# Output: Measure each qubit in the corresponding basis and return a list of results
#         (encoding measurement result Zero as False and One as True).
#
# Bob's measurement is the key step where quantum information is converted to classical bits.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import List

def measure_bobs_qubits(qc: QuantumCircuit, qubits: List[int], bases: List[bool]) -> List[bool]:
    """
    Measure Bob's qubits in the specified bases.

    Args:
        qc: Quantum circuit containing the qubits to measure
        qubits: List of qubit indices to measure
        bases: List indicating measurement basis (False=computational, True=diagonal)

    Returns:
        List of measurement results (False=0, True=1)
    """
    # Your code here
    pass
