import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    from qiskit import QuantumCircuit
    from qiskit_aer.primitives import SamplerV2
except ImportError:
    print("[!] Thong bao: Can cai dat Qiskit va Qiskit-Aer de chay script nay:")
    print("    pip install qiskit qiskit-aer")
    sys.exit(0)

qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

sampler = SamplerV2()
result = sampler.run([qc],shots=4096).result()
print(result[0].data.meas.get_counts())
print(qc.draw("text"))