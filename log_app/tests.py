# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

# Create your tests here.
print os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
print (os.path.abspath(__file__))
print (os.path.abspath('log_file/log.txt'))