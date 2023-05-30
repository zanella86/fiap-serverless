import json
from sqsHandler import SqsHandler


def handler(event, context):
    print(json.dumps(event))
