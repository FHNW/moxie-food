import logging
import json
from datetime import datetime

from moxie.core.service import Service
from moxie.core.kv import kv_store

from moxie_food.domain import Meal


logger = logging.getLogger(__name__)

KEY_MEAL = 'meals'
KEY_UPDATED = 'last_updated'


class FoodService(Service):

    def __init__(self, providers=None, service_key='food'):
        """Food service
        :param providers: list of providers to be used
        :param service_key: identifier of the service, mainly used when storing data
        """
        self.provider = self._import_provider(providers.items()[0])
        self.service_key = service_key

    def import_meals(self):
        """Import meal data from provider
        """
        meals = self.provider.import_meals()
        data = json.dumps([meal.as_dict() for meal in meals])
        kv_store.set(self._get_key(KEY_MEAL), data)
        self._set_last_updated()

    def get_meal(self):
        """Get meal data from storage
        :return: Meal domain object
        """
        meal = kv_store.get(self._get_key(KEY_MEAL))
        if not meal:
            return None
        return Meal.from_dict(json.loads(obs))

    def get_attribution(self):
        """Returns a dictionary containing attribution data
        """
        return self.provider.ATTRIBUTION

    def get_last_updated(self):
        """Get date of last update
        """
        return kv_store.get(self._get_key(KEY_UPDATED))

    def _get_key(self, key):
        """Get key used in kv store
        :param key: key to format
        :return: key formatted
        """
        return "{app}_{key}".format(app=self.service_key, key=key)

    def _set_last_updated(self):
        """Set the last updated date to now
        """
        kv_store.set(self._get_key(KEY_UPDATED), datetime.now().isoformat())
