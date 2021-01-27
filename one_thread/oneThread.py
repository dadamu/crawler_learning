import requests
from io import StringIO
import pandas as pd
import numpy as np
import datetime
import time

start = datetime.date(2013, 1, 2)
end = datetime.date(2013, 1, 5)
current = start

while(end>current):
    dateformat = current.strftime("%Y%m%d")
    # 下載股價
    r = requests.post(
        'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + dateformat + '&type=ALL')

    # 整理資料，變成表格
    df = pd.read_csv(StringIO(r.text.replace("=", "")),
                     header=["證券代號" in l for l in r.text.split("\n")].index(True)-1)

    # 整理一些字串：
    df = df.apply(lambda s: pd.to_numeric(s.astype(str).str.replace(
        ",", "").replace("+", "1").replace("-", "-1"), errors='coerce'))
    print(df)
    time.sleep(2)
    current = current + datetime.timedelta(days=1)

