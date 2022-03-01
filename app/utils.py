import json
import pandas as pd


def normalization(data_json):
  print(data_json)
  with open(f'{data_json}.json','r') as f:
    data = json.loads(f.read())
  df = pd.json_normalize(data, record_path=['data'])
  print(df.head(5))
  return df