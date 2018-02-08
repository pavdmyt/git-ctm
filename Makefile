OK_COLOR=\033[32;01m
NO_COLOR=\033[0m

.PHONY: build

name=ctm.py

flake:
	@echo "$(OK_COLOR)==> Linting code ...$(NO_COLOR)"
	@flake8 .

lint:
	@echo "$(OK_COLOR)==> Linting code ...$(NO_COLOR)"
	@pylint setup.py $(name) -rn -f colorized

isort-all:
	isort -rc --atomic --verbose setup.py $(name)

install-dev:
	@pip install -r requirements.txt
	@pip install -r requirements-dev.txt

clean-pyc:
	@echo "$(OK_COLOR)==> Cleaning bytecode ...$(NO_COLOR)"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

rm-build:
	@rm -rf build dist .egg $(name).egg-info

# requires docutils and pygments to be installed
# -s stands for strict (raises errors instead of warnings)
check-rst:
	@python setup.py check --restructuredtext -s

build: rm-build
	@echo "$(OK_COLOR)==> Building sdist and bdist_wheel $(NO_COLOR)"
	@python setup.py sdist
	@python setup.py bdist_wheel --universal

build-pex: rm-build build
	@echo "$(OK_COLOR)==> Building PEX $(NO_COLOR)"
	@./build_pex.sh


publish: flake check-rst rm-build
	@echo "$(OK_COLOR)==> Publishing...$(NO_COLOR)"
	@python setup.py sdist upload -r pypi
	@python setup.py bdist_wheel --universal upload -r pypi
