from flask_resty import ApiError, HeaderAuthentication
from sqlalchemy.orm.exc import NoResultFound

from . import models


class BearerAuthentication(HeaderAuthentication):
    def authenticate_request(self, token):
        try:
            models.User.query.filter(token=token).one()
        except NoResultFound:
            raise ApiError(401, {"message": "Invalid credentials"})
