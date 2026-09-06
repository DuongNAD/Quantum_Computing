from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer.primitives import SamplerV2

sampler = SamplerV2()

def dem(qc, shots=4096):
    return sampler.run([qc], shots=shots).result()[0].data

# A — một cổng H
a = QuantumCircuit(1); a.h(0); a.measure_all()
print("A  H      ->", dem(a).meas.get_counts())
print(a.draw("text"))

# B — hai cổng H liên tiếp
b = QuantumCircuit(1); b.h(0); b.h(0); b.measure_all()
print("B  H,H    ->", dem(b).meas.get_counts())
print(b.draw("text"))

# C — H, đo giữa chừng, rồi H
q    = QuantumRegister(1, "q")
giua = ClassicalRegister(1, "giua")
cuoi = ClassicalRegister(1, "cuoi")
c = QuantumCircuit(q, giua, cuoi)
c.h(0); c.measure(0, giua[0]); c.h(0); c.measure(0, cuoi[0])
print("C  H,đo,H ->", dict(dem(c).cuoi.get_counts()))
print(c.draw("text"))