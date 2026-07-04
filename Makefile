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
	@printf "$(P)[$(H)?$(P)]$(R) Mengecek lingkungan$(M)...$(R)\n"
	@if [ -f "$(TERMUX_PATH)" ]; then \
		printf "$(P)[$(H)✓$(P)]$(R) Termux terdeteksi!\n"; \
		OS_TYPE="termux"; \
	elif [ -f "/etc/debian_version" ]; then \
		grep -qi ubuntu /etc/os-release && OS_TYPE="ubuntu" || OS_TYPE="debian"; \
		printf "$(P)[$(H)✓$(P)]$(R) $$OS_TYPE terdeteksi!\n"; \
	else \
		printf "$(P)[$(M)!$(P)]$(R) OS tidak didukung!\n"; \
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