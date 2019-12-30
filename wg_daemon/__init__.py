from flask import Flask
from . import settings

app = Flask(__name__)
app.config.from_object(settings)

8 from . import routes  # noqa: F401 isort:skip
