from marshmallow import Schema, fields


class PeerSchema(Schema):
    public_key = fields.String(required=True)
    addresses = fields.List(fields.String(), required=True)


class InterfaceSchema(Schema):
    name = fields.String(required=True)
    listen_port = fields.String(required=True)
    private_key = fields.String(required=True)

    addresses = fields.List(fields.String(), required=True)
    peers = fields.Nested(PeerSchema(), required=True)


class SyncSchema(Schema):
    interface = fields.Nested(InterfaceSchema(), required=True)
