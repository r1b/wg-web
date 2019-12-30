from subprocess import check_output
from . import settings


def syncconf(interface_name, config_file):
    check_output([settings.WG_PATH, "syncconf", interface_name, config_file])
