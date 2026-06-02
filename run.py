import subprocess
import sys
import os
import threading
import time

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
    ("requests",       "requests"),
    ("beautifulsoup4", "bs4"),
    ("urllib3",        "urllib3"),
    ("rich",           "rich"),
    ("wcwidth",        "wcwidth"),
    ("phonenumbers",   "phonenumbers"),
    ("pillow",         "PIL"),
]


def run(cmd, cwd=None):
    return subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)


def pkg_installed(package):
    r = run(["dpkg", "-s", package])
    return r.returncode == 0 and "Status: install ok installed" in r.stdout


def pip_installed(import_name):
    return run([sys.executable, "-c", f"import {import_name}"]).returncode == 0


def overwrite(text, newline=False):
    end = "\n" if newline else ""
    sys.stdout.write(f"\r\033[K{text}{end}")
    sys.stdout.flush()


def animate(label, stop_event):
    dots = ["   ", ".  ", ".. ", "..."]
    i = 0
    while not stop_event.is_set():
        overwrite(f"[>] {label}{dots[i % len(dots)]}")
        i += 1
        time.sleep(0.3)


def with_animation(label, task):
    stop = threading.Event()
    t = threading.Thread(target=animate, args=(label, stop))
    t.start()
    result = task()
    stop.set()
    t.join()
    return result


def handle_pkg(package):
    installed = with_animation(f"Mengecek Package {package}", lambda: pkg_installed(package))
    if installed:
        overwrite(f"[>] Package {package} Terdeteksi", newline=True)
    else:
        success = with_animation(f"Mendownload Package {package}", lambda: (
            subprocess.run(["pkg", "install", "-y", package], capture_output=True, text=True),
            pkg_installed(package)
        )[1])
        if success:
            overwrite(f"[>] Package {package} Terdeteksi", newline=True)
        else:
            overwrite(f"[>] Package {package} Gagal Diinstall!", newline=True)
            sys.exit(1)


def handle_pip(display, import_name):
    installed = with_animation(f"Mengecek Package {display}", lambda: pip_installed(import_name))
    if installed:
        overwrite(f"[>] Package {display} Terdeteksi", newline=True)
    else:
        pkg = "pillow<11" if display.lower() == "pillow" else display
        success = with_animation(f"Mendownload Package {display}", lambda: (
            subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", pkg], capture_output=True, text=True),
            pip_installed(import_name)
        )[1])
        if success:
            overwrite(f"[>] Package {display} Terdeteksi", newline=True)
        else:
            overwrite(f"[>] Package {display} Gagal Diinstall!", newline=True)
            sys.exit(1)


def jembut():
    os.system("clear")
    print("""
Ini lagi proses pengecekan bahan bahan Tools nya. Tungguin aja!
___________
""")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    subprocess.Popen(["pkg", "update", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for pkg in PKG_PACKAGES:
        handle_pkg(pkg)

    subprocess.Popen(
        [sys.executable, "-m", "pip", "install", "--quiet", "--upgrade", "pip", "setuptools", "wheel"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    for display, imp in PIP_PACKAGES:
        handle_pip(display, imp)

    with_animation("Memeriksa Pembaruan", lambda: run(["git", "pull"], cwd=script_dir))
    print("[>] Pembaruan Selesai")

    print("[>] Menjalankan Script Utama")

    main_pyc = os.path.join(script_dir, "Spammer.pyc")
    if not os.path.exists(main_pyc):
        print("[>] File Spammer.pyc tidak ditemukan!")
        sys.exit(1)

    os.execv(sys.executable, [sys.executable, main_pyc])


if __name__ == "__main__":
    jembut()
    main()
