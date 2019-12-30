from flask_resty import ApiView

from . import config, schemas


# TODO: Service auth
class SyncView(ApiView):
    schema = schemas.SyncSchema()

    def post(self):
        data = self.get_request_data()

        try:
            config.sync(data)
        except Exception as e:
            raise ApiError(422) from e

        return self.make_empty_response()
