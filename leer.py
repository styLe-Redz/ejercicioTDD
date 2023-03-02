# Funcion Lambda 1

import json
import boto3
from datetime import datetime
from urllib.request import urlopen

def lambda_handler(event, context):

    url = "https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario"
    
    with urlopen(url) as response:
        body = response.read()
    
    boto3.client('s3').put_object(Body=body,Bucket='dolar-raw-1032498680-v2',Key="archivo.txt")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }