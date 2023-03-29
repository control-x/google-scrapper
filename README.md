# Google Scraper using ScrapingBee API

This script allows you to scrape Google search results using the ScrapingBee API. It takes a list of city names and search queries as input and generates a CSV file with the organic search results.

## Requirements

- Python 3.6 or higher
- A ScrapingBee API key


## Installation

### On Mac

1. Open Terminal on your Mac.
 
2. Check if you have Python 3.6 or higher installed by running the following command:
   ```
   python3 --version
   ```
   If you don't have Python 3.6 or higher, please download and install it from the official website: https://www.python.org/downloads/
3. Check if Git is installed by running the following command:
   ```
   git --version
   ```
   If Git is not installed, download and install it from the official website: https://git-scm.com/downloads
   Alternatively, you can install Git using Homebrew. If you don't have Homebrew installed, follow the instructions at https://brew.sh/ to install it. Once Homebrew is installed, run the following command to install Git:
   ```
   brew install git
   ```
4. Clone the repository using the following command:
   ```
   git clone https://github.com/control-x/google-scrapper
   ```
5. Change to the repository directory:
   ```
   cd google-scrapper
   ```

6. Install the required Python packages using the `REQUIREMENTS.txt` file:
   ```
   python3 -m pip install -r REQUIREMENTS.txt
   ```

## Usage

1. Prepare two CSV files: one for city names (e.g., `cities.csv`) and one for search queries (e.g., `search_queries.csv`). The search queries file can have a `%city` placeholder that will be replaced by city names from the cities file.

   Example `cities.csv`:
   ```
   New York
   Los Angeles
   Chicago
   ```

   Example `search_queries.csv`:
   ```
   best pizza in %city
   top attractions in %city
   ```

2. Run the script using Terminal with the following command:
   ```
   python3 scrape_google.py --city_file cities.csv --search_queries_file search_queries.csv --output_file output.csv --api_key YOUR_API_KEY
   ```
   Replace `YOUR_API_KEY` with your ScrapingBee API key.

3. The script will generate an output CSV file (e.g., `output.csv`) containing the organic search results for each city and search query combination.

## Troubleshooting

If you encounter any issues or need further assistance, please check the official Python and ScrapingBee documentation, or open an issue on this repository.
