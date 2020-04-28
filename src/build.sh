#!/bin/bash
sudo apt -y install libftgl-dev

git clone https://github.com/mugwort-rc/python-ftgl
cd python-ftgl
python setup.py build
python3 setup.py build
sudo python setup.py install
sudo python3 setup.py install

