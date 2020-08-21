from __future__ import absolute_import

# This is a switcher:
try:
    from develop import *  # or .dev if you want dev
    # from .product import *  # or .dev if you want dev
except ImportError:
    from .develop import *  # or .dev if you want dev
    # from product import *  # or .dev if you want dev

##### DJANGO SECRETS
SECRET_KEY = '9nneu#^7_aai*(#(6_qiihu-^k-+%a86&vjh=_i9#(c4^8s51n'
# DATABASES['default']['PASSWORD'] = 'scrtpsswd'

##### OTHER SECRETS