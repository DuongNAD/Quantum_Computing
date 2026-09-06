"""
Lộ trình sắp xếp 350 bài kata theo thứ tự học từ ZERO đến HERO.

Bộ bài gốc (qiskit-community/Qiskit-QuantumKatas) là một dataset benchmark —
các task nằm lộn xộn, không có thứ tự sư phạm. File này áp một lộ trình lên
chúng: 8 bậc, mỗi bậc chỉ mở ra khi bậc trước có nghĩa.

Mỗi bậc gắn với một phase trong lo-trinh-quantum-zero-to-hero.md.
"""

# (thư mục, tên hiển thị, phase tương ứng, mô tả, [danh sách topic theo thứ tự])
#
# Topic viết dạng "tutorials/Qubit" nghĩa là chỉ lấy nhóm con đó.
# Topic viết dạng "BasicGates" nghĩa là lấy cả topic.
# Topic viết dạng "BasicGates:1" nghĩa là chỉ lấy các bài có id bắt đầu bằng "1."
BAC = [
    (
        "01-toan-nen",
        "Bậc 1 · Toán nền",
        "Phase 1",
        "Số phức và vector — hai thứ duy nhất phải biết trước khi chạm vào qubit. "
        "Chưa có qubit nào ở đây cả, chỉ là NumPy thuần.",
        [
            "tutorials/ComplexArithmetic",
            "tutorials/LinearAlgebra",
        ],
    ),
    (
        "02-qubit-dau-tien",
        "Bậc 2 · Qubit đầu tiên",
        "Phase 0-1",
        "Một qubit, các cổng tác động lên nó, và cách nhìn nó trên quả cầu Bloch. "
        "Đây là bậc quan trọng nhất — đừng vội qua.",
        [
            "tutorials/Qubit",
            "tutorials/RandomNumberGeneration",
            "tutorials/SingleQubitGates",
            "tutorials/VisualizationTools",
            "BasicGates:1",
        ],
    ),
    (
        "03-nhieu-qubit",
        "Bậc 3 · Nhiều qubit & vướng víu",
        "Phase 1",
        "Tích tensor, cổng có điều khiển, và entanglement. Chỗ này là nơi trực giác "
        "cổ điển bắt đầu gãy — bình thường.",
        [
            "tutorials/MultiQubitSystems",
            "tutorials/MultiQubitGates",
            "BasicGates:2",
            "Superposition",
        ],
    ),
    (
        "04-do-luong",
        "Bậc 4 · Đo lường",
        "Phase 1",
        "Born rule trong thực chiến: đo là gì, đo xong mất gì, và phân biệt trạng thái "
        "bằng cách đo thế nào.",
        [
            "Measurements",
            "JointMeasurements",
        ],
    ),
    (
        "05-giao-thuc",
        "Bậc 5 · Giao thức lượng tử",
        "Phase 2",
        "Teleportation, superdense coding, BB84. Những giao thức đầu tiên thật sự "
        "*dùng* được entanglement để làm một việc cụ thể.",
        [
            "examples",
            "Teleportation",
            "SuperdenseCoding",
            "KeyDistribution_BB84",
        ],
    ),
    (
        "06-oracle-thuat-toan",
        "Bậc 6 · Oracle & thuật toán kinh điển",
        "Phase 2",
        "Deutsch-Jozsa, Simon, Grover. Mấu chốt: hiểu oracle và phase kickback trước, "
        "thuật toán tự khắc dễ.",
        [
            "tutorials/Oracles",
            "MarkingOracles",
            "tutorials/ExploringDeutschJozsaAlgorithm",
            "DeutschJozsa",
            "SimonsAlgorithm",
            "GroversAlgorithm",
            "SolveSATWithGrover",
        ],
    ),
    (
        "07-qft-phase",
        "Bậc 7 · QFT & Phase Estimation",
        "Phase 2",
        "Nền móng của Shor. Đây là phần toán nặng nhất trong toàn bộ lộ trình.",
        [
            "QFT",
            "PhaseEstimation",
        ],
    ),
    (
        "08-mach-nang-cao",
        "Bậc 8 · Mạch nâng cao & ứng dụng",
        "Phase 3",
        "Xây mạch cỡ lớn: bộ cộng, bảng chân trị, tô màu đồ thị, knapsack. "
        "Bậc rèn kỹ năng dựng mạch chứ không phải học khái niệm mới.",
        [
            "TruthTables",
            "UnitaryPatterns",
            "DistinguishUnitaries",
            "RippleCarryAdder",
            "GraphColoring",
            "BoundedKnapsack",
        ],
    ),
    (
        "09-nghich-ly-qec",
        "Bậc 9 · Nghịch lý lượng tử & Sửa lỗi",
        "Phase 4",
        "Các trò chơi chứng minh lượng tử thật sự khác cổ điển (CHSH, GHZ), và "
        "bit-flip code — viên gạch đầu tiên của Quantum Error Correction.",
        [
            "CHSHGame",
            "GHZGame",
            "MagicSquareGame",
            "QEC_BitFlipCode",
        ],
    ),
]


def natural_key(task_id: str):
    """Sắp '1.10' sau '1.2' thay vì trước nó."""
    tail = task_id.split("/")[-1]
    parts = []
    for chunk in tail.replace("-", ".").split("."):
        parts.append((0, int(chunk)) if chunk.isdigit() else (1, chunk))
    return parts


def topic_of(task_id: str) -> str:
    """'tutorials/Qubit/1' -> 'tutorials/Qubit';  'BasicGates/1.1' -> 'BasicGates'."""
    parts = task_id.split("/")
    return "/".join(parts[:2]) if parts[0] == "tutorials" else parts[0]


def short_topic(task_id: str) -> str:
    """Tên topic ngắn để đặt tên thư mục."""
    return topic_of(task_id).split("/")[-1]


def matches(task_id: str, selector: str) -> bool:
    if ":" in selector:
        topic, group = selector.split(":", 1)
        return topic_of(task_id) == topic and task_id.split("/")[-1].startswith(group + ".")
    return topic_of(task_id) == selector


def build_order(rows):
    """Trả về list (bac_index, thu_tu_toan_cuc, row) đã sắp xếp theo lộ trình."""
    out, used, n = [], set(), 0
    for bi, (_slug, _name, _phase, _desc, selectors) in enumerate(BAC):
        for sel in selectors:
            picked = [r for r in rows if r["task_id"] not in used and matches(r["task_id"], sel)]
            picked.sort(key=lambda r: (topic_of(r["task_id"]), natural_key(r["task_id"])))
            for r in picked:
                used.add(r["task_id"])
                n += 1
                out.append((bi, n, r))
    leftover = [r for r in rows if r["task_id"] not in used]
    if leftover:  # an toàn: không bao giờ bỏ rơi bài nào
        leftover.sort(key=lambda r: (topic_of(r["task_id"]), natural_key(r["task_id"])))
        for r in leftover:
            n += 1
            out.append((len(BAC) - 1, n, r))
    return out
