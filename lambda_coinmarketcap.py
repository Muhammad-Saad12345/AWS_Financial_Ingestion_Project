import requests
import json
import boto3
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

def lambda_handler(event, context):
    url = 'https://coinmarketcap.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    rows = soup.select('tbody tr')[:10]  # Top 10
    data = []
    
    for row in rows:
        try:
            name = row.select_one('p.sc-4984dd93-0.kKpPOn').text
            symbol = row.select_one('p.coin-item-symbol').text
            price = row.select_one('div.sc-a0353bbc-0 span').text.replace('$', '').replace(',', '')
            market_cap = row.select_one('span.sc-7bc56c81-0').text.replace('$', '').replace(',', '')
            
            data.append({
                "name": name,
                "symbol": symbol,
                "price_usd": float(price),
                "market_cap_usd": market_cap,
                "status": "success"
            })
        except:
            continue
    
    now = datetime.now(pytz.UTC)
    s3 = boto3.client('s3')
    bucket = 'data-hackathon-smit-saad'
    key = f"raw/coinmarketcap/{now.strftime('%Y/%m/%d/%H%M')}.json"
    
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps({
            "timestamp": now.isoformat(),
            "source": "CoinMarketCap",
            "data": data
        })
    )
