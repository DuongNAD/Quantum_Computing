#!/usr/bin/env python3
"""
qk — Quantum Katas runner (kiểu rustlings, chạy offline)

    python qk.py              trạng thái + bài kế tiếp
    python qk.py gen          sinh/đồng bộ file bài tập (không ghi đè bài đã làm)
    python qk.py next         mở bài kế tiếp chưa xong
    python qk.py run [ID]     chấm 1 bài (bỏ trống = bài đang làm dở)
    python qk.py run --bac 2  chấm cả một bậc
    python qk.py run --all    chấm toàn bộ
    python qk.py watch        tự chấm lại mỗi khi bạn lưu file
    python qk.py hint ID      gợi ý tăng dần (gọi nhiều lần để mở thêm)
    python qk.py solution ID  hiện lời giải chuẩn (dùng khi đã thật sự bí)
    python qk.py list [--bac N]
    python qk.py reset ID     trả bài về stub gốc
    python qk.py progress     xuất tiến độ ra JSON cho slide

ID có thể viết tắt: "BasicGates/1.1", "1.1", hoặc số thứ tự toàn cục "42".
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from curriculum import BAC, build_order, short_topic, topic_of  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "qiskit_quantumkatas.jsonl"
EXDIR = ROOT / "exercises"
STATE = ROOT / ".state.json"

# ── màu terminal ──────────────────────────────────────────────────────────────
_TTY = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


def c(code: str, s: str) -> str:
    return f"\033[{code}m{s}\033[0m" if _TTY else s


BOLD = lambda s: c("1", s)          # noqa: E731
DIM = lambda s: c("2", s)           # noqa: E731
RED = lambda s: c("31", s)          # noqa: E731
GREEN = lambda s: c("32", s)        # noqa: E731
YELLOW = lambda s: c("33", s)       # noqa: E731
BLUE = lambda s: c("36", s)         # noqa: E731
MAGENTA = lambda s: c("35", s)      # noqa: E731


def hr(ch="─", n=74):
    return DIM(ch * n)


# ── dữ liệu ───────────────────────────────────────────────────────────────────
def load_rows():
    if not DATA.exists():
        sys.exit(RED(f"Không tìm thấy {DATA}. Xem katas/README.md để tải lại dataset."))
    return [json.loads(line) for line in DATA.open(encoding="utf-8")]


def load_state():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def save_state(st):
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")


class Kata:
    __slots__ = ("bac", "n", "row", "path")

    def __init__(self, bac, n, row):
        self.bac, self.n, self.row = bac, n, row
        slug = BAC[bac][0]
        fname = f"{n:03d}-{row['entry_point']}.py"
        self.path = EXDIR / slug / short_topic(row["task_id"]) / fname

    @property
    def id(self):
        return self.row["task_id"]

    @property
    def entry(self):
        return self.row["entry_point"]

    @property
    def title(self):
        """Dòng '# Task 1.1. State flip: ...' -> 'State flip: ...'"""
        for line in self.row["prompt"].splitlines():
            m = re.match(r"#\s*Task\s+[\d.]+\.?\s*(.+)", line.strip())
            if m:
                return m.group(1).strip()
        for line in self.row["prompt"].splitlines():
            s = line.strip().lstrip("#").strip()
            if s:
                return s
        return self.entry


def catalog():
    rows = load_rows()
    return [Kata(b, n, r) for b, n, r in build_order(rows)]


# ── sinh file bài tập ─────────────────────────────────────────────────────────
HEADER = """# ══════════════════════════════════════════════════════════════════════════════
# BÀI {n:03d}/{total}  ·  {bac}
# {id}
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run {id}
#   Gợi ý:      python qk.py hint {id}
#   Lời giải:   python qk.py solution {id}
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

"""


def stub_source(k: Kata, total: int) -> str:
    return HEADER.format(n=k.n, total=total, bac=BAC[k.bac][1], id=k.id) + k.row["prompt"] + "\n"


def cmd_gen(args):
    kats = catalog()
    total = len(kats)
    created = skipped = 0
    for k in kats:
        k.path.parent.mkdir(parents=True, exist_ok=True)
        if k.path.exists():
            skipped += 1
            continue
        k.path.write_text(stub_source(k, total), encoding="utf-8")
        created += 1
    for bi, (slug, name, phase, desc, _sel) in enumerate(BAC):
        d = EXDIR / slug
        if d.exists():
            n_in_bac = sum(1 for k in kats if k.bac == bi)
            (d / "README.md").write_text(
                f"# {name}\n\n*{phase} · {n_in_bac} bài*\n\n{desc}\n", encoding="utf-8"
            )
    print(GREEN(f"✔ Sinh {created} bài mới") + DIM(f"  (giữ nguyên {skipped} bài đã có)"))
    print(DIM(f"  → {EXDIR}"))


# ── chấm bài ──────────────────────────────────────────────────────────────────
def is_untouched(k: Kata, total: int) -> bool:
    if not k.path.exists():
        return True
    cur = k.path.read_text(encoding="utf-8")
    return _norm(cur) == _norm(stub_source(k, total))


def _norm(s: str) -> str:
    return "\n".join(line.rstrip() for line in s.strip().splitlines())


def _explain(exc, src_lines, path):
    """Biến traceback thành thông báo ngắn, chỉ nói về code của người học."""
    tb = exc.__traceback__
    frames = []
    while tb:
        f = tb.tb_frame
        if f.f_code.co_filename == str(path):
            frames.append(tb.tb_lineno)
        tb = tb.tb_next
    out = []
    kind = type(exc).__name__
    msg = str(exc).strip()

    if isinstance(exc, AssertionError):
        out.append("Test không pass — kết quả hàm của bạn chưa đúng.")
        if msg:
            out.append(f"Thông báo: {msg}")
    elif isinstance(exc, TypeError) and "NoneType" in msg:
        out.append("Hàm đang trả về None — nhiều khả năng bạn chưa xoá `pass`, "
                   "hoặc quên `return`.")
        out.append(f"{kind}: {msg}")
    elif isinstance(exc, NotImplementedError):
        out.append("Bài này chưa được làm.")
    else:
        out.append(f"{kind}: {msg}" if msg else kind)

    if frames:
        ln = frames[-1]
        out.append("")
        lo, hi = max(0, ln - 3), min(len(src_lines), ln + 2)
        for i in range(lo, hi):
            marker = "→" if i + 1 == ln else " "
            out.append(f"  {marker} {i+1:4d} │ {src_lines[i]}")
    return "\n".join(out)


def grade(k: Kata):
    """Trả về (ok: bool, err: str|None, out: str)."""
    if not k.path.exists():
        return False, "Chưa có file bài tập. Chạy: python qk.py gen", ""
    user = k.path.read_text(encoding="utf-8")
    src = user + "\n\n" + k.row["test"] + "\n"
    src_lines = src.splitlines()
    g = {"__name__": "__main__", "__file__": str(k.path)}
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            exec(compile(src, str(k.path), "exec"), g)
            tests = [v for name, v in g.items() if name.startswith("test_") and callable(v)]
            if not tests:
                raise RuntimeError("Không tìm thấy hàm test_* trong bộ đề")
            for t in tests:
                t()
    except Exception as exc:  # noqa: BLE001 — mọi lỗi đều là phản hồi cho người học
        return False, _explain(exc, src_lines, k.path), buf.getvalue()
    return True, None, buf.getvalue()


def mark(st, k: Kata, ok: bool):
    e = st.setdefault(k.id, {"attempts": 0})
    e["attempts"] = e.get("attempts", 0) + 1
    e["n"] = k.n
    e["bac"] = k.bac
    if ok and not e.get("done_at"):
        e["done_at"] = datetime.now().isoformat(timespec="seconds")
    e["done"] = bool(ok) or bool(e.get("done"))
    return e


def report(k: Kata, ok, err, out, verbose=True):
    tag = f"{k.n:03d} · {k.id}"
    if ok:
        print(GREEN(f"  ✔ PASS  {tag}") + DIM(f"  — {k.title}"))
        return
    print(RED(f"  ✘ FAIL  {tag}") + DIM(f"  — {k.title}"))
    if verbose:
        if out.strip():
            print(DIM("  ── stdout ──"))
            for line in out.strip().splitlines()[-10:]:
                print(DIM("  │ " + line))
        print(YELLOW("  ── lỗi ──"))
        for line in (err or "").strip().splitlines()[-14:]:
            print("  │ " + line)


def resolve(kats, token: str):
    """Tìm kata theo id đầy đủ, đuôi id, entry_point, hoặc số thứ tự."""
    token = token.strip()
    if token.isdigit():
        n = int(token)
        for k in kats:
            if k.n == n:
                return k
    exact = [k for k in kats if k.id == token]
    if exact:
        return exact[0]
    low = token.lower()
    cand = [k for k in kats if k.id.lower().endswith("/" + low) or k.entry.lower() == low]
    if len(cand) == 1:
        return cand[0]
    if len(cand) > 1:
        print(YELLOW(f"'{token}' khớp nhiều bài, ghi rõ hơn:"))
        for k in cand[:12]:
            print(f"   {k.n:03d}  {k.id}")
        sys.exit(1)
    part = [k for k in kats if low in k.id.lower() or low in k.entry.lower()]
    if len(part) == 1:
        return part[0]
    if part:
        print(YELLOW(f"'{token}' khớp nhiều bài, ghi rõ hơn:"))
        for k in part[:12]:
            print(f"   {k.n:03d}  {k.id}")
        sys.exit(1)
    sys.exit(RED(f"Không tìm thấy bài nào khớp '{token}'"))


def cmd_run(args):
    kats = catalog()
    st = load_state()
    total = len(kats)

    if args.all:
        target = kats
    elif args.bac is not None:
        target = [k for k in kats if k.bac == args.bac - 1]
        if not target:
            sys.exit(RED(f"Không có bậc {args.bac}. Có 1..{len(BAC)}."))
    elif args.id:
        target = [resolve(kats, args.id)]
    else:
        target = [next_kata(kats, st, total)]
        if target[0] is None:
            print(GREEN("🎉 Bạn đã xong toàn bộ 350 bài."))
            return

    verbose = len(target) == 1
    npass = nblank = 0
    for k in target:
        if len(target) > 1 and is_untouched(k, total):
            nblank += 1
            continue
        ok, err, out = grade(k)
        mark(st, k, ok)
        npass += ok
        report(k, ok, err, out, verbose=verbose)
    save_state(st)

    if len(target) > 1:
        nfail = len(target) - npass - nblank
        print(hr())
        print(
            f"  {GREEN(f'{npass} pass')}   {RED(f'{nfail} fail')}   "
            f"{DIM(f'{nblank} chưa làm')}   / {len(target)} bài"
        )
    elif npass:
        nk = next_kata(kats, st, total)
        if nk:
            print(hr())
            print(f"  Bài kế tiếp: {BOLD(nk.id)}  →  {DIM(str(nk.path.relative_to(ROOT)))}")


def next_kata(kats, st, total):
    for k in kats:
        if not st.get(k.id, {}).get("done"):
            return k
    return None


def cmd_next(args):
    kats = catalog()
    st = load_state()
    total = len(kats)
    k = next_kata(kats, st, total)
    if not k:
        print(GREEN("🎉 Hết bài rồi. Bạn đã hoàn thành cả 350 kata."))
        return
    slug, name, phase, desc, _ = BAC[k.bac]
    print()
    print(hr("═"))
    print(f"  {MAGENTA(name)}  {DIM('·')}  {DIM(phase)}")
    print(f"  {BOLD(f'Bài {k.n:03d}/{total}')}  {BLUE(k.id)}")
    print(hr("═"))
    print(f"  {BOLD(k.title)}")
    print()
    print(f"  File   {DIM(str(k.path.relative_to(ROOT)))}")
    print(f"  Chấm   {DIM(f'python qk.py run {k.id}')}")
    print(f"  Gợi ý  {DIM(f'python qk.py hint {k.id}')}")
    print()
    desc = [ln for ln in k.row["prompt"].splitlines() if ln.strip().startswith("#")]
    for line in desc[:18]:
        print("  " + DIM(line))
    sig = [ln for ln in k.row["prompt"].splitlines() if ln.startswith("def ")]
    if sig:
        print()
        print(f"  {BOLD('Hàm cần viết:')}  {BLUE(sig[0][4:].rstrip(':'))}")
    print()


def cmd_list(args):
    kats = catalog()
    st = load_state()
    cur_bac = cur_topic = None
    for k in kats:
        if args.bac and k.bac != args.bac - 1:
            continue
        if k.bac != cur_bac:
            cur_bac = k.bac
            slug, name, phase, desc, _ = BAC[k.bac]
            done = sum(1 for x in kats if x.bac == k.bac and st.get(x.id, {}).get("done"))
            tot = sum(1 for x in kats if x.bac == k.bac)
            print()
            print(hr("═"))
            print(f"  {MAGENTA(BOLD(name))}   {GREEN(f'{done}/{tot}')}   {DIM(phase)}")
            print(hr("═"))
            cur_topic = None
        t = topic_of(k.id)
        if t != cur_topic:
            cur_topic = t
            print(f"  {BLUE(t)}")
        mk = GREEN("✔") if st.get(k.id, {}).get("done") else DIM("·")
        print(f"    {mk} {k.n:03d}  {k.id:<34} {DIM(k.title[:44])}")
    print()


def solution_body(sol: str):
    """Bỏ import, docstring và dòng trống — chỉ giữ code thật sự."""
    lines, out, in_doc, quote = sol.splitlines(), [], False, ""
    for ln in lines:
        s = ln.strip()
        if in_doc:
            if quote in s:
                in_doc = False
            continue
        if s.startswith(('"""', "'''")):
            quote = s[:3]
            if not (len(s) > 3 and s.endswith(quote)):
                in_doc = True
            continue
        if not s or s.startswith(("import ", "from ")):
            continue
        out.append(ln)
    return out


def cmd_hint(args):
    kats = catalog()
    k = resolve(kats, args.id)
    st = load_state()
    e = st.setdefault(k.id, {})
    lvl = e.get("hint", 0) + 1
    e["hint"] = lvl
    save_state(st)

    sol = k.row["canonical_solution"]
    body = solution_body(sol)
    comments = [ln.strip().lstrip("#").strip() for ln in sol.splitlines() if ln.strip().startswith("#")]
    gates = sorted(
        set(re.findall(r"\b(?:qc|circuit|qcirc)\.(\w+)\(", sol))
        | set(re.findall(r"\bnp\.(\w+)\(", sol))
    )

    print()
    print(f"  {YELLOW(f'Gợi ý mức {lvl}')} cho {BOLD(k.id)}")
    print(hr())
    if lvl == 1:
        if gates:
            print(f"  Lời giải dùng các thao tác: {BOLD(', '.join(gates))}")
        print(f"  Độ dài lời giải: khoảng {len(body)} dòng code.")
        print(DIM("  Chạy lại lệnh hint để mở gợi ý sâu hơn."))
    elif lvl == 2:
        if comments:
            print("  Chú thích của tác giả trong lời giải:")
            for cm in comments[:6]:
                print(f"    {DIM('·')} {cm}")
        else:
            print(f"  Khung lời giải:\n")
            for ln in body[:4]:
                print(DIM("    " + re.sub(r"(?<=\().*(?=\))", "…", ln)))
        print(DIM("  Chạy hint lần nữa để xem lời giải rút gọn."))
    else:
        print("  Lời giải (đã bỏ docstring):")
        for ln in body:
            print("    " + ln)
        print()
        print(DIM(f"  Bản đầy đủ: python qk.py solution {k.id}"))
    print()


def cmd_solution(args):
    kats = catalog()
    k = resolve(kats, args.id)
    st = load_state()
    st.setdefault(k.id, {})["saw_solution"] = True
    save_state(st)
    print()
    print(f"  {MAGENTA('Lời giải chuẩn')} · {BOLD(k.id)}")
    print(hr())
    for ln in k.row["canonical_solution"].splitlines():
        print("  " + ln)
    print(hr())
    print(DIM("  Đọc hiểu rồi tự gõ lại vào file — đừng copy-paste."))
    print()


def cmd_reset(args):
    kats = catalog()
    k = resolve(kats, args.id)
    total = len(kats)
    k.path.parent.mkdir(parents=True, exist_ok=True)
    k.path.write_text(stub_source(k, total), encoding="utf-8")
    st = load_state()
    st.pop(k.id, None)
    save_state(st)
    print(GREEN(f"✔ Đã trả {k.id} về stub gốc."))


def cmd_watch(args):
    kats = catalog()
    total = len(kats)
    st = load_state()
    index = {str(k.path.resolve()): k for k in kats}
    print(BOLD("  qk watch") + DIM("  — lưu file bất kỳ trong exercises/ là tự chấm. Ctrl-C để thoát."))
    k0 = next_kata(kats, st, total)
    if k0:
        print(DIM(f"  Bài kế tiếp: {k0.id}  ({k0.path.relative_to(ROOT)})"))
    mtimes = {p: p.stat().st_mtime for p in EXDIR.rglob("*.py")}
    try:
        while True:
            time.sleep(0.5)
            for p in EXDIR.rglob("*.py"):
                m = p.stat().st_mtime
                if mtimes.get(p) == m:
                    continue
                mtimes[p] = m
                k = index.get(str(p.resolve()))
                if not k:
                    continue
                print()
                print(hr())
                print(DIM(f"  {datetime.now():%H:%M:%S}  {p.relative_to(ROOT)}"))
                ok, err, out = grade(k)
                mark(st, k, ok)
                save_state(st)
                report(k, ok, err, out, verbose=True)
                if ok:
                    nk = next_kata(kats, st, total)
                    if nk:
                        print(f"  {GREEN('→')} Bài kế tiếp: {BOLD(nk.id)}  {DIM(str(nk.path.relative_to(ROOT)))}")
                    else:
                        print(GREEN("  🎉 Xong toàn bộ 350 bài."))
    except KeyboardInterrupt:
        print("\n" + DIM("  Thoát watch."))


def cmd_progress(args):
    kats = catalog()
    st = load_state()
    out = {
        "total": len(kats),
        "done": sum(1 for k in kats if st.get(k.id, {}).get("done")),
        "updated": datetime.now().isoformat(timespec="seconds"),
        "bac": [],
    }
    for bi, (slug, name, phase, desc, _s) in enumerate(BAC):
        ks = [k for k in kats if k.bac == bi]
        out["bac"].append({
            "slug": slug, "name": name, "phase": phase, "desc": desc,
            "total": len(ks),
            "done": sum(1 for k in ks if st.get(k.id, {}).get("done")),
            "topics": sorted({topic_of(k.id) for k in ks}),
        })
    dest = ROOT.parent / "slides" / "assets" / "progress.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    print(DIM(f"\n→ đã ghi {dest}"))


def cmd_status(args):
    kats = catalog()
    st = load_state()
    total = len(kats)
    done = sum(1 for k in kats if st.get(k.id, {}).get("done"))
    print()
    print(hr("═"))
    print(BOLD("  QUANTUM KATAS") + DIM("   350 bài · 9 bậc · zero → hero"))
    print(hr("═"))
    for bi, (slug, name, phase, desc, _s) in enumerate(BAC):
        ks = [k for k in kats if k.bac == bi]
        d = sum(1 for k in ks if st.get(k.id, {}).get("done"))
        width = 22
        fill = round(width * d / len(ks)) if ks else 0
        bar = GREEN("█" * fill) + DIM("░" * (width - fill))
        pct = f"{100*d/len(ks):3.0f}%" if ks else "  -"
        print(f"  {bar} {pct}  {name:<34} {DIM(f'{d}/{len(ks)}')}")
    print(hr())
    width = 40
    fill = round(width * done / total)
    print(f"  {GREEN('█'*fill)}{DIM('░'*(width-fill))}  {BOLD(f'{done}/{total}')}  ({100*done/total:.1f}%)")
    print()
    k = next_kata(kats, st, total)
    if k:
        print(f"  Tiếp theo → {BOLD(k.id)}  {DIM(k.title[:40])}")
        print(f"              {DIM(str(k.path.relative_to(ROOT)))}")
        print()
        print(DIM("  python qk.py next     xem đề đầy đủ"))
        print(DIM("  python qk.py watch    chấm tự động khi lưu file"))
    else:
        print(GREEN("  🎉 Hoàn thành toàn bộ."))
    print()


def main():
    p = argparse.ArgumentParser(prog="qk", description="Quantum Katas runner")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("gen", help="sinh file bài tập").set_defaults(fn=cmd_gen)
    sub.add_parser("next", help="bài kế tiếp").set_defaults(fn=cmd_next)
    sub.add_parser("status", help="bảng tiến độ").set_defaults(fn=cmd_status)
    sub.add_parser("watch", help="tự chấm khi lưu file").set_defaults(fn=cmd_watch)
    sub.add_parser("progress", help="xuất tiến độ JSON").set_defaults(fn=cmd_progress)

    r = sub.add_parser("run", help="chấm bài")
    r.add_argument("id", nargs="?")
    r.add_argument("--bac", type=int)
    r.add_argument("--all", action="store_true")
    r.set_defaults(fn=cmd_run)

    l = sub.add_parser("list", help="liệt kê bài")
    l.add_argument("--bac", type=int)
    l.set_defaults(fn=cmd_list)

    for name, fn in (("hint", cmd_hint), ("solution", cmd_solution), ("reset", cmd_reset)):
        s = sub.add_parser(name)
        s.add_argument("id")
        s.set_defaults(fn=fn)

    args = p.parse_args()
    if not args.cmd:
        return cmd_status(args)
    args.fn(args)


if __name__ == "__main__":
    main()
