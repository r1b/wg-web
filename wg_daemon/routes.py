from flask_resty import Api

from . import app, views


api = Api(app, prefix="/api/v1")


api.add_resource("/sync/", views.SyncView)
