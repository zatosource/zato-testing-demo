.PHONY: install test clean

VENV := .venv
PYTHON := $(VENV)/bin/python

install:
	@rm -rf $(VENV)
	@uv venv $(VENV)
	@uv pip install -e ".[dev]" --python $(VENV)/bin/python
	@echo ""
	@echo "  \033[92m✓\033[0m  Installation complete"
	@echo ""

test: install
	@PYTHONPATH=$(CURDIR)/src $(PYTHON) -m pytest tests/ -p no:terminal

clean:
	@rm -rf $(VENV) build/ dist/ *.egg-info src/*.egg-info .pytest_cache/
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo ""
	@echo "  \033[92m✓\033[0m  Cleaned"
	@echo ""
