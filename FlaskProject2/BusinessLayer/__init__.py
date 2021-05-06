from FlaskProject2.BusinessLayer.amazonScraper import scrapeAmazon
from FlaskProject2.BusinessLayer.amazonDisplayer import displayAmazon

amazon = scrapeAmazon()
amazon_displayer = displayAmazon(amazon)

from FlaskProject2.BusinessLayer.tapazScraper import scrapeTapaz
from FlaskProject2.BusinessLayer.tapazDisplayer import displayTapaz

tapaz = scrapeTapaz()
display_web2 = displayTapaz(tapaz)


