from secrets import token_urlsafe

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from . import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "wg_users"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text, default=token_urlsafe, nullable=False)


class Interface(db.Model):
    __tablename__ = "wg_interfaces"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    host = db.Column(db.Text, nullable=False)
    port = db.Column(db.Integer, nullable=False)
    private_key = db.Column(db.Text, nullable=False)

    addresses = relationship("InterfaceAddress", backref="interface")

    @property
    def endpoint(self):
        return f"{self.host}:{self.port}"

    @endpoint.setter
    def endpoint(self, endpoint):
        self.host, self.port = endpoint.split(":")


class InterfaceAddress(db.Model):
    __tablename__ = "wg_interface_addresses"

    id = db.Column(db.Integer, primary_key=True)
    interface_id = db.Column(db.Integer, db.ForeignKey(Interface.id), nullable=False)

    address = db.Column(db.Text, nullable=False)
    mask = db.Column(db.Integer, nullable=False)

    @property
    def cidr(self):
        return f"{self.address}/{self.mask}"

    @cidr.setter
    def cidr(self, cidr):
        self.address, self.mask = cidr.split("/")


class Peer(db.Model):
    __tablename__ = "wg_peers"

    id = db.Column(db.Integer, primary_key=True)
    public_key = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text)

    addresses = relationship("PeerAddress", backref="peer")


class PeerAddress(db.Model):
    __tablename__ = "wg_peer_addresses"

    id = db.Column(db.Integer, primary_key=True)
    interface_id = db.Column(db.Integer, db.ForeignKey(Interface.id), nullable=False)
    peer_id = db.Column(db.Integer, db.ForeignKey(Peer.id), nullable=False)

    address = db.Column(db.Text, nullable=False)
    mask = db.Column(db.Integer, nullable=False)

    @property
    def cidr(self):
        return f"{self.address}/{self.mask}"

    @cidr.setter
    def cidr(self, cidr):
        self.address, self.mask = cidr.split("/")
