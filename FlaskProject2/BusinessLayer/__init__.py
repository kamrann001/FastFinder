from FlaskProject2.BusinessLayer.amazonScraper import ScrapeAmazon
from FlaskProject2.BusinessLayer.amazonDisplayer import displayAmazon

amazon = ScrapeAmazon()
amazon_displayer = displayAmazon(amazon)

from FlaskProject2.BusinessLayer.tapazScraper import ScrapeTapaz
from FlaskProject2.BusinessLayer.tapazDisplayer import displayTapaz

tapaz = ScrapeTapaz()
tapaz_displayer = displayTapaz(tapaz)

from FlaskProject2.BusinessLayer.aliexpressScraper import aliexpressScraper
from FlaskProject2.BusinessLayer.aliexpressDisplayer import displayAliexpress

aliexpress = aliexpressScraper()
aliexpress_displayer = displayAliexpress(aliexpress)


