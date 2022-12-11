import os

import boto3


def get_record(userId, date):

    table = boto3.resource('dynamodb').Table(os.environ["log_table"])
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
