#!/bin/sh

python -m pip install --upgrade twine

python setup.py sdist bdist_wheel

python -m twine upload --repository pypi dist/*