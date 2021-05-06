from abc import ABCMeta, abstractmethod


class Scraper(metaclass=ABCMeta):
    @abstractmethod
    def web_scrape(self, item):
        pass