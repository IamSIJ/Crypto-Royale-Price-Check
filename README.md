## Files

- `main.py` - Main application with scheduled price checking
- `get_data.py` - Fetches price data from CoinGecko API
- `api_ping.py` - Tests API connectivity
- `requirements.txt` - Python dependencies

## Setup

### Prerequisites

- Python 3.7+
- CoinGecko API key

### Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root:
   ```
   COINGECKO_API_KEY=your_api_key_here
   ```

3. Get a free API key from [CoinGecko](https://www.coingecko.com/en/api)

## Usage

### Test API Connection
```bash
python api_ping.py
```

### Fetch Current Price
```bash
python get_data.py
```

### Run Main Application
```bash
python main.py
```

## Dependencies

- **requests** - HTTP library for API calls
- **python-dotenv** - Environment variable management
- **pytz** - Timezone support

## API

Uses the CoinGecko API endpoint:
```
https://api.coingecko.com/api/v3/simple/price
```

Returns Crypto Royale price in USD with 24-hour change percentage.
