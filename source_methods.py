"""
Methods concerning sending requests
"""
from bs4 import BeautifulSoup
from selenium import webdriver

def get_page_source(page_url: str) -> str:
    """
    Send get request and return page HTML
    :param page_url:
    :return:
    """
    browser = webdriver.Firefox()
    browser.get(page_url)
    source = browser.page_source
    browser.quit()
    return source


def get_offer_soup(offer_url: str) -> BeautifulSoup:
    """
    :param offer_url:
    :return: BeautifulSoup object
    """
    soup = BeautifulSoup(get_page_source(offer_url), "html.parser")
    return soup
