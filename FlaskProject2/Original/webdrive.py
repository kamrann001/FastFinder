from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)


def scrapeAmazon(product):
    if product == '':
        return []
    url = f'https://amazon.com/s?k={product}'

    chromeOptions = Options()
    chromeOptions.headless = False
    driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    def extract_list(item):
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

    records = []

    for item in results:
        record = extract_list(item)

        if record:
            records.append(record)

    driver.quit()
    return records


def scrapeTapaz(product):
    if product == '':
        return []
    url = f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords={product}&q%5Bregion_id%5D='

    chromeOptions = Options()
    chromeOptions.headless = False
    driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    results = soup.find_all('div', {'class': "products-i rounded bumped"}) + soup.find_all('div', {'class': "products-i rounded bumped products-shop"}) + soup.find_all('div', {'class': "products-i rounded"})

    def extract_list(item):
        # description
        atag = item.a
        description = item.find('div', 'products-name').text.strip()
        url = 'https://tap.az' + atag.get('href')[:-9]

        # getting price
        try:
            price = item.find('div', 'products-price').text
            price_tag = price  #saving price as a string to display

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

    records = []

    for item in results:
        record = extract_list(item)

        if record:
            records.append(record)

    driver.quit()
    return records


def scrapeAliexpress(product):
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


def sortByOrder(records, reverse=False):
    newList = sorted(records, key=lambda k: k['price'], reverse=reverse)
    return newList


def minMaxPrice(records, min_price, max_price):
    newList = [d for d in records if min_price < d['price'] < max_price]
    return newList


def displayAmazon(item, sort_style, amazon, currency, min_price=0, max_price=999999):
    if amazon:
        amazon_products = scrapeAmazon(item)
        if currency == 'azn':
            for i in amazon_products:
                i['price'] = round((i['price'] * 1.7), 2)

        if min_price and max_price:
            amazon_products = minMaxPrice(amazon_products, float(min_price), float(max_price))

        if sort_style == 'ascending':
            amazon_products = sortByOrder(amazon_products)
        elif sort_style == 'descending':
            amazon_products = sortByOrder(amazon_products, True)
        return amazon_products
    else:
        return []


def displayTapaz(item, sort_style, tapaz, currency, min_price=0, max_price=999999):
    if tapaz:
        tapaz_products = scrapeTapaz(item)
        if currency == 'usd':
            for i in tapaz_products:
                i['price'] = round((i['price'] * 0.59), 2)

        if min_price and max_price:
            tapaz_products = minMaxPrice(tapaz_products, float(min_price), float(max_price))

        if sort_style == 'ascending':
            tapaz_products = sortByOrder(tapaz_products)
        elif sort_style == 'descending':
            tapaz_products = sortByOrder(tapaz_products, True)
        return tapaz_products
    else:
        return []


def displayAliexpress(item, sort_style, aliexpress, currency, min_price=0, max_price=999999):
    if aliexpress:
        aliexpress_products = scrapeAliexpress(item)
        if currency == 'usd':
            for i in aliexpress_products:
                i['price'] = round((i['price'] * 0.013), 2)
        if currency == 'azn':
            for i in aliexpress_products:
                i['price'] = round((i['price'] * 0.022), 2)

        if min_price and max_price:
            aliexpress_products = minMaxPrice(aliexpress_products, float(min_price), float(max_price))

        if sort_style == 'ascending':
            aliexpress_products = sortByOrder(aliexpress_products)
        elif sort_style == 'descending':
            aliexpress_products = sortByOrder(aliexpress_products, True)
        return aliexpress_products
    else:
        return []
