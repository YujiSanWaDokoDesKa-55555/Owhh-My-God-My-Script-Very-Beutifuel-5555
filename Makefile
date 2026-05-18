run:
	git pull
	python Spammer.pyc

update:
	git pull

id:
	git pull
	python id.pyc

install:
	pkg update -y && pkg upgrade -y && pkg install -y libjpeg-turbo zlib freetype clang python && pip install --upgrade pip setuptools wheel && pip install requests beautifulsoup4 urllib3 phonenumbers "pillow<11"
