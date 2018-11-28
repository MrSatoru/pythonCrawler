from bs4 import BeautifulSoup
import requests
import re


class Index:
    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp


req = requests.get("http://www.boerse-frankfurt.de/index/DAX")
doc = BeautifulSoup(req.text, "html.parser")


def get_value_timestamp():

    value = None
    time_stamp = None

    for element in doc.select("div.push-value"):
        if re.match('^\d+[.]\d{3}[,]\d{2}$', element.text):
            value = element.text
        elif re.match('^\d{2}[:]\d{2}[:]\d{2}$', element.text):
            time_stamp = element.text

    dax = Index(value, time_stamp)

    return dax







