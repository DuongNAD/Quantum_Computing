"""
Test cho qsim.py — chạy:  pytest test_qsim.py -x -q

Test xếp theo đúng thứ tự MỐC trong qsim.py. Cờ -x làm pytest dừng ở lỗi đầu
tiên, nên bạn luôn biết chính xác việc kế tiếp cần làm là gì.

MỐC 5 (test_khop_qiskit_*) so simulator của bạn với qiskit-aer trên các mạch
ngẫu nhiên. Đó là bài kiểm tra thật sự — pass được nghĩa là xong Phase 1.
"""
import numpy as np
import pytest

import qsim as Q

TOL = 1e-10


# ══════════════════════════════════════════════════════════════════════════════
# MỐC 1 · ma trận cổng
# ══════════════════════════════════════════════════════════════════════════════
def test_moc1_ma_tran_da_dien():
    for ten in ("X", "Y", "Z", "H", "S", "T"):
        M = getattr(Q, ten)
        assert M is not None, f"{ten} vẫn còn None — điền ma trận đi"
        assert np.asarray(M).shape == (2, 2), f"{ten} phải là ma trận 2x2"


def test_moc1_cac_cong_deu_unitary():
    for ten in ("X", "Y", "Z", "H", "S", "T"):
        M = np.asarray(getattr(Q, ten), dtype=complex)
        assert np.allclose(M @ M.conj().T, np.eye(2), atol=TOL), \
            f"{ten} không unitary: U @ U† phải bằng I"


def test_moc1_hanh_vi_tung_cong():
    assert np.allclose(Q.X @ np.array([1, 0]), [0, 1]), "X|0> phải bằng |1>"
    assert np.allclose(Q.Z @ np.array([0, 1]), [0, -1]), "Z|1> phải bằng -|1>"
    assert np.allclose(Q.H @ np.array([1, 0]), [1 / np.sqrt(2)] * 2), "H|0> phải bằng |+>"
    assert np.allclose(Q.H @ Q.H, np.eye(2), atol=TOL), "H·H phải bằng I"
    assert np.allclose(Q.S @ Q.S, Q.Z, atol=TOL), "S·S phải bằng Z"
    assert np.allclose(Q.T @ Q.T, Q.S, atol=TOL), "T·T phải bằng S"


@pytest.mark.parametrize("theta", [0.0, 0.7, np.pi / 2, np.pi, 2.3])
def test_moc1_cong_quay(theta):
    for f in (Q.rx, Q.ry, Q.rz):
        M = np.asarray(f(theta), dtype=complex)
        assert M.shape == (2, 2)
        assert np.allclose(M @ M.conj().T, np.eye(2), atol=TOL), f"{f.__name__} không unitary"
    assert np.allclose(Q.rx(np.pi), -1j * Q.X, atol=TOL), "rx(pi) phải bằng -i·X"
    assert np.allclose(Q.ry(np.pi), -1j * Q.Y, atol=TOL), "ry(pi) phải bằng -i·Y"
    assert np.allclose(Q.rz(np.pi), -1j * Q.Z, atol=TOL), "rz(pi) phải bằng -i·Z"


def test_moc1_khoi_tao_trang_thai():
    s = Q.QSim(3)
    assert s.state is not None and len(s.state) == 8, "3 qubit phải có 2**3 = 8 biên độ"
    assert np.iscomplexobj(s.state), "state phải là mảng số phức"
    expect = np.zeros(8, dtype=complex); expect[0] = 1
    assert np.allclose(s.state, expect), "phải bắt đầu ở |000> "


# ══════════════════════════════════════════════════════════════════════════════
# MỐC 2 · áp cổng 1 qubit
# ══════════════════════════════════════════════════════════════════════════════
def test_moc2_x_tren_qubit_0():
    s = Q.QSim(2); s.x(0)
    expect = np.zeros(4, dtype=complex); expect[1] = 1      # |01> theo little-endian
    assert np.allclose(s.state, expect), "x(0) phải cho chỉ số 1, không phải 2"


def test_moc2_x_tren_qubit_1_kiem_tra_endian():
    s = Q.QSim(2); s.x(1)
    expect = np.zeros(4, dtype=complex); expect[2] = 1
    assert np.allclose(s.state, expect), \
        "x(1) phải cho chỉ số 2. Ra chỉ số 1 nghĩa là bạn đang đảo ngược thứ tự qubit."


def test_moc2_h_tao_chong_chap():
    s = Q.QSim(1); s.h(0)
    assert np.allclose(s.state, [1 / np.sqrt(2), 1 / np.sqrt(2)])


def test_moc2_h_hai_lan_quay_ve_ban_dau():
    s = Q.QSim(3); s.h(1); s.h(1)
    expect = np.zeros(8, dtype=complex); expect[0] = 1
    assert np.allclose(s.state, expect, atol=TOL), "H·H = I, phải quay về |000>"


def test_moc2_giu_chuan_hoa():
    rng = np.random.default_rng(0)
    s = Q.QSim(4)
    for _ in range(30):
        s.apply_1q(Q.rx(float(rng.random() * 6)), int(rng.integers(0, 4)))
        s.h(int(rng.integers(0, 4)))
    assert abs(np.sum(np.abs(s.state) ** 2) - 1) < TOL, "tổng xác suất phải luôn bằng 1"


def test_moc2_khong_dung_ma_tran_day_du():
    """15 qubit = 32768 biên độ. Cách naive 2**n x 2**n sẽ treo/hết RAM ở đây."""
    s = Q.QSim(15)
    for q in range(15):
        s.h(q)
    assert abs(np.sum(np.abs(s.state) ** 2) - 1) < 1e-9


# ══════════════════════════════════════════════════════════════════════════════
# MỐC 3 · cổng 2 qubit
# ══════════════════════════════════════════════════════════════════════════════
def test_moc3_cnot_tren_trang_thai_co_ban():
    s = Q.QSim(2); s.x(0); s.cx(0, 1)          # |01> -> |11>
    expect = np.zeros(4, dtype=complex); expect[3] = 1
    assert np.allclose(s.state, expect)

    s = Q.QSim(2); s.cx(0, 1)                  # |00> không đổi
    expect = np.zeros(4, dtype=complex); expect[0] = 1
    assert np.allclose(s.state, expect)


def test_moc3_bell_state():
    s = Q.QSim(2); s.h(0); s.cx(0, 1)
    expect = np.zeros(4, dtype=complex)
    expect[0] = expect[3] = 1 / np.sqrt(2)
    assert np.allclose(s.state, expect, atol=TOL), \
        "Bell state phải là (|00> + |11>)/sqrt(2) — chỉ chỉ số 0 và 3 khác 0"


def test_moc3_cz_doi_xung():
    a = Q.QSim(2); a.h(0); a.h(1); a.cz(0, 1)
    b = Q.QSim(2); b.h(0); b.h(1); b.cz(1, 0)
    assert np.allclose(a.state, b.state, atol=TOL), "CZ phải đối xứng"


def test_moc3_cz_bang_h_cnot_h():
    a = Q.QSim(2); a.h(0); a.h(1); a.cz(0, 1)
    b = Q.QSim(2); b.h(0); b.h(1); b.h(1); b.cx(0, 1); b.h(1)
    assert np.allclose(a.state, b.state, atol=TOL), "CZ = H(t)·CNOT·H(t)"


def test_moc3_swap():
    s = Q.QSim(3); s.x(0); s.swap(0, 2)
    expect = np.zeros(8, dtype=complex); expect[4] = 1      # |100>
    assert np.allclose(s.state, expect, atol=TOL)


def test_moc3_swap_hai_lan_la_dong_nhat():
    rng = np.random.default_rng(3)
    s = Q.QSim(3)
    for q in range(3):
        s.ry(float(rng.random() * 3), q)
    before = s.state.copy()
    s.swap(0, 2); s.swap(0, 2)
    assert np.allclose(s.state, before, atol=TOL)


# ══════════════════════════════════════════════════════════════════════════════
# MỐC 4 · đo lường
# ══════════════════════════════════════════════════════════════════════════════
def test_moc4_xac_suat():
    s = Q.QSim(2); s.h(0); s.cx(0, 1)
    p = np.asarray(s.probabilities())
    assert np.allclose(p, [0.5, 0, 0, 0.5], atol=TOL)
    assert abs(p.sum() - 1) < TOL


def test_moc4_sample_dung_dinh_dang():
    s = Q.QSim(3); s.h(0); s.cx(0, 1)
    out = s.sample(shots=2000, seed=42)
    assert isinstance(out, dict) and sum(out.values()) == 2000
    for k in out:
        assert len(k) == 3, f"bitstring '{k}' phải dài đúng 3 ký tự"
    assert set(out) <= {"000", "011"}, \
        f"chỉ được xuất hiện '000' và '011', nhận được {sorted(out)}"


def test_moc4_sample_dung_ti_le():
    s = Q.QSim(1); s.ry(2 * np.arccos(np.sqrt(0.25)), 0)   # P(1) = 0.75
    out = s.sample(shots=20000, seed=7)
    assert abs(out.get("1", 0) / 20000 - 0.75) < 0.02


def test_moc4_do_lam_sap_trang_thai():
    s = Q.QSim(2); s.h(0); s.cx(0, 1)
    bit = s.measure(0, seed=1)
    assert bit in (0, 1)
    assert abs(np.sum(np.abs(s.state) ** 2) - 1) < TOL, \
        "sau khi đo phải CHUẨN HOÁ LẠI — tổng xác suất vẫn phải bằng 1"
    p = np.abs(s.state) ** 2
    if bit == 0:
        assert p[0] > 1 - TOL, "đo ra 0 thì trạng thái phải sập hẳn về |00>"
    else:
        assert p[3] > 1 - TOL, "đo ra 1 thì trạng thái phải sập hẳn về |11>"


def test_moc4_do_lai_ra_ket_qua_cu():
    s = Q.QSim(2); s.h(0); s.cx(0, 1)
    first = s.measure(0, seed=5)
    for _ in range(5):
        assert s.measure(0, seed=99) == first, "đo lại qubit đã đo phải ra kết quả cũ"


# ══════════════════════════════════════════════════════════════════════════════
# MỐC 5 · kiểm chứng chéo với qiskit-aer  ⟵ BÀI KIỂM TRA THẬT
# ══════════════════════════════════════════════════════════════════════════════
qiskit = pytest.importorskip("qiskit", reason="cần qiskit để kiểm chứng chéo")
from qiskit import QuantumCircuit                      # noqa: E402
from qiskit.quantum_info import Statevector            # noqa: E402

G1 = ["h", "x", "y", "z", "s", "t"]
ROT = ["rx", "ry", "rz"]
G2 = ["cx", "cz", "swap"]


def _mach_ngau_nhien(rng, n, do_dai):
    qc = QuantumCircuit(n)
    sim = Q.QSim(n)
    for _ in range(do_dai):
        r = rng.random()
        if r < 0.5 or n == 1:
            g = G1[int(rng.integers(0, len(G1)))]
            q = int(rng.integers(0, n))
            getattr(qc, g)(q); getattr(sim, g)(q)
        elif r < 0.75:
            g = ROT[int(rng.integers(0, 3))]
            q = int(rng.integers(0, n))
            th = float(rng.random() * 2 * np.pi)
            getattr(qc, g)(th, q); getattr(sim, g)(th, q)
        else:
            a, b = (int(v) for v in rng.choice(n, 2, replace=False))
            g = G2[int(rng.integers(0, 3))]
            getattr(qc, g)(a, b); getattr(sim, g)(a, b)
    return qc, sim


@pytest.mark.parametrize("seed", range(12))
def test_khop_qiskit_mach_ngau_nhien(seed):
    """12 mạch ngẫu nhiên — yêu cầu Phase 1 là ≥ 10 mạch."""
    rng = np.random.default_rng(seed)
    n = int(rng.integers(1, 6))
    qc, sim = _mach_ngau_nhien(rng, n, int(rng.integers(4, 16)))
    lech = np.max(np.abs(Statevector(qc).data - np.asarray(sim.state)))
    assert lech < TOL, (
        f"lệch {lech:.2e} so với Qiskit trên mạch {n} qubit.\n"
        f"Lệch cỡ 1e-1 trở lên thường là sai quy ước endian.\n"
        f"Lệch chỉ ở DẤU/PHA thường là do rz viết sai dạng.\n{qc}"
    )


def test_khop_qiskit_mach_lon():
    rng = np.random.default_rng(1234)
    qc, sim = _mach_ngau_nhien(rng, 10, 120)
    lech = np.max(np.abs(Statevector(qc).data - np.asarray(sim.state)))
    assert lech < 1e-9, f"lệch {lech:.2e} trên mạch 10 qubit / 120 cổng"
