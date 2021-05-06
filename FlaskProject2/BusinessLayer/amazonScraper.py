from bs4 import BeautifulSoup
from FlaskProject2.BusinessLayer.driver import Driver
from FlaskProject2.BusinessLayer.scraper import Scraper
amazon_driver = Driver(True)


class ScrapeAmazon(Scraper):
    def __init__(self):
        self.driver = amazon_driver.get_driver()

    @staticmethod
    def scrape_amazon(item):
        # description
        atag = item.h2.a
        description = atag.text.strip()
        url = 'https://www.amazon.com' + atag.get('href')

        # getting price
        try:
            price_parent = item.find('span', 'a-price')
            price = price_parent.find('span', 'a-offscreen').text.strip()
            price_tag = price #saving for displaying later

            price = price.replace(",", "")
            price = float(price[1:])
        except AttributeError:
            price = 0
            price_tag = 'No price available'
        # rating
        try:
            rating = item.find('span', 'a-icon-alt').text

        except AttributeError:
            rating = 'No rating available'

        result = {'description': description, 'price': price, 'price_tag': price_tag, 'rating': rating, 'url': url}
        return result

    def web_scrape(self, product):
        if product == '':
            return []
        url = f'https://amazon.com/s?k={product}'

        self.driver.get(url)

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})
        records = []
        for item in results:
            record = self.scrape_amazon(item)
            if record:
                records.append(record)

        return records
