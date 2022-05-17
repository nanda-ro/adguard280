from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests
import datetime

URL_FORMAT = "https://280blocker.net/files/280blocker_domain_ag_{}{:0>2}.txt"

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def index():
    today = datetime.date.today()
    url = URL_FORMAT.format(today.year, today.month) # URLを生成
    response = requests.get(url)
    response.encoding = "UTF-8" # テキストエンコーディングが正しく返却されないので指定

    return response.text # 取得したリストをそのままテキスト形式で返却
