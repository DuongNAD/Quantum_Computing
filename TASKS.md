---
document_type: project_task_board
project: Quantum Computing
version: 1.0.0
last_updated: 2026-09-23
master_index: file:///D:/02_Learning_Knowledge/INDEX.md
focus_board: file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md
central_tasks: file:///D:/02_Learning_Knowledge/TASKS.md
rfc2119_compliance: strict
emoji_policy: none
---

# Quantum Computing - Task Board

Master Knowledge Map: [INDEX.md](file:///D:/02_Learning_Knowledge/INDEX.md)
Active Focus Board: [ACTIVE_LEARNING.md](file:///D:/02_Learning_Knowledge/ACTIVE_LEARNING.md)
System Task Board: [TASKS.md](file:///D:/02_Learning_Knowledge/TASKS.md)
Project Overview: [README.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/README.md)
Curriculum Roadmap: [lo-trinh-quantum-zero-to-hero.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/lo-trinh-quantum-zero-to-hero.md)
Circuit Simulator Engine: [qsim](file:///D:/02_Learning_Knowledge/Quantum_Computing/qsim)
Katas Suite: [katas](file:///D:/02_Learning_Knowledge/Quantum_Computing/katas)

## Task Maintenance Rules (RFC 2119)
- Standardized Schema: All tasks MUST follow the tag format `- [ ] [Deadline: YYYY-MM-DD HH:mm] [Priority: P0/P1/P2] Description`.
- Task Preservation: AI agents MUST NEVER delete existing tasks.
- Status Transitions: Task status MUST ONLY be transitioned between `[ ]` and `[x]`, and status change to completed MUST occur ONLY IF verification criteria are met.
- Task Placement: Newly identified micro-tasks MUST be appended to the end of the appropriate section.
- Local Authority: Local operations within this project directory MUST update this file directly.

## 1. Curriculum Setup & Phase 0 Simulation
- [x] [Deadline: 2026-09-21 23:59] [Priority: P2] Thiết lập lộ trình học tập Zero-to-Hero trong [lo-trinh-quantum-zero-to-hero.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/lo-trinh-quantum-zero-to-hero.md).
- [x] [Deadline: 2026-09-21 23:59] [Priority: P2] Khởi tạo cấu trúc dự án: [phase0](file:///D:/02_Learning_Knowledge/Quantum_Computing/phase0), [katas](file:///D:/02_Learning_Knowledge/Quantum_Computing/katas), [qsim](file:///D:/02_Learning_Knowledge/Quantum_Computing/qsim).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Thực nghiệm cổng Hadamard và trạng thái chồng chập (|0> + |1>)/sqrt(2) trong [phase0/h_test.py](file:///D:/02_Learning_Knowledge/Quantum_Computing/phase0/h_test.py).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Thực nghiệm hiện tượng giao thoa sóng lượng tử trong [phase0/giao_thoa.py](file:///D:/02_Learning_Knowledge/Quantum_Computing/phase0/giao_thoa.py).
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Thực nghiệm tạo và đo cặp vướng víu Bell state trong [phase0/bell_test.py](file:///D:/02_Learning_Knowledge/Quantum_Computing/phase0/bell_test.py).
- [ ] [Deadline: 2026-09-27 23:59] [Priority: P1] Chạy và hoàn thành kịch bản thực hành tương tác trực quan trong [phase0/thuc_hanh_tuong_tac.py](file:///D:/02_Learning_Knowledge/Quantum_Computing/phase0/thuc_hanh_tuong_tac.py).

## 2. Phase 1 - Custom Quantum Circuit Simulator (`qsim`)
- [x] [Deadline: 2026-09-22 23:59] [Priority: P2] Khởi tạo bộ test suite toàn diện: [qsim/test_qsim.py](file:///D:/02_Learning_Knowledge/Quantum_Computing/qsim/test_qsim.py).
- [ ] [Deadline: 2026-09-29 23:59] [Priority: P1] Mốc 1: Hoàn thiện ma trận các cổng 1-qubit (I, X, Y, Z, H, S, T) và ma trận quay R_x(theta), R_y(theta), R_z(theta) trong [qsim/qsim.py](file:///D:/02_Learning_Knowledge/Quantum_Computing/qsim/qsim.py).
- [ ] [Deadline: 2026-09-30 23:59] [Priority: P1] Mốc 1.5: Cài đặt khởi tạo vector trạng thái |00...0> kích thước 2^n phần tử complex trong lớp QSim.
- [ ] [Deadline: 2026-10-01 23:59] [Priority: P2] Mốc 2: Cài đặt áp dụng cổng 1-qubit lên qubit bất kỳ trong hệ n-qubit sử dụng phép biến đổi chỉ số nhị phân (tránh nhân ma trận toàn phần 2^n x 2^n).
- [ ] [Deadline: 2026-10-02 23:59] [Priority: P2] Mốc 3: Cài đặt các cổng 2-qubit (CNOT, CZ, SWAP) tác động lên cặp qubit điều khiển và qubit đích.
- [ ] [Deadline: 2026-10-03 23:59] [Priority: P2] Mốc 4: Cài đặt hàm tính xác suất trạng thái, hàm lấy mẫu phân bố (sample), và hàm đo lường làm sụp đổ trạng thái (measure).
- [ ] [Deadline: 2026-10-04 23:59] [Priority: P2] Mốc 5: Triển khai mạch tạo 4 trạng thái Bell, trạng thái GHZ 3-qubit, và biến đổi Fourier lượng tử (QFT).
- [ ] [Deadline: 2026-10-05 23:59] [Priority: P2] Chạy `pytest Quantum_Computing/qsim/test_qsim.py` và vượt qua toàn bộ 39 test cases.

## 3. Katas Problem Sets (`katas`)
- [ ] [Deadline: 2026-09-28 23:59] [Priority: P1] Khởi chạy công cụ luyện tập katas qua CLI: `python katas/qk.py list`.
- [ ] [Deadline: 2026-09-28 23:59] [Priority: P1] Hoàn thành Chủ đề 01: Cơ bản về Qubit và biểu diễn trạng thái trên quả cầu Bloch.
- [ ] [Deadline: 2026-10-06 23:59] [Priority: P2] Hoàn thành Chủ đề 02: Cổng lượng tử 1-qubit (Pauli X, Y, Z, Phase Shift, Hadamard).
- [ ] [Deadline: 2026-10-07 23:59] [Priority: P2] Hoàn thành Chủ đề 03: Hệ đa qubit, tích Tensor (Kronecker product), và trạng thái vướng víu.
- [ ] [Deadline: 2026-10-08 23:59] [Priority: P2] Hoàn thành Chủ đề 04: Đo lường lượng tử, tiên đề cơ bản và tính ngẫu nhiên Born.
- [ ] [Deadline: 2026-10-09 23:59] [Priority: P2] Hoàn thành bài tập nâng cao: Giao thức dịch chuyển tức thời lượng tử (Quantum Teleportation).

## 4. Roadmap v2 Milestones ([ROADMAP.md](file:///D:/02_Learning_Knowledge/Quantum_Computing/Roadmaps/ROADMAP.md))
- [ ] [Deadline: 2026-10-18 21:00] [Priority: P2] Tạo venv ngoài SSD, cài qiskit 2.5.1 và qiskit-aer 0.17.2 từ requirements.txt; chạy python katas/qk.py status.
- [ ] [Deadline: 2026-11-15 21:00] [Priority: P2] Xong M1-M2: kata 001-006, 062, 063; qsim -k khoi_tao pass; thuc_hanh_tuong_tac.py chương 1, 3, 5.
- [ ] [Deadline: 2026-12-06 21:00] [Priority: P2] Xong M3: 13 kata lõi; qsim Mốc 1-2 (15 passed).
- [ ] [Deadline: 2027-01-10 21:00] [Priority: P2] Xong M4-M5: 23 kata lõi; qsim 39/39 khớp Qiskit.
- [ ] [Deadline: 2027-01-31 21:00] [Priority: P2] Xong M6-M7: teleportation, superdense coding, Deutsch-Jozsa, Bernstein-Vazirani (20 kata lõi).
- [ ] [Deadline: 2027-03-07 21:00] [Priority: P2] Xong M8-M9: Grover, QFT, QPE (17 kata lõi); Shor N = 15 làm tay.
- [ ] [Deadline: 2027-04-04 21:00] [Priority: P2] Xong M10-M11, Dự án 2 và buổi ôn tổng kết.
