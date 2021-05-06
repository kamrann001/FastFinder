from FastFinder.BusinessLayer.amazonScraper import ScrapeAmazon
from FastFinder.BusinessLayer.amazonDisplayer import displayAmazon

amazon = ScrapeAmazon()
amazon_displayer = displayAmazon(amazon)

from FastFinder.BusinessLayer.tapazScraper import ScrapeTapaz
from FastFinder.BusinessLayer.tapazDisplayer import displayTapaz

tapaz = ScrapeTapaz()
tapaz_displayer = displayTapaz(tapaz)

from FastFinder.BusinessLayer.aliexpressScraper import aliexpressScraper
from FastFinder.BusinessLayer.aliexpressDisplayer import displayAliexpress

aliexpress = aliexpressScraper()
aliexpress_displayer = displayAliexpress(aliexpress)


