# Funcion Lambda 2

import json
import boto3
from datetime import datetime

def lambda_handler(event, context):

    dt = str(datetime.now())
    nombre = "dolar_" + dt[:10] + ".csv"
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('dolar-raw-1032498680-v2')
    obj = bucket.Object('archivo.txt')
    body = obj.get()['Body'].read()
    

    data = json.loads(body)
    
    s = "fecha,valor\n"
    
    for i in data:
        date = int(int(i[0])/1000)
        s = s + str(datetime.fromtimestamp(date)) +','+str(i[1]) + '\n'
            
    boto3.client('s3').put_object(Body=s,Bucket='dolar-final-103248680-v2',Key=nombre)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }