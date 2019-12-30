from flask_resty import Api

from . import app, views

api = Api(app, prefix="/api/v1")


api.add_resource("/wg/show/", views.ConfigurationShowView)
api.add_resource("/wg/syncconf/", views.ConfigurationSyncView)
api.add_resource("/wg-quick/up/", views.InterfaceUpView)
api.add_resource("/wg-quick/down/", views.InterfaceDownView)
