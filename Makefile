ci: clean create-venv2 build2


all : clean build2

clean: clean-build clean-pyc

clean-build:
		rm -fr build/
		rm -fr dist/
		rm -fr .eggs/
		find . -name '*.egg-info' -exec rm -fr {} +
		find . -name '*.egg' -exec rm -f {} +

clean-pyc:
		find . -name '*.pyc' -exec rm -f {} +
		find . -name '*.pyo' -exec rm -f {} +
		find . -name '*~' -exec rm -f {} +
		find . -name '__pycache__' -exec rm -fr {} +

install: clean
		python setup.py install

build3:
	    .venv3/bin/python setup.py bdist_egg

build2:
	    .venv2/bin/python setup.py bdist_egg

create-venv3:
		virtualenv --python=python3 .venv3
		.venv3/bin/pip3 install -r requirements.txt

create-venv2:
	virtualenv --python=python2 .venv2
	. .venv2/bin/activate
	pip install -r requirements.txt
