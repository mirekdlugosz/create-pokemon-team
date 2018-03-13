#!/usr/bin/env python3
from api import app


application = app.create('settings')
application.run(port=application.config["PORT"])
