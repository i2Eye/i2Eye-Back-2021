.PHONY: fmt
fmt:
	python -m black . --exclude=.data/ --exclude=venv/
	python -m isort .