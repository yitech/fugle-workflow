import argparse
import time
from datetime import datetime, timedelta
from scripts.utils import Utils
from loguru import logger

def validate_date(date_str: str):
    """Validates that the input is a valid date."""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: '{date_str}'. Expected format: YYYY-MM-DD")

def main(from_date: str, to_date: datetime, symbol: datetime, dry_run: bool):
    logger.info(f"Fetching data for symbol: {symbol} from {from_date} to {to_date}")
    # Your logic to insert historical klines here
    client = Utils()
    status_code, response = client.get(Utils.POSTREST_URL, 
                                        "/market_metadata", 
                                        {
                                            "select": "symbol",
                                            "symbol": f"eq.{symbol}"
                                        })
    if status_code > 299 or len(response) == 0:
        logger.error("Failed to fetch metadata")
        return
    date = from_date
    delta = timedelta(days=14)
    while date < to_date:
        next_date = min(date + delta, to_date)
        logger.info(f"Fetching data from {date.strftime('%Y-%m-%d')} to {next_date.strftime('%Y-%m-%d')}")
        status_code, response = client.get(Utils.FUGLE_URL, "/api/v1/historical/candles", {
            "symbol": symbol,
            "from_date": date.strftime('%Y-%m-%d'),
            "to_date": next_date.strftime('%Y-%m-%d')
        })
        time.sleep(1) # 60 requests per minute
        if status_code > 299:
            logger.error(f"Failed to fetch candles, status code: {status_code}, {response}")
            return
        if not dry_run:        
            for data in response['data'][::-1]:
                # Insert data into the database
                client.post(Utils.POSTREST_URL, "/klines", {
                    "symbol": symbol,
                    "date": data['date'],
                    "open": data['open'],
                    "high": data['high'],
                    "low": data['low'],
                    "close": data['close'],
                    "volume": data['volume'],
                })
                time.sleep(0.1)
        logger.info(f"Inserting data {len(response['data'])} into the database")
        date = next_date + timedelta(days=1)
        
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Insert historical klines data into the database.")
    
    parser.add_argument('--from_date', required=True, type=validate_date, help="Start date in YYYY-MM-DD format.")
    parser.add_argument('--to_date', required=True, type=validate_date, help="End date in YYYY-MM-DD format.")
    parser.add_argument('--symbol', required=True, type=str, help="Symbol to fetch data for.")
    parser.add_argument('--dry_run', action='store_true', help="If set, no data will be inserted into the database.")
    args = parser.parse_args()
    
    main(args.from_date, args.to_date, args.symbol, args.dry_run)
