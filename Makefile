### Defensive settings for make:
#     https://tech.davis-hansson.com/p/make/
SHELL:=bash
.ONESHELL:
.SHELLFLAGS:=-xeu -o pipefail -O inherit_errexit -c
.SILENT:
.DELETE_ON_ERROR:
MAKEFLAGS+=--warn-undefined-variables
MAKEFLAGS+=--no-builtin-rules

# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`

PLONE5=5.2-latest
PLONE6=6.0-latest

ifndef LOG_LEVEL
	LOG_LEVEL=INFO
endif
CURRENT_USER=$$(whoami)
USER_INFO=$$(id -u ${CURRENT_USER}):$$(getent group ${CURRENT_USER}|cut -d: -f3)

CODE_QUALITY_VERSION=2.0.0
LINT=docker run -e LOG_LEVEL="${LOG_LEVEL}" --rm -v "$(PWD)":/github/workspace plone/code-quality:${CODE_QUALITY_VERSION} check
FORMAT=docker run --user="${USER_INFO}" -e LOG_LEVEL="${LOG_LEVEL}" --rm -v "$(PWD)":/github/workspace plone/code-quality:${CODE_QUALITY_VERSION} format

PACKAGE_NAME=kitconcept.dsgvo
PACKAGE_PATH=src/
CHECK_PATH=setup.py $(PACKAGE_PATH)

all: build

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

bin/pip:
	@echo "$(GREEN)==> Setup Virtual Env$(RESET)"
	python3 -m venv .
	bin/pip install -U pip wheel

.PHONY: build-plone-5.2
build-plone-5.2: bin/pip ## Build Plone 5.2
	@echo "$(GREEN)==> Build with Plone 5.2$(RESET)"
	bin/pip install Plone plone.app.testing -c https://dist.plone.org/release/$(PLONE5)/constraints.txt
	bin/pip install -e ".[test]"
	bin/mkwsgiinstance -d . -u admin:admin

.PHONY: build-plone-6.0
build-plone-6.0: bin/pip ## Build Plone 6.0
	@echo "$(GREEN)==> Build with Plone 6.0$(RESET)"
	bin/pip install Plone plone.app.testing -c https://dist.plone.org/release/$(PLONE6)/constraints.txt
	bin/pip install -e ".[test]"
	bin/mkwsgiinstance -d . -u admin:admin

.PHONY: build
build: build-plone-6.0 ## Build Plone 6.0

.PHONY: clean
clean: ## Remove old virtualenv and creates a new one
	@echo "$(RED)==> Cleaning environment and build$(RESET)"
	rm -rf bin lib lib64 include share etc var inituser pyvenv.cfg .installed.cfg

.PHONY: format
format: format-black format-isort format-zpretty## Format the codebase according to our standards

.PHONY: format-black
format-black:  ## Format the codebase with black
	@echo "$(GREEN)==> Format codebase with black$(RESET)"
	$(FORMAT) black ${CODEPATH}

.PHONY: format-isort
format-isort:  ## Format the codebase with isort
	@echo "$(GREEN)==> Format codebase with isort$(RESET)"
	$(FORMAT) isort ${CODEPATH}

.PHONY: format-zpretty
format-zpretty:  ## Format the codebase with zpretty
	@echo "$(GREEN)==> Format codebase with zpretty$(RESET)"
	$(FORMAT) zpretty ${CODEPATH}

.PHONY: lint
lint: lint-isort lint-black lint-flake8 lint-zpretty ## check code style

.PHONY: lint-black
lint-black: ## validate black formating
	$(LINT) black ${CODEPATH}

.PHONY: lint-flake8
lint-flake8: ## validate black formating
	$(LINT) flake8 ${CODEPATH}

.PHONY: lint-isort
lint-isort: ## validate using isort
	$(LINT) isort ${CODEPATH}

.PHONY: lint-zpretty
lint-zpretty: ## validate ZCML/XML using zpretty
	$(LINT) zpretty ${CODEPATH}

# i18n
bin/i18ndude:	bin/pip
	@echo "$(GREEN)==> Install translation tools$(RESET)"
	bin/pip install i18ndude

.PHONY: i18n
i18n: bin/i18ndude ## Update locales
	@echo "$(GREEN)==> Updating locales$(RESET)"
	bin/update_locale

.PHONY: test
test: ## run tests
	PYTHONWARNINGS=ignore ./bin/zope-testrunner --auto-color --auto-progress --test-path $(PACKAGE_PATH)

.PHONY: start
start: ## Start a Plone instance on localhost:8080
	PYTHONWARNINGS=ignore ./bin/runwsgi etc/zope.ini
