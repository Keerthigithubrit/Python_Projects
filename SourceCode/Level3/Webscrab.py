# Import libraries
import requests
from bs4 import BeautifulSoup

# URL for scraping
url = "https://quotes.toscrape.com"

# Send HTTP request to website
response = requests.get(url)

# Check request
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text,'html.parser')

    # Find all links(<a> tags)
    links = soup.find_all("a")
    print("Extracted Links")

    for link in links:
        text = link.get_text(strip=True)
        href= link.get("href")
        if href:
            print(f"Text: {text} & Link: {href}")
else:
    print("failed to retrieve the webpage.")
