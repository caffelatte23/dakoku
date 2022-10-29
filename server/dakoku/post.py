import json
import os
from datetime import datetime

import boto3

table = boto3.resource('dynamodb').Table(os.environ["table"])


def get_record(userId, date):
    response = table.get_item(
        Key={
            'userId': str(userId),
            'date': date
        }
    )
    return response["Item"] if "Item" in response.keys() else None


def lambda_handler(event, context):

    body = json.loads(event["body"])
    time = datetime.strptime(body["time"], "%Y-%m-%d %H:%M")

    item = get_record(body["userId"], time.strftime("%Y-%m-%d"))

    if item is not None:
        item["endTime"] = time.strftime("%H:%M")
    else:
        item = {
            'userId': body["userId"],
            'date': time.strftime("%Y-%m-%d"),
            "startTime": time.strftime("%H:%M"),
            "endTime": ''
        }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "hello world"}),
        "headers": {
            'Access-Control-Allow-Origin': "*"
        }
    }
