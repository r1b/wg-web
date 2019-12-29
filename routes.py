from flask_resty import Api

from . import app, views

api = Api(app, prefix="/api/v1")

api.add_resource("/interfaces/", views.InterfaceListView, views.InterfaceView)
api.add_resource(
    "/interfaces/<id>/addresses/",
    views.InterfaceAddressListView,
    views.InterfaceAddressView,
)
api.add_resource("/peers/", views.PeerListView, views.PeerView)
api.add_resource(
    "/peers/<id>/addresses/", views.PeerAddressListView, views.PeerAddressView
)
