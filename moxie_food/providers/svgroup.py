import logging
import requests
from requests import RequestException
from lxml import etree
from datetime import datetime, date, time

from moxie_food.domain import Meal

logger = logging.getLogger(__name__)


class FhnwSvGroupFoodProvider(object):
    """
    Import Meals from SV Group Web page
    """

    ATTRIBUTION = {
        'title': 'FhnwSvGroup',
        'url': 'http://fhnw.sv-group.ch/'}

    def __init__(self, url):
        self.url = url

    def import_meals(self):
        r = requests.get(self.url)
        return iter(self._scrape_xml(r.text.encode('utf-8', 'ignore')))

    def _scrape_xml(self, content):
        parser = etree.HTMLParser(encoding='utf-8')
        root = etree.fromstring(content, parser)

        for offer in root.iterfind('.//div[@class="offer"]'):
            meal = Meal()
            meal.name = offer.find('.//div[@class="title"]').text.strip()
            description = offer.find('.//div[@class="trimmings"]')
            meal.description = ' '.join(etree.tostring(
                 description, method='text', encoding='utf-8').splitlines())
            meal.menu_type = offer.find('.//div[@class="offer-description"]').text.strip()
            for price_item in offer.findall('.//span[@class="price-item"]'):
                price = price_item.text.strip() 
                if 'INT' in price:
                    meal.price_int = float(price[3:])
                elif 'EXT' in price:
                    meal.price_ext = float(price[3:])
                else:
                    # should not happen
                    pass
            yield meal


if __name__ == '__main__':
   provider = FhnwSvGroupFoodProvider('http://localhost:8000/menuplan.html')
   for x in provider.import_meals():
      print(x.as_dict())
