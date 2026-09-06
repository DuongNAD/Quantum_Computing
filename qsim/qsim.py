"""
qsim — simulator state-vector tự viết bằng NumPy.  ⟵ ĐÂY LÀ BÀI CỦA BẠN

Deliverable Phase 1: file này chạy đúng và khớp qiskit-aer trên ≥ 10 mạch ngẫu nhiên.

Cách làm:
    1. Đọc TODO theo thứ tự MỐC 1 → MỐC 5, đừng nhảy cóc.
    2. Sau mỗi TODO chạy:  pytest test_qsim.py -x -q
    3. Test đầu tiên chuyển xanh thì làm tiếp cái sau.

╔══════════════════════════════════════════════════════════════════════════════╗
║ QUY ƯỚC LITTLE-ENDIAN — CHỐT NGAY, GHI VÀO ĐẦU, ĐỪNG ĐỔI GIỮA CHỪNG        ║
║                                                                              ║
║ Qubit q là bit thứ q (tính từ phải) của chỉ số cơ sở.                        ║
║   chỉ số 6 = 110₂  →  q0=0, q1=1, q2=1                                       ║
║ Kiểm tra qubit q của chỉ số i:      (i >> q) & 1                             ║
║ Lật qubit q của chỉ số i:            i ^ (1 << q)                            ║
║                                                                              ║
║ Đây là quy ước Qiskit dùng. Nếu simulator của bạn ra '10' còn Qiskit ra      ║
║ '01' thì bạn KHÔNG sai vật lý — bạn sai quy ước.                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import numpy as np

# ══════════════════════════════════════════════════════════════════════════════
# MỐC 1 (Ngày 1–2) · Ma trận cổng 1 qubit
# ══════════════════════════════════════════════════════════════════════════════
# TODO 1.1 — điền các ma trận 2×2 dưới đây, dtype=complex.
#            Gợi ý kiểm tra: mọi ma trận phải unitary, tức U @ U.conj().T == I.

I2 = np.eye(2, dtype=complex)

X = None      # TODO: [[0,1],[1,0]] — cổng NOT
Y = None      # TODO: chứa ±1j
Z = None      # TODO: giữ |0>, đổi dấu |1>
H = None      # TODO: [[1,1],[1,-1]] / sqrt(2)
S = None      # TODO: phase gate, |1> -> i|1>
T = None      # TODO: |1> -> exp(i·pi/4)|1>


def rx(theta: float) -> np.ndarray:
    """Quay quanh trục X góc theta.  [[cos(θ/2), -i·sin(θ/2)], [-i·sin(θ/2), cos(θ/2)]]"""
    raise NotImplementedError("TODO 1.2")


def ry(theta: float) -> np.ndarray:
    """Quay quanh trục Y góc theta. Ma trận này THỰC, không có phần ảo."""
    raise NotImplementedError("TODO 1.3")


def rz(theta: float) -> np.ndarray:
    """Quay quanh trục Z góc theta. Ma trận chéo: exp(∓i·θ/2).

    Cẩn thận: nhiều tài liệu viết rz = diag(1, exp(iθ)) — bản đó lệch pha toàn cục
    so với Qiskit. Muốn khớp test thì dùng dạng đối xứng diag(e^{-iθ/2}, e^{+iθ/2}).
    """
    raise NotImplementedError("TODO 1.4")


class QSim:
    """Simulator state-vector cho n qubit.

    state là mảng 2**n số phức. state[i] là biên độ của trạng thái cơ sở |i>.
    """

    def __init__(self, n: int):
        self.n = n
        # TODO 1.5 — khởi tạo state ở |00...0>:
        #            mảng 2**n phần tử complex, toàn 0 trừ phần tử đầu bằng 1.
        self.state: np.ndarray = None
        raise NotImplementedError("TODO 1.5")

    # ══════════════════════════════════════════════════════════════════════════
    # MỐC 2 (Ngày 3–4) · Áp cổng 1 qubit
    # ══════════════════════════════════════════════════════════════════════════
    def apply_1q(self, U: np.ndarray, t: int) -> "QSim":
        """Áp ma trận 2×2 U lên qubit t.

        ĐỪNG dựng ma trận 2**n × 2**n rồi nhân — cách đó tốn O(4**n) và sẽ chết
        ở ~12 qubit. Thay vào đó ghép CẶP biên độ:

            với mọi chỉ số i mà bit t của i bằng 0:
                j = i + 2**t          (cùng chỉ số đó nhưng bit t bằng 1)
                (state[i], state[j]) = (U[0,0]*state[i] + U[0,1]*state[j],
                                        U[1,0]*state[i] + U[1,1]*state[j])

        Cách này là O(2**n) mỗi cổng. Nhớ đọc a, b ra biến tạm TRƯỚC khi ghi đè,
        nếu không bạn sẽ dùng giá trị đã bị sửa.
        """
        raise NotImplementedError("TODO 2.1")

    # cổng tiện dụng — làm xong apply_1q là mấy cái này chạy luôn
    def x(self, q): return self.apply_1q(X, q)
    def y(self, q): return self.apply_1q(Y, q)
    def z(self, q): return self.apply_1q(Z, q)
    def h(self, q): return self.apply_1q(H, q)
    def s(self, q): return self.apply_1q(S, q)
    def t(self, q): return self.apply_1q(T, q)
    def rx(self, theta, q): return self.apply_1q(rx(theta), q)
    def ry(self, theta, q): return self.apply_1q(ry(theta), q)
    def rz(self, theta, q): return self.apply_1q(rz(theta), q)

    # ══════════════════════════════════════════════════════════════════════════
    # MỐC 3 (Ngày 5–6) · Cổng 2 qubit — chỗ entanglement thật sự xuất hiện
    # ══════════════════════════════════════════════════════════════════════════
    def cx(self, c: int, t: int) -> "QSim":
        """CNOT: lật qubit t, chỉ với những chỉ số có bit c bằng 1.

        Duyệt mọi chỉ số i. Nếu bit c của i là 1 VÀ bit t của i là 0 thì
        hoán đổi state[i] với state[i lật bit t]. Điều kiện "bit t bằng 0"
        để mỗi cặp chỉ bị đổi đúng một lần.
        """
        raise NotImplementedError("TODO 3.1")

    def cz(self, c: int, t: int) -> "QSim":
        """CZ: nhân −1 vào biên độ của những chỉ số có CẢ bit c và bit t bằng 1.

        Lưu ý: CZ đối xứng — cz(a,b) và cz(b,a) cho kết quả giống hệt nhau.
        """
        raise NotImplementedError("TODO 3.2")

    def swap(self, a: int, b: int) -> "QSim":
        """Hoán đổi hai qubit. Có thể ghép từ 3 cổng CNOT — thử tự tìm thứ tự."""
        raise NotImplementedError("TODO 3.3")

    # ══════════════════════════════════════════════════════════════════════════
    # MỐC 4 (Ngày 7–8) · Đo lường
    # ══════════════════════════════════════════════════════════════════════════
    def probabilities(self) -> np.ndarray:
        """Trả mảng 2**n xác suất. Born rule: p_i = |amplitude_i|²."""
        raise NotImplementedError("TODO 4.1")

    def sample(self, shots: int = 1024, seed: int | None = None) -> dict[str, int]:
        """Lấy mẫu shots lần KHÔNG làm sập trạng thái (mô phỏng chạy lại mạch).

        Trả dict {bitstring: số lần}. Bitstring dài đúng n ký tự, viết theo
        quy ước Qiskit: ký tự PHẢI NHẤT là qubit 0.
        Gợi ý: np.random.default_rng(seed).choice(...), và format(i, f"0{n}b").
        """
        raise NotImplementedError("TODO 4.2")

    def measure(self, q: int, seed: int | None = None) -> int:
        """Đo THẬT qubit q: trả về 0/1 và LÀM SẬP trạng thái.

        Ba bước:
          1. p1 = tổng |amplitude|² trên mọi chỉ số có bit q bằng 1
          2. tung ngẫu nhiên theo p1 để ra bit
          3. xoá (gán 0) mọi biên độ không khớp bit đó, rồi CHUẨN HOÁ LẠI
             phần còn lại bằng cách chia cho sqrt(xác suất của nhánh đã chọn)

        Bước 3 chính là "sụp đổ trạng thái" — bỏ chuẩn hoá là sai ngay.
        """
        raise NotImplementedError("TODO 4.3")

    # ══════════════════════════════════════════════════════════════════════════
    # MỐC 5 (Ngày 9–10) · Kiểm chứng chéo — xem test_qsim.py
    # ══════════════════════════════════════════════════════════════════════════
    def __repr__(self) -> str:
        if self.state is None:
            return f"QSim(n={self.n}, chưa khởi tạo)"
        terms = [
            f"{a:+.3f}|{i:0{self.n}b}>"
            for i, a in enumerate(self.state)
            if abs(a) > 1e-9
        ]
        return " ".join(terms) if terms else "0"
