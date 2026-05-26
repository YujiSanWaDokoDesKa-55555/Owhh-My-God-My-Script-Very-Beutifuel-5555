# Warna ANSI
P = \033[1;37m   # Putih
H = \033[1;32m   # Hijau
M = \033[1;31m   # Merah
K = \033[1;33m   # Kuning
B = \033[1;34m   # Biru
U = \033[1;35m   # Ungu
C = \033[1;36m   # Cyan
R = \033[0m      # Reset

run:
	git pull
	@echo -e "$(H) #$(P) Wait Bro... $(M)!"
	python Spammer.pyc

update:
	git pull

id:
	git pull
	python id.pyc

install:
	pkg update -y && pkg upgrade -y && termux-setup-storage && pkg install -y libjpeg-turbo termux-api bash zlib freetype clang python && pip install --upgrade pip setuptools wheel && pip install requests beautifulsoup4 urllib3 wcwidth phonenumbers "pillow<11"
	@echo -e "$(P) Instalasi Selesai $(M)!"
	@echo -e "$(P) Ketik $(H)make run$(P) Untuk Menjalankan Tools$(R)"