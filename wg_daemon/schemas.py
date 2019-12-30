from marshmallow import Schema, fields


class PeerSyncSchema(Schema):
    public_key = fields.String(required=True)
    addresses = fields.List(fields.String(), required=True)


class InterfaceSyncSchema(Schema):
    name = fields.String(required=True)
    listen_port = fields.String(required=True)
    private_key = fields.String(required=True)

    addresses = fields.List(fields.String(), required=True)
    peers = fields.List(fields.Nested(PeerSyncSchema(), required=True))


class ConfigurationSyncSchema(Schema):
    interface = fields.Nested(InterfaceSyncSchema(), required=True)


# ----------------------------------------------------------------------------


class PeerShowSchema(Schema):
    # FIXME: real types
    public_key = fields.String(required=True)
    preshared_key = fields.String(required=True)
    endpoint = fields.String(required=True)
    allowed_ips = fields.List(fields.String(), required=True)
    latest_handshake = fields.String(required=True)
    transfer_rx = fields.String(required=True)
    transfer_tx = fields.String(required=True)
    persistent_keepalive = fields.String(required=True)


class InterfaceShowSchema(Schema):
    name = fields.String(required=True)
    listen_port = fields.Int(required=True)
    private_key = fields.String(required=True)
    public_key = fields.String(required=True)

    peers = fields.List(fields.Nested(PeerShowSchema(), required=True))


class ConfigurationShowSchema(Schema):
    interfaces = fields.List(fields.Nested(InterfaceShowSchema()))
