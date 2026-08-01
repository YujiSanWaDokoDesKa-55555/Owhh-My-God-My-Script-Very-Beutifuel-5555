import os
import sys
import tty
import time
import termios
import shutil
import subprocess
import atexit
import select

MIN_COLS = 63

a = "\033[1;30m"
m = "\033[1;31m"
h = "\033[1;32m"
k = "\033[1;33m"
c = "\033[1;36m"
p = "\033[1;37m"
r = "\033[0m"

def hide_cursor():
    print("\033[?25l", end="", flush=True)

def show_cursor():
    print("\033[?25h", end="", flush=True)

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

atexit.register(show_cursor)

def restore_terminal():
    try:
        termios.tcsetattr(
            fd,
            termios.TCSADRAIN,
            old_settings
        )
    except:
        pass

def get_key():
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None

def auto_update():
    try:
        with open(os.devnull, 'w') as devnull:
            result = subprocess.run(
                ["git", "remote", "-v"],
                stdout=subprocess.PIPE,
                stderr=devnull,
                text=True
            )
            
            if result.stdout.strip():
                subprocess.run(
                    ["git", "pull"],
                    stdout=devnull,
                    stderr=devnull,
                    check=False
                )
    except Exception:
        pass

auto_update()

os.system("clear")

try:
    tty.setcbreak(fd)
    hide_cursor()

    last_status = None

    while True:
        cols = shutil.get_terminal_size().columns

        if cols >= MIN_COLS:
            status = (
                "OK",
                f"""
\033[102m   {r} {p}Ukuran Layar {h}Sudah{p} Sesuai. Silahkan Klik Huruf Y"""
            )
        else:
            status = (
                "SMALL",
                f"""
\033[101m   {r} {p}Ukuran Layar {m}Belum{p} Sesuai. Silahkan Cubit Layar"""
            )

        if status != last_status:
            print("\033[2J\033[H", end="", flush=True)
            print(status[1], end="", flush=True)
            last_status = status

        if cols >= MIN_COLS:
            key = get_key()

            if key and key.lower() == "y":

                restore_terminal()
                show_cursor()

                print("\033[2J\033[H", end="", flush=True)

                import signal
                signal.signal(signal.SIGINT, signal.SIG_IGN)

                subprocess.run(
                    [sys.executable, "run.py"],
                    stdin=sys.stdin,
                    stdout=sys.stdout,
                    stderr=sys.stderr
                )

                signal.signal(signal.SIGINT, signal.SIG_DFL)
                sys.exit()

        time.sleep(0.05)

except KeyboardInterrupt:
    pass

finally:
    restore_terminal()
    show_cursor()