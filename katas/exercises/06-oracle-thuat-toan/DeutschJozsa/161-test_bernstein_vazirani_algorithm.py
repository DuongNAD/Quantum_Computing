# ══════════════════════════════════════════════════════════════════════════════
# BÀI 161/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/3.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/3.2
#   Gợi ý:      python qk.py hint DeutschJozsa/3.2
#   Lời giải:   python qk.py solution DeutschJozsa/3.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.2. Testing Bernstein-Vazirani algorithm
# Goal: use your implementation of Bernstein-Vazirani algorithm to figure out
# what bit vector the scalar product function oracle was using.
# As a reminder, this oracle creates an operation f(x) = Σᵢ rᵢ xᵢ modulo 2 for a given bit vector r,
# and Bernstein-Vazirani algorithm recovers that bit vector given the operation.

from qiskit import QuantumCircuit
from typing import Callable

def bv_algorithm_helper(N: int, uf_func: Callable[[QuantumCircuit, list[int], int], QuantumCircuit]) -> list[int]:
    """Helper BV algorithm implementation."""
    from qiskit_aer import AerSimulator

    qc = QuantumCircuit(N + 1, N)
    query = list(range(N))
    answer = N

    # State preparation
    for qubit in query:
        qc.h(qubit)
    qc.x(answer)
    qc.h(answer)

    # Apply oracle
    qc = uf_func(qc, query, answer)

    # Apply Hadamard to query register
    for qubit in query:
        qc.h(qubit)

    # Measure query register
    for i, qubit in enumerate(query):
        qc.measure(qubit, i)

    # Execute
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()

    measured_bits = list(counts.keys())[0]
    r = [int(bit) for bit in reversed(measured_bits)]

    return r

def oracle_product_function_bv(qc: QuantumCircuit, x: list[int], y: int, r: list[int]) -> QuantumCircuit:
    """Product function oracle for BV testing."""
    for i, bit in enumerate(r):
        if bit == 1:
            qc.cx(x[i], y)
    return qc

def oracle_kth_qubit(qc: QuantumCircuit, x: list[int], y: int, k: int) -> QuantumCircuit:
    """Oracle for k-th qubit function."""
    qc.cx(x[k], y)
    return qc

def test_bernstein_vazirani_algorithm() -> dict:
    """
    Test the Bernstein-Vazirani algorithm on various oracles.

    Returns:
        Dictionary with test results
    """
    # Your code here
    pass
