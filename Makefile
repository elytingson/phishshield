.PHONY: install optional test

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

optional:
	pip install -r requirements-optional.txt

test:
	pytest -q
