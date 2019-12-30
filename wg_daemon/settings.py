import os
import sys

WG_PATH = os.environ.get("WG_PATH")

# TODO: Is this even right lol
if WG_PATH is None:
    if sys.platform == "win32":
        WG_PATH = "C:\\Program Files\\WireGuard\\wg.exe"
    else:
        WG_PATH = "/usr/bin/wg"
