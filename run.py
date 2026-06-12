import subprocess
import sys
import os
import threading
import time

a = "\033[1;30m"
m = "\033[1;31m"
h = "\033[1;32m"
k = "\033[1;33m"
c = "\033[1;36m"
p = "\033[1;37m"
r = "\033[0m"

PKG_PACKAGES = [
    "libjpeg-turbo",
    "termux-api",
    "bash",
    "zlib",
    "freetype",
    "clang",
    "python",
    "mpv",
]

PIP_PACKAGES = [
    ("requests", "requests"),
    ("beautifulsoup4", "bs4"),
    ("urllib3", "urllib3"),
    ("rich", "rich"),
    ("wcwidth", "wcwidth"),
    ("phonenumbers", "phonenumbers"),
    ("pillow", "PIL"),
    ("pycryptodome", "Crypto"),
]


def run(cmd, cwd=None):
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=cwd
    )


def pkg_installed(package):
    r = run(["dpkg", "-s", package])
    return (
        r.returncode == 0
        and "Status: install ok installed" in r.stdout
    )


def pip_installed(import_name):
    return subprocess.run(
        [sys.executable, "-c", f"import {import_name}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    ).returncode == 0


def overwrite(text, newline=False):
    end = "\n" if newline else ""
    sys.stdout.write(f"\r\033[K{text}{end}")
    sys.stdout.flush()

def animate(label, stop_event):
    dots = [
        "     ",
        ".    ",
        "..   ",
        "...  ",
        ".... ",
        "....."
    ]

    i = 0

    while not stop_event.is_set():
        overwrite(
            f"  {p}[{h}>{p}] {label}{m}{dots[i % len(dots)]}"
        )
        i += 1
        time.sleep(0.1)

def with_animation(label, task):
    stop = threading.Event()

    t = threading.Thread(
        target=animate,
        args=(label, stop),
        daemon=True
    )

    t.start()

    try:
        result = task()
    finally:
        stop.set()
        t.join()

    return result


def handle_pkg(package):
    installed = with_animation(
        f"Mengecek Package {package}",
        lambda: pkg_installed(package)
    )

    if installed:
        overwrite(
            f"  {p}[{h}>{p}] Package {package} Terdeteksi",
            newline=True
        )
        return

    success = with_animation(
        f"Mendownload Package {package}",
        lambda: (
            subprocess.run(
                ["pkg", "install", "-y", package],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            ),
            pkg_installed(package)
        )[1]
    )

    if success:
        overwrite(
            f"{p}  [{h}>{p}] Package {package} Terdeteksi",
            newline=True
        )
    else:
        overwrite(
            f"{p}  [{m}>{p}] Package {package} Gagal Diinstall!",
            newline=True
        )
        sys.exit(1)


def handle_pip(display, import_name):
    installed = with_animation(
        f"Mengecek Package {display}",
        lambda: pip_installed(import_name)
    )

    if installed:
        overwrite(
            f"{p}  [{h}>{p}] Package {display} Terdeteksi",
            newline=True
        )
        return

    pkg_name = (
        "pillow<11"
        if display.lower() == "pillow"
        else display
    )

    success = with_animation(
        f"Mendownload Package {display}",
        lambda: (
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--quiet",
                    "--break-system-packages",
                    pkg_name
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            ),
            pip_installed(import_name)
        )[1]
    )

    if success:
        overwrite(
            f"{p}  [{h}>{p}] Package {display} Terdeteksi",
            newline=True
        )
    else:
        overwrite(
            f"{p}  [{m}>{p}] Package {display} Gagal Diinstall!",
            newline=True
        )
        sys.exit(1)


def banner():
    os.system("clear")
    print(f"""{a}
╭─────────────────────────────────────────────────────────────╮
│{p} Ini lagi proses pengecekan kebutuhan untuk menjalank Script {a}│
│{p} Jadi ga usah nanya nanya ke Admin. Tungguin aja sampai peng {a}│
│{p} ecekan Selesai!                                             {a}│
╰─────────────────────────────────────────────────────────────╯
""")


def check_update(script_dir):
    result = with_animation(
        "Memeriksa Pembaruan",
        lambda: run(["git", "pull"], cwd=script_dir)
    )

    if result.returncode != 0:
        overwrite(
            f"{p}  [{m}>{p}] Gagal Memeriksa Pembaruan!",
            newline=True
        )
        return

    output = (
        result.stdout.lower()
        + result.stderr.lower()
    )

    if "already up to date" in output:
        overwrite(
            f"{p}  [{h}>{p}] Tidak Ada Pembaruan",
            newline=True
        )
    else:
        overwrite(
            f"{p}  [{h}>{p}] Pembaruan Berhasil",
            newline=True
        )


def main():
    script_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    for pkg in PKG_PACKAGES:
        handle_pkg(pkg)

    for display, imp in PIP_PACKAGES:
        handle_pip(display, imp)

    check_update(script_dir)

    print(f"{p}  [{h}>{p}] Menjalankan Script Utama")

    main_pyc = os.path.join(
        script_dir,
        "Spammer.py"
    )

    if not os.path.exists(main_pyc):
        print(
            f"{p}  [{m}>{p}] File{h} Spammer.py {p}tidak ditemukan!"
        )
        sys.exit(1)

    os.execv(
        sys.executable,
        [sys.executable, main_pyc]
    )


if __name__ == "__main__":
    banner()
    main()
