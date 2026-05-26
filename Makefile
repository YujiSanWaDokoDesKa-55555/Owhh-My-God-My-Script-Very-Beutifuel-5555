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

