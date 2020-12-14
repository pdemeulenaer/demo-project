lint:
	mypy src --ignore-missing-imports
	flake8 src --ignore=$(shell cat .flakeignore)

dev:
	pip install -e .

test: dev
	pytest --doctest-modules --junitxml=junit/test-results.xml
	bandit -r src -f xml -o junit/security.xml || true