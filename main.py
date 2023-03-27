"""
Main to run webscraping process
"""

import time
import csv

from bs4 import BeautifulSoup
from selenium import webdriver

from config import WEBPAGE_TEMPLATE
from offer_parser import get_offer_details
from main_page_parser import get_offers_tags, get_next_page_url
from source_methods import get_page_source

browser = webdriver.Firefox()


def get_page_url_for_fuel_type(fuel_type):
    return WEBPAGE_TEMPLATE.format(fuel=fuel_type)


def write_to_csv(dict_list, file_name, mode):
    column_names = dict_list[0].keys()
    with open(file_name, mode) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(dict_list)


if __name__ == "__main__":
    FUEL_TYPE = 'diesel'
    current_page = WEBPAGE_TEMPLATE.format(fuel=FUEL_TYPE)

    all_offers = []

    while current_page:
        print(current_page)
        page_offers = []
        soup = BeautifulSoup(get_page_source(current_page), "html.parser")
        for index, offer_tag in enumerate(get_offers_tags(soup)):
            offer = get_offer_details(offer_tag, index, soup)
            all_offers.append(offer)
            page_offers.append(offer)
            current_page = get_next_page_url(soup)
        write_to_csv(page_offers, 'results.csv', 'a')
        time.sleep(1)