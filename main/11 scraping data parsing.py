import os
from bs4 import BeautifulSoup

for files in os.listdir("htmls"):
    with open(f"htmls/{files}") as f:
        htmlContent = f.read()
        soup = BeautifulSoup(htmlContent, "html.parser")
        # print(soup)
        # print(soup.title)
        for link in soup.find_all("a"):
            # print(link)
            print(link.get("href"))