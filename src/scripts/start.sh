#!/bin/bash

export DB_URL=REQUIRED
export SECRET_KEY=REQUIRED

source .venv/bin/activate
cd src
exec gunicorn -w 4 'app.main.__main__:create_app()'
