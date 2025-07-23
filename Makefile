VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip


install:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	@echo "Запуск сервиса"
	$(PYTHON) main.py


