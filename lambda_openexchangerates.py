import requests
import json
import boto3
from datetime import datetime
import pytz

def lambda_handler(event, context):
    app_id = "-------------------------"  # Replace this!
    url = f"https://openexchangerates.org/api/latest.json?app_id={app_id}"
    
    response = requests.get(url)
    result = response.json()
    
    now = datetime.now(pytz.UTC)
    s3 = boto3.client('s3')
    bucket = 'data-hackathon-smit-saad'
    key = f"raw/openexchangerates/{now.strftime('%Y/%m/%d/%H%M')}.json"
    
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps({
            "timestamp": now.isoformat(),
            "source": "OpenExchangeRates",
            "base": result.get("base"),
            "rates": result.get("rates"),
            "status": "success"
        })
    )
