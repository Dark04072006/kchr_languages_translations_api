#!/bin/bash

export DB_URL=files/kchr_translations.db
export SECRET_KEY=REQUIRED

source .venv/bin/activate
cd src
exec gunicorn -w 4 'app.main.__main__:create_app()'
