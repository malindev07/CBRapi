VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip


install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt


run:
	@echo "Запуск тестов"
	$(PYTHON) -m pytest -v tests/
	@echo "Запуск сервиса"
	$(PYTHON) main.py


