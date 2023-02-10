import json
import random
import re
import string


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
