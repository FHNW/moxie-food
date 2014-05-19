from flask import request

from moxie.core.views import ServiceView, accepts
from moxie.core.representations import HAL_JSON, JSON

from moxie_food.services import FoodService
from moxie_food.representations import HALFoodRepresentation


class FoodView(ServiceView):

    def handle_request(self):
        service = FoodService.from_context()
        self.meals = service.get_meals()
        self.attribution = service.get_attribution()
        self.last_updated = service.get_last_updated()
        return None

    @accepts(HAL_JSON, JSON)
    def as_hal_json(self, result):
        return HALFoodRepresentation(
            self.meals, self.attribution, self.last_updated,
            request.url_rule.endpoint).as_json()
