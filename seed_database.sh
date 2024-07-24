#!/bin/bash

rm db.sqlite3
rm -rf ./choreapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations choreapi
python3 manage.py migrate choreapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata households
python3 manage.py loaddata HouseholdMembers
python3 manage.py loaddata feed
# python3 manage.py loaddata chores

