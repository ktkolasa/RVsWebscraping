from config import ROOT_URL
from source_methods import get_offer_soup


def get_prod_features_tags_list(soup):
    product_feature_tags = soup.find_all("div", {"class": "oneSpec clearfix"})
    return product_feature_tags


def find_feature(feature_name, product_feature_tags):
    feature_val = None
    for detail in product_feature_tags:
        if detail.find("h4").text.replace(" ", "") == feature_name.replace(" ", ""):
            feature_val = detail.find("h5").text
    return feature_val


def get_horsepower(offer_url):
    offer_soup = get_offer_soup(ROOT_URL + offer_url)
    product_feature_tags = get_prod_features_tags_list(offer_soup)
    horsepower = find_feature("HORSEPOWER", product_feature_tags)
    return horsepower
