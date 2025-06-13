🚀 Serverless Financial Data Ingestion Project (AWS Lambda + EventBridge + S3)

This project demonstrates a **serverless data ingestion pipeline** built with AWS services and Python to collect financial datasets in near real-time.

## 📌 Problem Statement
Ingest and store financial data from multiple sources (Yahoo Finance, CoinMarketCap, Open Exchange Rates) every minute using serverless architecture.

---

## 🧰 Tech Stack
- **AWS Lambda** – Serverless compute
- **Amazon S3** – Raw data storage
- **Amazon EventBridge** – Scheduling triggers (every minute)
- **Python** – Data fetching, transformation, and formatting
  - `yfinance`
  - `requests`
  - `beautifulsoup4`

---

## 🔍 Data Sources
| Source | Details |
|--------|---------|
| Yahoo Finance | S&P 500 OHLCV data at minute level |
| CoinMarketCap | Top 10 cryptocurrencies (scraped) |
| Open Exchange Rates | Forex data using App ID |

---

## 📂 S3 Bucket Structure
```

s3://data-hackathon-smit-{yourname}/raw/{source}/YYYY/MM/DD/HHMM.{file-format}

```

Metadata included: timestamp, source, response status, symbol

---

## 🛠 Setup Instructions

1. Clone the repo  
2. Set up virtual environment and install dependencies  
3. Create zip files for Lambda layers (for external libraries)  
4. Create S3 bucket and set folder structure  
5. Deploy Lambda functions  
6. Set EventBridge rules (1-minute schedule)  
7. Monitor and validate S3 ingestion
