import sys
import os
import subprocess
import types
import builtins
import inspect

R  = "\033[0m"
G  = "\033[1;32m"
Y  = "\033[1;33m"
RE = "\033[1;31m"
C  = "\033[1;36m"
W  = "\033[1;37m"
B  = "\033[1;30m"

OK   = f"{G}[OK]{R}"
FAIL = f"{RE}[FAIL]{R}"
WARN = f"{Y}[WARN]{R}"
INFO = f"{C}[INFO]{R}"

results = []

def cek(nama, status, keterangan=""):
    icon = OK if status else FAIL
    hasil = "AMAN" if status else "TERDETEKSI"
    results.append((nama, status, keterangan))
    print(f"  {icon}  {W}{nama}{R}")
    if keterangan:
        print(f"       {B}→ {keterangan}{R}")

def separator(judul):
    print(f"\n{B}{'─'*52}{R}")
    print(f"  {C}{judul}{R}")
    print(f"{B}{'─'*52}{R}")

os.system("clear")
print(f"""
{C}╔══════════════════════════════════════════════════════╗
║       OBFUSCATOR ANTI-DEBUG DIAGNOSTIC TOOL         ║
║  Cari tahu kondisi mana yang memicu deteksi debug   ║
╚══════════════════════════════════════════════════════╝{R}
""")

# ─────────────────────────────────────────────────────
# BLOK 1: Python Debugger (cek vA)
# ─────────────────────────────────────────────────────
separator("BLOK 1: Python Debugger Trace (vA)")

try:
    trace = sys.gettrace()
    cek("sys.gettrace() == None",
        trace is None,
        f"Nilai: {trace!r} — {'bersih' if trace is None else 'ADA trace function aktif! (IDE debugger atau pdb aktif)'}")
except Exception as e:
    cek("sys.gettrace()", False, f"Exception: {e}")

try:
    orig_exec = builtins.__dict__.get("exec")
    is_builtin = isinstance(orig_exec, types.BuiltinFunctionType)
    cek("builtins.exec masih BuiltinFunctionType",
        is_builtin,
        f"Tipe saat ini: {type(orig_exec).__name__} — {'bersih' if is_builtin else 'exec SUDAH DI-HOOK! (Kamer.py atau tool dump lain aktif)'}")
except Exception as e:
    cek("builtins.exec type check", False, f"Exception: {e}")

# ─────────────────────────────────────────────────────
# BLOK 2: Module Debugger (cek vB)
# ─────────────────────────────────────────────────────
separator("BLOK 2: Modul Debugger di sys.modules (vB)")

DEBUG_MODULES = [
    "pydevd", "debugpy", "bdb", "pdb", "rpdb",
    "pycdc", "decompyle3", "uncompyle6", "thxyzz404"
]

found_modules = [m for m in DEBUG_MODULES if m in sys.modules]
cek("Tidak ada modul debugger ter-import",
    len(found_modules) == 0,
    f"Ditemukan: {found_modules}" if found_modules else "Semua bersih")

# ─────────────────────────────────────────────────────
# BLOK 3: TracerPid (/proc/self/status) (cek _rck vB)
# ─────────────────────────────────────────────────────
separator("BLOK 3: TracerPid — Debugger Attach via ptrace")

try:
    r = subprocess.run(
        ["cat", "/proc/self/status"],
        capture_output=True, text=True, timeout=3
    )
    tracerpid = 0
    for ln in r.stdout.splitlines():
        if "TracerPid" in ln:
            tracerpid = int(ln.split(":")[-1].strip())
            break
    cek("TracerPid == 0",
        tracerpid == 0,
        f"TracerPid: {tracerpid} — {'bersih' if tracerpid == 0 else f'ADA proses yang attach! PID={tracerpid} (GDB/Frida/strace attach)'}")
except Exception as e:
    cek("TracerPid check", False, f"Exception: {e}")

# ─────────────────────────────────────────────────────
# BLOK 4: Memory Maps — Frida/GDB di /proc/self/maps
# ─────────────────────────────────────────────────────
separator("BLOK 4: Memory Maps — Frida/GDB/Debugger Library")

try:
    r = subprocess.run(
        ["cat", "/proc/self/maps"],
        capture_output=True, text=True, timeout=3
    )
    BAD_MAPS = ["frida", "gdb", "lldb", "r2pipe", "radare", "pydevd", "debugpy"]
    found_maps = [b for b in BAD_MAPS if b in r.stdout.lower()]
    cek("Tidak ada library debugger di memory maps",
        len(found_maps) == 0,
        f"Ditemukan di maps: {found_maps}" if found_maps else "Semua bersih")
except Exception as e:
    cek("Memory maps check", False, f"Exception: {e}")

# ─────────────────────────────────────────────────────
# BLOK 5: File Descriptor — Frida artifact
# ─────────────────────────────────────────────────────
separator("BLOK 5: File Descriptor — Frida Socket/Pipe")

try:
    frida_in_fd = False
    frida_fd_detail = ""
    for fd in os.listdir("/proc/self/fd"):
        try:
            link = os.readlink(f"/proc/self/fd/{fd}")
            if "frida" in link.lower():
                frida_in_fd = True
                frida_fd_detail = link
                break
        except Exception:
            pass
    cek("Tidak ada Frida artifact di file descriptor",
        not frida_in_fd,
        f"Ditemukan: {frida_fd_detail}" if frida_in_fd else "Bersih")
except Exception as e:
    cek("File descriptor check", False, f"Exception: {e}")

# ─────────────────────────────────────────────────────
# BLOK 6: Process List — Frida/GDB/Strace running
# ─────────────────────────────────────────────────────
separator("BLOK 6: Proses Aktif — Frida/GDB/Strace/Objection")

try:
    r = subprocess.run(
        ["ps", "aux"],
        capture_output=True, text=True, timeout=3
    )
    BAD_PROCS = ["frida", "gdb", "strace", "ltrace", "objection", "lldb", "r2"]
    found_procs = [b for b in BAD_PROCS if b in r.stdout.lower()]
    cek("Tidak ada proses debugger aktif",
        len(found_procs) == 0,
        f"Proses terdeteksi: {found_procs}" if found_procs else "Semua bersih")
except Exception as e:
    cek("Process list check", False, f"Exception: {e}")

# ─────────────────────────────────────────────────────
# BLOK 7: requests library integrity (cek vC)
# ─────────────────────────────────────────────────────
separator("BLOK 7: Integritas Library requests (HTTP Hook)")

try:
    import requests as _rq
    m = _rq.sessions.Session.request
    if isinstance(m, types.FunctionType):
        src_file  = inspect.getfile(m)
        real_file = inspect.getfile(_rq.sessions.Session)
        is_ok = (src_file == real_file)
        cek("requests.Session.request tidak di-hook",
            is_ok,
            f"File method: {os.path.basename(src_file)} | File class: {os.path.basename(real_file)}" if not is_ok
            else "requests bersih dari hook")
    else:
        cek("requests.Session.request tidak di-hook", True, "Tipe bukan FunctionType, aman")
except ImportError:
    cek("requests library check", True, "requests tidak ter-install (tidak di-check, skip)")
except Exception as e:
    cek("requests library check", False, f"Exception: {e}")

# ─────────────────────────────────────────────────────
# BLOK 8: urllib / http.client integrity (cek vC)
# ─────────────────────────────────────────────────────
separator("BLOK 8: Integritas urllib & http.client (Sniff Hook)")

try:
    import urllib.request as _uq
    import http.client as _hcq

    checks = [
        (_uq.urlopen,                  _uq,                    "urllib.request.urlopen"),
        (_hcq.HTTPConnection.request,  _hcq.HTTPConnection,   "http.client.HTTPConnection.request"),
        (_hcq.HTTPSConnection.request, _hcq.HTTPSConnection,  "http.client.HTTPSConnection.request"),
    ]

    for fn, owner, label in checks:
        if isinstance(fn, types.FunctionType):
            src_file  = inspect.getfile(fn)
            real_file = inspect.getfile(owner)
            is_ok = (src_file == real_file)
            cek(f"{label} tidak di-hook",
                is_ok,
                f"DI-HOOK! File method: {os.path.basename(src_file)} | File class: {os.path.basename(real_file)}"
                if not is_ok else "Bersih")
        else:
            cek(f"{label} tidak di-hook", True, "Bukan FunctionType, aman")
except Exception as e:
    cek("urllib/http.client check", False, f"Exception: {e}")

# ─────────────────────────────────────────────────────
# RINGKASAN
# ─────────────────────────────────────────────────────
print(f"\n{B}{'═'*52}{R}")
print(f"  {C}RINGKASAN HASIL{R}")
print(f"{B}{'═'*52}{R}\n")

gagal = [(nama, ket) for nama, status, ket in results if not status]
aman  = [(nama, ket) for nama, status, ket in results if status]

print(f"  {OK}  Kondisi aman : {len(aman)}/{len(results)}")
print(f"  {FAIL}  Kondisi gagal: {len(gagal)}/{len(results)}\n")

if not gagal:
    print(f"  {G}Semua kondisi AMAN.{R}")
    print(f"  {W}Kemungkinan penyebab lain:{R}")
    print(f"  {B}→ Pastikan menjalankan di Termux Android asli{R}")
    print(f"  {B}→ Cek apakah ada root/Magisk yang ke-detect{R}")
    print(f"  {B}→ Jalankan: {Y}RUNNER_DEBUG=1 python runner.py{R}")
else:
    print(f"  {RE}Kondisi yang memicu deteksi debugger:{R}\n")
    for i, (nama, ket) in enumerate(gagal, 1):
        print(f"  {RE}{i}.{R} {W}{nama}{R}")
        if ket:
            print(f"     {B}→ {ket}{R}")
        print()

print(f"{B}{'═'*52}{R}\n")
