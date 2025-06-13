import yfinance as yf
import json
import boto3
from datetime import datetime
import pytz

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'data-hackathon-smit-saad'
    now = datetime.now(pytz.UTC)
    symbols = ['AAPL', 'MSFT', 'GOOGL']  # Short list for demo

    for symbol in symbols:
        data = yf.download(tickers=symbol, interval='1m', period='1d')
        if not data.empty:
            latest = data.iloc[-1]
            output = {
                "timestamp": now.isoformat(),
                "source": "Yahoo Finance",
                "symbol": symbol,
                "ohlcv": {
                    "open": float(latest['Open']),
                    "high": float(latest['High']),
                    "low": float(latest['Low']),
                    "close": float(latest['Close']),
                    "volume": int(latest['Volume'])
                },
                "status": "success"
            }
            path = f"raw/yahoofinance/{now.strftime('%Y/%m/%d/%H%M')}_{symbol}.json"
            s3.put_object(
                Bucket=bucket,
                Key=path,
                Body=json.dumps(output)
            )
