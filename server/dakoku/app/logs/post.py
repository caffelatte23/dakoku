import json
import os
from datetime import datetime

import boto3
from .utils import *

table = boto3.resource('dynamodb').Table(os.environ["log-table"])


def lambda_handler(event, context):

    body = json.loads(event["body"])
    time = datetime.strptime(body["time"], "%Y-%m-%d %H:%M")

    item = get_record(body["userId"], time.strftime("%Y-%m-%d"))

    if body["IsAttend"]:
        item = {
            'userId': body["userId"],
            'date': time.strftime("%Y-%m-%d"),
            "startTime": time.strftime("%H:%M"),
            "endTime": ''
        }
    else:
        item["endTime"] = time.strftime("%H:%M")

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "hello world"}),
        "headers": {
            'Access-Control-Allow-Origin': "*"
        }
    }
