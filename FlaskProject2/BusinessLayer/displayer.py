from abc import ABCMeta, abstractmethod


class Displayer(metaclass=ABCMeta):
    @abstractmethod
    def display(self, item, sort_style, amazon, currency, min_price=0, max_price=999999):
        pass

    @staticmethod
    def minMaxPrice(records, min_price=0, max_price=999999):
        newList = [d for d in records if min_price < d['price'] < max_price]
        return newList

    @staticmethod
    def sortByOrder(records, reverse=False):
        newList = sorted(records, key=lambda k: k['price'], reverse=reverse)
        return newList