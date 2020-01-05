import os

IS_PRODUCTION = os.environ.get('IS_PRODUCTION')

if IS_PRODUCTION:
    from .conf.prod_server.settings import *
else:
    from .conf.dev_server.settings import *
