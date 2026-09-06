# ══════════════════════════════════════════════════════════════════════════════
# BÀI 159/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/2.3
#   Gợi ý:      python qk.py hint DeutschJozsa/2.3
#   Lời giải:   python qk.py solution DeutschJozsa/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. Testing Deutsch-Jozsa algorithm
# Goal: use your implementation of Deutsch-Jozsa algorithm to test
# each of the oracles for being constant or balanced.

from qiskit import QuantumCircuit
from typing import Callable

# Helper functions (simplified implementations)
def dj_state_prep(qc: QuantumCircuit, query: list[int], answer: int) -> QuantumCircuit:
    """Prepare initial state for DJ algorithm."""
    for qubit in query:
        qc.h(qubit)
    qc.x(answer)
    qc.h(answer)
    return qc

def dj_algorithm(N: int, uf_func: Callable[[QuantumCircuit, list[int], int], QuantumCircuit]) -> bool:
    """Deutsch-Jozsa algorithm implementation."""
    from qiskit_aer import AerSimulator

    qc = QuantumCircuit(N + 1, N)
    query = list(range(N))
    answer = N

    # State preparation
    qc = dj_state_prep(qc, query, answer)

    # Apply oracle
    qc = uf_func(qc, query, answer)

    # Final Hadamards on query register
    for qubit in query:
        qc.h(qubit)

    # Measure query register
    for i, qubit in enumerate(query):
        qc.measure(qubit, i)

    # Simulate
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()

    # If all measurements are 0, function is constant
    measured = list(counts.keys())[0]
    return all(bit == '0' for bit in measured)

def oracle_product_function(qc: QuantumCircuit, x: list[int], y: int, r: list[int]) -> QuantumCircuit:
    """Helper oracle for product function."""
    for i, bit in enumerate(r):
        if bit == 1:
            qc.cx(x[i], y)
    return qc

def test_deutsch_jozsa_algorithm() -> dict:
    """
    Test the Deutsch-Jozsa algorithm on various oracles.

    Returns:
        Dictionary with test results
    """
    # Your code here
    pass
