from io import BytesIO
import requests
import pandas as pd

URL = "https://docs.google.com/spreadsheets/d/1Hpz4QPcMyYzDmkOUwVjiWYhAgH6MnTfc6zCit0e290M/edit#gid=1576825517"
result_filename = "Result.csv"


_path = 'https://docs.google.com/spreadsheet/ccc?key=' + URL.split('/')[-2] + '&output=csv'
if '=' in URL:
    _gid = URL.split('=')[-1]
    _path += '&gid=' + _gid
    
print(_path)
df = pd.read_csv(BytesIO(requests.get(_path).content))
print(df)
df.to_csv(result_filename, index=None, header=True)
