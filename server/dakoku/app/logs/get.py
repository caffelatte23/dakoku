import json

from .utils import *


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
