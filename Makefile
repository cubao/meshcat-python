all:
	@echo nothing special

install:
	python3 setup.py install

serve:
	cubao-meshcat-server --host 0.0.0.0 --port 8081