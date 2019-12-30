from subprocess import CalledProcessError, check_output

from . import settings


class WgError(BaseException):
    def __init__(self, returncode, stdout, stderr):
        super("wg returned a non-zero exit code")
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def run_wg_command(command, *args):
    try:
        return check_output([settings.WG_PATH, command, *args])
    except CalledProcessError as e:
        raise WgError(e.returncode, e.stdout, e.stderr) from e


def show(*, interface="all", option="dump"):
    return run_wg_command("show", interface, option)


def syncconf(interface_name, config_file):
    return run_wg_command("syncconf", interface_name, config_file)
