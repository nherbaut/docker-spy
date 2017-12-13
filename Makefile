all : venv clean build buildp2

venv: .venv/bin/activate

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

build:
	    .venv/bin/python setup.py bdist_egg

buildp2:
	    .venvp2/bin/python setup.py bdist_egg

publish:
	   scp ./dist/Docker_Spy-0.0.2-py2.7.egg  nhelig:/home/nherbaut/vagrant-test/master/srv/salt/docker_spy/Docker_Spy-0.0.2-py2.7.egg
