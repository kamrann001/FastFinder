from FlaskProject2.BusinessLayer.displayer import Displayer
from FlaskProject2.BusinessLayer.scraper import Scraper


class displayTapaz(Displayer):
    def __init__(self, tapazScraper: Scraper):
        self.tapazScraper = tapazScraper

    def display(self, item, sort_style, tapaz, currency, min_price=0, max_price=999999):
        if tapaz:
            tapaz_products = self.tapazScraper.scrape(item)
            if currency == 'usd':
                for i in tapaz_products:
                    i['price'] = round((i['price'] * 0.59), 2)

            if min_price and max_price:
                tapaz_products = self.minMaxPrice(tapaz_products, float(min_price), float(max_price))

            if sort_style == 'ascending':
                tapaz_products = self.sortByOrder(tapaz_products)
            elif sort_style == 'descending':
                tapaz_products = self.sortByOrder(tapaz_products, True)
            return tapaz_products
        else:
            return []