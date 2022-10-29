import json
import os

import boto3


def get_record(userId, date):

    table = boto3.resource('dynamodb').Table(os.environ["table"])
    response = table.get_item(
        Key={
            'userId': userId,
            'date': date
        }
    )
    return response["Item"] if "Item" in response.keys() else {
        'userId': userId,
        'date': date,
        "startTime": "",
        "endTime": '',
    }


def get_status(item):
    if item["startTime"] != "" and item["endTime"] == "":
        return "WORKING"
    else:
        return "NOT_WORKING"


def lambda_handler(event, context):
    query = event["queryStringParameters"]
    item = get_record(query["userId"], query["date"])

    item["status"] = get_status(item=item)

    return {
        "statusCode": 200,
        "body": json.dumps(item),
        "headers": {
            'Access-Control-Allow-Origin': "*"
        }
    }
