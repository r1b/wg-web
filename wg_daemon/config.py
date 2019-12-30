from subprocess import CalledProcessError
from tempfile import TemporaryFile

from flask_resty import ApiError

from . import wg_wrapper as wg

# XXX: We can't use configparser here https://bugs.python.org/issue12662
def get_ini_lines(interface):
    ini_lines = []

    ini_lines.append("[Interface]\n")

    for address in interface["addresses"]:
        ini_lines.append(f"Address={address}\n")

    ini_lines.append(f"ListenPort={interface['listen_port']}\n")
    ini_lines.append(f"PrivateKey={interface['private_key']}\n")
    ini_lines.append(
        # We want to recover this config if the interface goes down
        "SaveConfig=true\n"
    )

    ini_lines.append("\n")

    for peer in interface["peers"]:
        ini_lines.append("[Peer]\n")

        ini_lines.append(f"PublicKey={peer['public_key']}\n")

        ini_lines.append("AllowedIPs=")
        ini_lines.append(f"{', '.join([address for address in peer['addresses']])}\n")

        ini_lines.append("\n")

    return ini_data


def sync(config_data):
    interface = config_data["interface"]
    interface_name = interface["name"]

    with TemporaryFile() as ini_file:
        ini_file.writelines(get_ini_lines(interface))

        try:
            wg.syncconf(interface_name, ini_file)
        except CalledProcessError as e:
            raise ApiError(
                422,
                {
                    "message": "Failed to sync configuration",
                    "interface": interface_name,
                    "command": e.command,
                    "returncode": e.returncode,
                    "stdout": e.stdout,
                    "stderr": e.stderr,
                },
            )
