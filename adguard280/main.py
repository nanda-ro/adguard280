from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests
import datetime

URL_PREFIX = "https://280blocker.net/files/280blocker_domain_ag_"
URL_SUFFIX = ".txt"

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def index():
    today = datetime.date.today()
    url = "{}{}{:0>2}{}".format(URL_PREFIX, today.year, today.month, URL_SUFFIX)
    response = requests.get(url)
    response.encoding = "UTF-8"
    return response.text
