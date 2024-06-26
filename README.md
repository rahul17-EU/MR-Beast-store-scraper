# MrBeast Store Scraper

This repository contains a Python script to scrape product information from the MrBeast store. The script uses Selenium and BeautifulSoup to extract data such as product name, color, and price. The data is then stored in a pandas DataFrame and exported to CSV files.

## Features

- **Web Scraping**: Uses Selenium and BeautifulSoup to navigate the website and extract product information.
- **Data Storage**: Stores the scraped data in pandas DataFrames.
- **CSV Export**: Exports the DataFrames to CSV files for further analysis.

## Requirements

To run the script, you need the following dependencies:

- Python 3.x
- BeautifulSoup
- Selenium
- Webdriver Manager for Chrome
- pandas

You can install the required libraries using:

```bash
pip install beautifulsoup4 selenium webdriver-manager pandas
