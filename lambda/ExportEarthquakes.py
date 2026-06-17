import boto3
import json

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

table = dynamodb.Table('Earthquakes')

def lambda_handler(event, context):

    response = table.scan()

    data = response['Items']

    s3.put_object(
        Bucket='jon-earthquakes-2026',
        Key='earthquakes.json',
        Body=json.dumps(data, default=str),
        ContentType='application/json'
    )

    return {
        'statusCode': 200,
        'items': len(data)
    }
