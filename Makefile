.PHONY: fmt
fmt:
	python -m black api
	python -m isort api --profile=black