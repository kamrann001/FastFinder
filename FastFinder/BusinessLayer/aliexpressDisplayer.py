from FastFinder.BusinessLayer.displayer import Displayer
from FastFinder.BusinessLayer.scraper import Scraper


class displayAliexpress(Displayer):
    def __init__(self, aliexpressScraper: Scraper):
        self.aliexpressScraper = aliexpressScraper

    def display(self, item, sort_style, aliexpress, currency, min_price=0, max_price=999999):
        if aliexpress:
            aliexpress_products = self.aliexpressScraper.web_scrape(item)
            if currency == 'azn':
                for i in aliexpress_products:
                    i['price'] = round((i['price'] * 1.7), 2)

            if min_price and max_price:
                aliexpress_products = self.minMaxPrice(aliexpress_products, float(min_price), float(max_price))

            if sort_style == 'ascending':
                aliexpress_products = self.sortByOrder(aliexpress_products)
            elif sort_style == 'descending':
                aliexpress_products = self.sortByOrder(aliexpress_products, True)
            return aliexpress_products
        else:
            return []
