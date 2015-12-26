import sys
import os

sys.path.insert(0,os.path.dirname(__file__))
import subprocess

activate_this = os.path.normpath(os.path.join(os.path.dirname(__file__),'../venv/bin/activate_this.py'))
execfile(activate_this, dict(__file__=activate_this))

from app import app as application
