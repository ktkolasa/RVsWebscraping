"""
Methods for parsing main offer list apart from offer details
"""


def get_next_page_url(soup):
    next_page = soup.find("a", {"class": "pag-btn next"})
    if next_page:
        return next_page.get("href")
    else:
        return None


def get_offers_tags(soup):
    return soup.find_all("div", {"class": "big"})
