import os
import dotenv

dotenv.load_dotenv()

debug = os.environ.get("DEBUG", False) == 'True'
DEBUG = debug

from .settings_release import *
# if debug:
#     from .settings_debug import *
# else:
#     from .settings_release import *
