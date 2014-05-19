from flask import url_for, jsonify

from moxie.core.representations import HALRepresentation


class HALFoodRepresentation(object):

    def __init__(self, meals, attribution, last_updated, endpoint):
        self.meals = meals
        self.attribution = attribution
        self.last_updated = last_updated
        self.endpoint = endpoint

    def as_dict(self):
        values = {}
        values['meals'] = [f.as_dict() for f in self.meals]
        values['_attribution'] = self.attribution
        values['_last_updated'] = self.last_updated
        representation = HALRepresentation(values)
        representation.add_link('self', url_for(self.endpoint))
        return representation.as_dict()

    def as_json(self):
        return jsonify(self.as_dict())
