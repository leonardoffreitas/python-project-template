export SIMPLE_SETTINGS=settings.base

install:
	@pip install -r requirements.txt

run:
	@python3 main.py -h
