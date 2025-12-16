import requests
from bs4 import BeautifulSoup

print(" Dynamic Web Scraper")
url = input("Enter the website URL (include https://): ")

try:
    # Fetch the website content
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all headings (h1, h2, h3)
    headings = soup.find_all(["h1", "h2", "h3"])

    print("\n Top Headings:\n")
    count = 0
    for heading in headings:
        text = heading.get_text().strip()
        if text:
            count += 1
            print(f"{count}. {text}")
        if count >= 10:  # Limit to top 10
            break

    if count == 0:
        print(" No headings found. The page may have a different structure.")

except requests.exceptions.RequestException as e:
    print(f" Error fetching data: {e}")
except Exception as e:
    print(f" Unexpected error: {e}")
