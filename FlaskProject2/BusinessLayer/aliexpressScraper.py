from FlaskProject2.BusinessLayer.scraper import Scraper
from FlaskProject2.BusinessLayer.driver import Driver
from bs4 import BeautifulSoup

aliexpress_driver = Driver(True)


class aliexpressScraper(Scraper):
    def __init__(self):
        self.driver = aliexpress_driver.get_driver()\


    @staticmethod
    def scrapeAliexpress(self, product):
        if product == '':
            return []
        url = f'https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20210415083131&SearchText={product}'

        chromeOptions = Options()
        chromeOptions.headless = False
        driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
        driver.get(url)
        sleep(1)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        results = soup.find_all('div', {'class': "product-card"})

        def extract_list(item):
            # description
            atag = item.a
            try:
                description = item.find('a', 'item-title').get('title').strip()
            except AttributeError:
                description = "No title available"
            url = atag.get('href')

            # getting price
            try:
                price = item.find('span', 'price-current').text
                price_tag = price
                price = str(price.encode(encoding="ascii", errors="replace"))
                price = price.split("-")[0]
                price = price.replace("?", "").replace("'", "").replace(",", ".")
                price = price[1:]
                price = price[:-2]
                price = float(price)
            except AttributeError:
                price_tag = 'No price available'
                price = 0
            # rating
            try:
                rating = item.find('span', 'rating-value').text

            except AttributeError:
                rating = 'No rating available'

            result = {'description': description, 'price': price, 'price_tag': price_tag, 'rating': rating, 'url': url}
            return result

        records = []

        for item in results:
            record = extract_list(item)

            if record:
                records.append(record)

        driver.quit()
        return records
