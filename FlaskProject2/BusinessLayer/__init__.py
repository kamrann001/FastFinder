from FlaskProject2.BusinessLayer.amazonScraper import ScrapeAmazon
from FlaskProject2.BusinessLayer.amazonDisplayer import displayAmazon

amazon = ScrapeAmazon()
amazon_displayer = displayAmazon(amazon)

from FlaskProject2.BusinessLayer.tapazScraper import ScrapeTapaz
from FlaskProject2.BusinessLayer.tapazDisplayer import displayTapaz

tapaz = scrapeTapaz()
display_web2 = displayTapaz(tapaz)


