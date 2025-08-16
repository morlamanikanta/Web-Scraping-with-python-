# IPL Auction Scraper

This Python script scrapes player auction data from the official IPL website and saves it to an Excel file.

## Features
- Fetches IPL 2024 auction data directly from the IPL website.
- Parses table headers and player details using BeautifulSoup.
- Outputs the data in a structured Excel file for easy analysis.

## Requirements
- Python 3.x
- Requests
- BeautifulSoup4
- pandas

## How to Use
1. Clone this repository or download the script.
2. Install required packages:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```
3. Run the script:
   ```bash
   python ipl-auction.py
   ```
4. The Excel file will be saved as `web scraping.xlsx` in the specified directory.

## Note
- Update the URL or file path in the script if needed for different auction years or output locations.
