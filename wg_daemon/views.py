from flask_resty import ApiView

from . import controller, schemas

# TODO: Service auth


class ConfigurationShowView(ApiView):
    serializer = schemas.ConfigurationShowSchema()

    def get(self):
        return self.make_response(controller.wg_show())


class ConfigurationSyncView(ApiView):
    deserializer = schemas.ConfigurationSyncSchema()

    def post(self):
        controller.wg_syncconf(self.get_request_data())
        return self.make_empty_response()


class InterfaceDownView(ApiView):
    deserializer = schemas.InterfaceDownSchema()

    def post(self):
        controller.wg_quick_down(self.get_request_data()["interface"])
        return self.make_empty_response()


class InterfaceUpView(ApiView):
    deserializer = schemas.InterfaceUpSchema()

    def post(self):
        controller.wg_quick_up(self.get_request_data()["interface"])
        return self.make_empty_response()
