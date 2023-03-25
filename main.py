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
    #current_page = WEBPAGE_TEMPLATE.format(fuel=FUEL_TYPE)
    current_page = 'https://rv.campingworld.com/searchresults?external_assets=false&rv_type=motorized&condition=new_used&subtype=A%2CAD%2CB%2CBP%2CC&floorplans=class-a%2Ccafl%2Ccabh%2Ccab2%2Ccarb%2Ccath%2Ccarl%2Cclass-b%2Ccbbh%2Ccbfl%2Ccbrb%2Ccbrl%2Cclass-c%2Cccbh%2Cccfl%2Cccth%2Cccbaah%2Cccrb%2Cccrl&slides_max=0&fueltype=diesel&sort=featured_asc&search_mode=advanced&locations=nationwide&scpc=&apiSearch=0&make=&landingMake=0&page=59'

    all_offers = []

    while current_page:
        page_offers = []
        print(current_page)
        soup = BeautifulSoup(get_page_source(current_page), "html.parser")
        for index, offer_tag in enumerate(get_offers_tags(soup)):
            print(index)
            offer = get_offer_details(offer_tag, index, soup)
            all_offers.append(offer)
            page_offers.append(offer)
            current_page = get_next_page_url(soup)
        write_to_csv(page_offers, 'appended_results2.csv', 'a')
        #time.sleep(2)
    write_to_csv(all_offers, 'all_results2.csv', 'w')
