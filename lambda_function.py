import json
import requests
import pandas as pd

def lambda_handler(event,context):
    print('Event data --> ', event)
    response = request.get('https://www.google.com/')
    print(response)

    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Demo Complete !!!!!')

