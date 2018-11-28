from bs4 import BeautifulSoup
import requests


req = requests.get("http://www.boerse-frankfurt.de/index/DAX")
doc = BeautifulSoup(req.text, "html.parser")

for element in doc.select("div.push-value"):
    print(element.text)

