# Version package

PROJECT_HOME = "`pwd`"

help:
	@echo
	@echo "Please use 'make <target>' where <target> is one of"
	@echo

	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Clear *.pyc files, etc
	@rm -rf build dist *.egg-info
	@find . \( -name '*.pyc' -o  -name '__pycache__' -o -name '**/*.pyc' -o -name '*~' \) -delete

dist: clean ## Make dist
	@python setup.py sdist

publish: clean dist ## Make publish
	twine upload dist/*

test: ## Run tests
	nosetests --verbose --rednose  --nocapture --cover-package=ccvs_scanning_api_client --with-coverage
	coverage report -m
