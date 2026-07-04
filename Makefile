P = \033[1;37m   # Putih
H = \033[1;32m   # Hijau
M = \033[1;31m   # Merah
K = \033[1;33m   # Kuning
B = \033[1;34m   # Biru
U = \033[1;35m   # Ungu
C = \033[1;36m   # Cyan
R = \033[0m      # Reset

TERMUX_PATH := /data/data/com.termux/files/usr/bin/bash

detectCLI:
	@echo "{P}[{H}?{P}] Mengecek lingkungan{M}..."
	@if [ -f "$(TERMUX_PATH)" ]; then \
		echo "{P}[{H}✓{P}] Termux terdeteksi!"; \
		OS_TYPE="termux"; \
	elif [ -f "/etc/debian_version" ]; then \
		grep -qi ubuntu /etc/os-release && OS_TYPE="ubuntu" || OS_TYPE="debian"; \
		echo "{P}[{H}✓{P}] $$OS_TYPE terdeteksi!"; \
	else \
		echo "{P}[{M}!{P}] OS tidak didukung!"; \
		exit 1; \
	fi; \
	echo $$OS_TYPE > .os_type

run:
	@python cl.py

fix: detectCLI
	@OS_TYPE=$$(cat .os_type); \
	if [ "$$OS_TYPE" = "termux" ]; then \
		pip uninstall requests -y; \
		pip uninstall psutil -y; \
		pip install requests; \
		pip install "urllib3<2"; \
		bash python313.sh; \
	else \
		. venv/bin/activate && \
		pip uninstall requests -y && \
		pip uninstall psutil -y && \
		pip install requests && \
		pip install "urllib3<2"; \
	fi