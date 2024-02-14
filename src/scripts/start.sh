#!/bin/bash

export DB_URL=REQUIRED
export SECRET_KEY=REQUIRED

exec python -m app.main
