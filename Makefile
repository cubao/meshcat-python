all:
	@echo nothing special

install:
	python3 setup.py install

serve:
	cubao-meshcat-server --host 0.0.0.0 --port 8081

build:
	python3 setup.py sdist

pypi_remote ?= pypi
upload:
	twine upload dist/*.tar.gz -r $(pypi_remote)

.PHONY: all install build serve
