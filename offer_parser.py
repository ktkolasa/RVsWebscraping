from rvdetails_parser import get_horsepower
import re
from config import COLLECT_HORSEPOWER_PRICE_THRESHOLD


def get_offer_name(soup, index):
    tag = soup.find_all('div', {'class': 'unit-right'})[index]
    return tag.find('span', {'itemprop': 'name'}).text


def get_location_and_stock_id(soup, index):
    my_dict = dict()
    location = soup.find_all("span", {"class": "stock-results"})[4*index].text
    stock_id = soup.find_all("span", {"class": "stock-results"})[4*index+1].text
    my_dict["location"] = location.replace(" ", "")
    my_dict["stock_id"] = stock_id.replace(" ", "").replace("Stock#", "")
    return my_dict


def get_offer_url(tag):
    return tag.find("a", {"class": "segment-nav-link"})["href"]


def get_stock_id(tag):
    y = tag.find_all("span", {"class": "stock-results"})
    return y[1].text.split()[-1]


def get_status(soup, index):
    return soup.find_all("span", {"class": "status"})[index*2].text


def get_specs_dict(soup, index):
    specs_dict = dict()
    tag = soup.find_all('div', {'class': 'unit-right'})[index]
    for spec in tag.find_all("div", {"class": "specs"}):
        if spec.find("span").text == "Sleeps":
            specs_dict["sleeps"] = spec.text.split()[-1]
        if spec.find("span").text == "Length(ft)":
            specs_dict["length"] = spec.text.split()[-1]
        if spec.find("span").text == "Mileage":
            specs_dict["mileage"] = spec.text.split()[-1]
        if spec.find("span").text == "Slide Outs":
            if spec.text.split()[-1] == "-":
                specs_dict["slide_outs"] = "-"
            else:
                specs_dict["slide_outs"] = spec.text.split()[-2]
    return specs_dict


def get_price(tag, index):
    price = tag.find_all("span", {"class": "price-info low-price"})[index].text
    return int(re.sub("\D", "", price))


def get_offer_details(tag, index, soup):
    offer_dict = dict()
    offer_dict["name"] = get_offer_name(soup, index)
    offer_dict["offer_url"] = get_offer_url(tag)
    offer_dict.update(get_location_and_stock_id(soup, index))
    offer_dict['status'] = get_status(soup, index)
    offer_dict.update(get_specs_dict(soup, index))
    offer_dict['price'] = get_price(soup, index)

    if offer_dict['price'] > COLLECT_HORSEPOWER_PRICE_THRESHOLD:
        offer_dict['horsepower'] = get_horsepower(offer_dict["offer_url"])
    else:
        offer_dict['horsepower'] = '-'
    return offer_dict
