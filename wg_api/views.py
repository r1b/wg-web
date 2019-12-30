import operator

from flask_resty import (
    ColumnFilter,
    Filtering,
    GenericModelView,
    NoOpAuthorization,
    Sorting,
)

from . import auth, models, schemas

# -----------------------------------------------------------------------------


class WgViewBase(GenericModelView):
    authentication = auth.BearerAuthentication()
    authorization = NoOpAuthorization()


# -----------------------------------------------------------------------------


class InterfaceViewBase(WgViewBase):
    model = models.Interface
    schema = schemas.InterfaceSchema()


class InterfaceListView(InterfaceViewBase):
    filtering = Filtering(name=ColumnFilter(operator.eq, required=True))
    sorting = Sorting("id", default="-id")

    def get(self):
        return self.list()

    def post(self):
        return self.create()


class InterfaceView(InterfaceViewBase):
    def get(self, id):
        return self.retrieve(id)

    def delete(self, id):
        return self.destroy(id)


# -----------------------------------------------------------------------------


class InterfaceAddressViewBase(WgViewBase):
    model = models.InterfaceAddress
    schema = schemas.InterfaceAddressSchema()


class InterfaceAddressListView(InterfaceAddressViewBase):
    sorting = Sorting("id", default="-id")

    def get(self):
        return self.list()

    def post(self):
        return self.create()


class InterfaceAddressView(InterfaceAddressViewBase):
    def get(self, id):
        return self.retrieve(id)

    def delete(self, id):
        return self.destroy(id)


# -----------------------------------------------------------------------------


class PeerViewBase(WgViewBase):
    model = models.Peer
    schema = schemas.PeerSchema()


class PeerListView(PeerViewBase):
    filtering = Filtering(name=ColumnFilter(operator.eq, required=True))
    sorting = Sorting("id", default="-id")

    def get(self):
        return self.list()

    def post(self):
        return self.create()


class PeerView(PeerViewBase):
    def get(self, id):
        return self.retrieve(id)

    def delete(self, id):
        return self.destroy(id)


# -----------------------------------------------------------------------------


class PeerAddressViewBase(WgViewBase):
    model = models.PeerAddress
    schema = schemas.PeerAddressSchema()


class PeerAddressListView(PeerAddressViewBase):
    sorting = Sorting("id", default="-id")

    def get(self):
        return self.list()

    def post(self):
        return self.create()


class PeerAddressView(PeerAddressViewBase):
    def get(self, id):
        return self.retrieve(id)

    def delete(self, id):
        return self.destroy(id)
