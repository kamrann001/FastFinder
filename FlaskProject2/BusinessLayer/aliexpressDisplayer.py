from FlaskProject2.BusinessLayer.displayer import Displayer


class displayAliexpress(Displayer):
    def displayAliexpress(self, item, sort_style, aliexpress, currency, min_price=0, max_price=999999):
        if aliexpress:
            aliexpress_products = scrapeAliexpress(item)
            if currency == 'usd':
                for i in aliexpress_products:
                    i['price'] = round((i['price'] * 0.013), 2)
            if currency == 'azn':
                for i in aliexpress_products:
                    i['price'] = round((i['price'] * 0.022), 2)

            if min_price and max_price:
                aliexpress_products = self.minMaxPrice(aliexpress_products, float(min_price), float(max_price))

            if sort_style == 'ascending':
                aliexpress_products = self.sortByOrder(aliexpress_products)
            elif sort_style == 'descending':
                aliexpress_products = self.sortByOrder(aliexpress_products, True)
            return aliexpress_products
        else:
            return []