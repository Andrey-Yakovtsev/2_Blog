#!/bin/bash
set -e


echo 'Running migrations'
flask db upgrade

exec "$@"