# Rocklog
Webapp for scraping and saving rock.lt.

## Setup

1. Have Python 3.6+
2. Clone
3. `$ pip install -r requirements.txt`. This should install all the dependencies inclusing Django and Django-environ.
4. `$ python manage.py runserver`
5. Go to `localhost:8000`

## Additional Setup

- A webapp account for uploading new songs needs to be created.
- A Google app needs to be registered for login + YouTube access.

## Song Scraping

Each minute, a cron job triggers a Cloudflare Worker which scrapes the most recent song from rockfm.lt. Then that worker makes a GET request to Rocklog, with the song data base64 encoded as a URL parameter. An `Authorization: Basic` header is used to authenticate uploads as coming from Cloudflare.
