from io import StringIO
from tempfile import TemporaryFile

from flask_resty import ApiError

from . import wg_quick_wrapper as wg_quick
from . import wg_wrapper as wg


def is_interface(show_entry):
    return len(show_entry) == 5


# XXX: We can't use configparser here https://bugs.python.org/issue12662
# FIXME: `wg-quick strip` when talking to `wg`
def ini_lines(interface):
    yield "[Interface]"

    for address in interface["addresses"]:
        yield f"Address={address}"

    yield f"ListenPort={interface['listen_port']}"
    yield f"PrivateKey={interface['private_key']}"
    yield (
        # We want to recover this config if the interface goes down
        "SaveConfig=true"
    )

    yield ""

    for peer in interface["peers"]:
        yield "[Peer]"
        yield f"PublicKey={peer['public_key']}"
        yield f"AllowedIPs={', '.join([address for address in peer['addresses']])}"
        yield ""


# ----------------------------------------------------------------------------


def wg_show():
    try:
        show_output = StringIO(wg.show())  # FIXME: Maybe have to decode utf-8
    except wg.WgError as e:
        # TODO: Log stuff on WgError
        raise ApiError(500, {"message": "Failed to retrieve stats"}) from e

    results = []
    current_interface = None

    while True:
        raw_entry = show_output.readline()

        if raw_entry == "":
            break

        entry = raw_entry.split("\t")

        if is_interface(entry):
            interface_name, private_key, public_key, listen_port, fwmark = entry

            if current_interface is not None:
                results.append(current_interface)

            current_interface = {
                "name": interface_name,
                "private_key": private_key,
                "public_key": public_key,
                "listen_port": int(listen_port),
                "fwmark": fwmark,
                "peers": [],
            }
        else:
            (
                _,
                public_key,
                preshared_key,
                endpoint,
                allowed_ips,
                latest_handshake,
                transfer_rx,
                transfer_tx,
                persistent_keepalive,
            ) = entry

            current_interface["peers"].append(
                {
                    "public_key": public_key,
                    "preshared_key": preshared_key,
                    "endpoint": endpoint,
                    "allowed_ips": allowed_ips.split(","),
                    "latest_handshake": latest_handshake,
                    "transfer_rx": transfer_rx,
                    "transfer_tx": transfer_tx,
                    "persistent_keepalive": persistent_keepalive,
                }
            )

    return {"interfaces": results}


# ----------------------------------------------------------------------------


def wg_syncconf(config_data):
    interface = config_data["interface"]
    interface_name = interface["name"]

    # FIXME: For `SaveConfig` to work this needs to be in `/etc/wireguard/`
    with TemporaryFile() as ini_file:
        ini_file.write("\n".join(ini_lines(interface)))

        try:
            wg.syncconf(interface_name, ini_file)
        except wg.WgError as e:
            # TODO: Log stuff on WgError
            raise ApiError(
                422,
                {
                    "message": "Failed to sync configuration",
                    "interface": interface_name,
                },
            ) from e


# ----------------------------------------------------------------------------


def wg_quick_down(interface_name):
    try:
        wg_quick.down(interface_name)
    except wg_quick.WgQuickError as e:
        raise ApiError(
            422,
            {"message": "Failed to bring interface down", "interface": interface_name},
        ) from e


def wg_quick_up(interface_name):
    try:
        wg_quick.up(interface_name)
    except wg_quick.WgQuickError as e:
        raise ApiError(
            422,
            {"message": "Failed to bring interface up", "interface": interface_name},
        ) from e
