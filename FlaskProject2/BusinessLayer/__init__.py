from FlaskProject.BusinessLayer.amazonScraper import ScrapeAmazon
from FlaskProject.BusinessLayer.amazonDisplayer import displayAmazon

amazon = ScrapeAmazon()
amazon_displayer = displayAmazon(amazon)

from FlaskProject.BusinessLayer.tapazScraper import ScrapeTapaz
from FlaskProject.BusinessLayer.tapazDisplayer import displayTapaz

tapaz = scrapeTapaz()
display_web2 = displayTapaz(tapaz)


