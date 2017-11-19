"""
Create CSV from database items
"""
import io
import csv
import boto3


def lambda_handler(request, context):
    """
    Queries DynamoDB table based on index and key condition expression to convert data to CSV
    """
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(request['table'])

    items = []
    response = table.scan()

    items = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(
            ExclusiveStartKey=response['LastEvaluatedKey']
        )

        items.extend(response['Items'])

    keys = []

    for item in items:
        for key in list(item):
            if key not in keys:
                keys.append(key)


    output = io.StringIO()

    dict_writer = csv.DictWriter(output, keys, quoting=csv.QUOTE_NONNUMERIC)
    dict_writer.writeheader()
    dict_writer.writerows(items)

    s3 = boto3.client('s3')

    s3.put_object(
        Body=output.getvalue(),
        Bucket=request['bucket'],
        Key=request['key'])
