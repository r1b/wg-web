from subprocess import CalledProcessError, check_output

from . import settings


class WgQuickError(BaseException):
    def __init__(self, returncode, stdout, stderr):
        super("wg-quick returned a non-zero exit code")
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def run_wg_quick_command(command, *args):
    try:
        return check_output([settings.WG_QUICK_PATH, command, *args])
    except CalledProcessError as e:
        raise WgQuickError(e.returncode, e.stdout, e.stderr) from e


def up(interface_name):
    return run_wg_quick_command("up", interface_name)


def down(interface_name):
    return run_wg_quick_command("down", interface_name)
