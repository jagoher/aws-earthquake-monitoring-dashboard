import json
import urllib.request
from datetime import datetime

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Earthquakes')

lambda_client = boto3.client('lambda')

USGS_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
    "all_hour.geojson"
)

def lambda_handler(event, context):

    response = urllib.request.urlopen(USGS_URL)
    data = json.loads(response.read())

    count = 0

    for feature in data["features"]:

        props = feature["properties"]
        coords = feature["geometry"]["coordinates"]

        quake_id = feature["id"]

        item = {
            "quakeId": quake_id,
            "magnitude": str(props.get("mag", 0)),
            "place": str(props.get("place", "")),
            "time": str(props.get("time", "")),
            "updated": str(props.get("updated", "")),
            "longitude": str(coords[0]),
            "latitude": str(coords[1]),
            "depthKm": str(coords[2]),
            "url": str(props.get("url", "")),
            "loadedAt": datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)
        count += 1

    lambda_client.invoke(
        FunctionName='ExportEarthquakes',
        InvocationType='Event',
        Payload=json.dumps({"source": "IngestEarthquakes"})
    )

    return {
        "statusCode": 200,
        "itemsLoaded": count
    }
