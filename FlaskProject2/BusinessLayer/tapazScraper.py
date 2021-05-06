from bs4 import BeautifulSoup
from FlaskProject2.BusinessLayer.driver import Driver
from FlaskProject2.BusinessLayer.scraper import Scraper

tapaz_driver = Driver(True)


class scrapeTapaz(Scraper):
    def __init__(self):
        self.driver = tapaz_driver.get_driver()

    @staticmethod
    def scrape_tapaz(item):

        # description
        atag = item.a
        description = item.find('div', 'products-name').text.strip()
        url = 'https://tap.az' + atag.get('href')[:-9]

        # getting price
        try:
            price = item.find('div', 'products-price').text
            price_tag = price  # saving price as a string to display

            price = price.replace(" ", "")
            price = float(price[:-3])
        except AttributeError:
            price_tag = 'No price available'
            price = 0
        # rating
        try:
            rating = item.find('span', 'a-icon-alt').text

        except AttributeError:
            rating = ''

        result = {'description': description, 'price': price, 'price_tag': price_tag, 'rating': rating, 'url': url}
        return result

    def web_scrape(self, product):
        if product == '':
            return []
        url = f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords={product}&q%5Bregion_id%5D='

        self.driver.get(url)

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        results = soup.find_all('div', {'class': "products-i rounded bumped"}) + soup.find_all('div', {
            'class': "products-i rounded bumped products-shop"}) + soup.find_all('div', {'class': "products-i rounded"})

        records = []

        for item in results:
            record = self.scrape_tapaz(item)
            if record:
                records.append(record)

        self.driver.quit()
        return records