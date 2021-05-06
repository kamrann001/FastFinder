from FlaskProject2.BusinessLayer.scraper import Scraper
import requests
import json


class aliexpressScraper(Scraper):
    @staticmethod
    def createApi(product):

        url = "https://magic-aliexpress1.p.rapidapi.com/api/products/search"

        querystring = {"name": product}

        headers = {
            'x-rapidapi-key': "4b8f198acemsh3f250505b04fbd8p15736ajsndf9e45e323b6",
            'x-rapidapi-host': "magic-aliexpress1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(str(response.text))
        item_list = data['docs']

        records = []
        for item in item_list:
            description = item['product_title']
            price = item['app_sale_price']
            currency = item['app_sale_price_currency']
            url = item['product_detail_url']

            try:
                rating_val = item['evaluate_rate']
                rating = str(rating_val) + '/5'
            except:
                rating_val = 0
                rating = "No rating available"
            result = {'description': description, 'price': price, 'currency':currency, 'rating': rating, 'url': url}
            records.append(result)

        return records

    def web_scrape(self, product):
        result = self.createApi(product)
        return result


