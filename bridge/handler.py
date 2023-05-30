import json
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime
from sqsHandler import SqsHandler


def allEventsHandler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('eventos-pizzaria')
    
    print("event ANTES: {}".format(json.dumps(event)))
    
    response = table.put_item(Item={
            'time': str(datetime.now()),
            'pedido': str(event['detail']['pedido']),
            'cliente': event['detail']['cliente'],
            'status': event['detail']['status']
    }, ReturnConsumedCapacity='TOTAL')
    print("event: {}".format(json.dumps(event)))
    
    return event
    
def readyHandler(event, context):
    print(json.dumps(event))

    sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/610798871504/espera-entrega")

    payload=event["detail"]
    print(json.dumps(payload))
    sqs.send(json.dumps(payload))

    return event