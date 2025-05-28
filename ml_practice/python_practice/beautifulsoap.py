import requests
from bs4 import BeautifulSoup
# 7VZE093SOD8UIF0X

url = "https://www.highsense.in/"

headers = {"User-Agent": "Mozilla/5.0"} 

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.text.strip()
    print(f"Page Title: {title}\n")
    headings = soup.find_all(["h1", "h2", "h3"])
    print("Headings:")
    for heading in headings:
        print(f"- {heading.text.strip()}")
    links = soup.find_all("a", href=True)
    print("\nLinks:")
    for link in links[:10]:
        print(f"- {link['href']}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")