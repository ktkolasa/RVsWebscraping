"""
Methods for parsing main ofer list apart from offer details
"""


def get_next_page_url(soup):
    next = soup.find("a", {"class": "pag-btn next"})
    if next:
        return next.get("href")
    else:
        return None


def get_offers_tags(soup):
    return soup.find_all("div", {"class": "big"})
