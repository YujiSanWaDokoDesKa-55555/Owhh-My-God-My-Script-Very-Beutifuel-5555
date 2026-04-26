run:
	@python Spammer.py

update:
	@git pull

install:
	@pkg install python pip git && pip install requests beautifulsoup4 urllib3
