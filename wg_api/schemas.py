from marshmallow import Schema, fields


class InterfaceAddressSchema(Schema):
    id = fields.Int(dump_only=True)
    interface_id = fields.Int(dump_only=True)

    cidr = fields.String(required=True)


class InterfaceSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.String(required=True)
    endpoint = fields.String(required=True)
    private_key = fields.String(required=True)

    addresses = fields.Nested(InterfaceAddressSchema())


class PeerAddressSchema(Schema):
    id = fields.Int(dump_only=True)
    interface_id = fields.Int(required=True)
    peer_id = fields.Int(dump_only=True)

    cidr = fields.String(required=True)


class PeerSchema(Schema):
    id = fields.Int(dump_only=True)

    public_key = fields.String(required=True)
    name = fields.String()

    addresses = fields.Nested(PeerAddressSchema())
