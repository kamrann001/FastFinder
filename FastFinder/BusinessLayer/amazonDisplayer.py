from FastFinder.BusinessLayer.displayer import Displayer
from FastFinder.BusinessLayer.scraper import Scraper


class displayAmazon(Displayer):
    def __init__(self, amazonScraper: Scraper):
        self.amazonScraper = amazonScraper

    def display(self, item, sort_style, amazon, currency, min_price=0, max_price=999999):
        if amazon:
            amazon_products = self.amazonScraper.web_scrape(item)
            if currency == 'azn':
                for i in amazon_products:
                    i['price'] = round((i['price'] * 1.7), 2)
                    i['price'] = str(i['price']) + 'AZN'

            if min_price and max_price:
                amazon_products = self.minMaxPrice(amazon_products, float(min_price), float(max_price))

            if sort_style == 'ascending':
                amazon_products = self.sortByOrder(amazon_products)
            elif sort_style == 'descending':
                amazon_products = self.sortByOrder(amazon_products, True)
            return amazon_products
        else:
            return []
