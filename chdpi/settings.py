import os
import dotenv

dotenv.load_dotenv()

debug = bool(os.environ.get("DEBUG", False))
DEBUG = debug
if debug:
    from .settings_debug import *
else:
    from .settings_release import *
