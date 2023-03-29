import requests
import click
import csv
import json
from urllib.parse import quote

from pprint import pprint


@click.command()
@click.option(
    "--city_file", required=True, help="Path to the CSV file containing city names."
)
@click.option(
    "--search_queries_file",
    required=True,
    help="Path to the CSV file containing search_queries.",
)
@click.option(
    "--output_file", default="output.csv", help="Path to the output CSV file."
)
@click.option("--api_key", required=True, help="Your ScrapingBee API key.")
@click.option("--nb_results", default=20, help="Number of results to scrape.")
@click.option("--language", default="fr", help="Language of the search results.")
def scrape_google(
    city_file, search_queries_file, output_file, api_key, nb_results, language
):
    api_url = f"https://app.scrapingbee.com/api/v1/store/google?api_key={api_key}&search={{}}&nb_results={nb_results}&language={language}"
    cities = read_csv(city_file)
    search_queries = read_csv(search_queries_file)

    with open(output_file, "w", newline="", encoding="utf-8") as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(
            ["City", "Title", "URL", "Position", "Description", "Search Query"]
        )

        for search_query in search_queries:
            for city in cities:
                search_query = search_query.replace("%city", city)
                print(f"Scraping '{search_query}'...")
                encoded_search_query = quote(search_query)
                response = requests.get(api_url.format(encoded_search_query))

                if response.status_code == 200:
                    json_data = json.loads(response.text)
                    organic_results = json_data["organic_results"]

                    for result in organic_results:
                        csv_writer.writerow(
                            [
                                city,
                                result.get("title", ""),
                                result.get("url", ""),
                                result.get("position", ""),
                                result.get("description", ""),
                                search_query,
                            ]
                        )
                    print(f"Done for query '{search_query}'")
                else:
                    print(f"Error {response.status_code} for query '{search_query}'")


def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        return [row[0] for row in reader]


if __name__ == "__main__":
    scrape_google()
