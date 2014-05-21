class Meal(object):

    name = ''

    description = ''

    menu_type = ''

    price_int = 0.0

    price_ext = 0.0

    def as_dict(self):
        return {'name': self.name,
                'description': self.description,
                'menu_type': self.menu_type,
                'price_int': self.price_int,
                'price_ext': self.price_ext}

    @staticmethod
    def from_dict(values):
        meal = Meal()
        meal.name = values['name']
        meal.description = values['description']
        meal.menu_type = values['menu_type']
        meal.price_int = values['price_int']
        meal.price_ext = values['price_ext']
        return meal
