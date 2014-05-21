==========
moxie-food
==========

Restaurant module for Moxie

Gather data from Campus Restaurant FHNW Brugg-Windisch and process it for moxie. 

Moxie blueprint: ::

  services:
      food:
          FoodService:
              providers:
                  moxie_food.providers.svgroup.FhnwSvGroupFoodProvider:
                      url: 'http://fhnw.sv-group.ch/de.html'
          KVService:
              backend_uri: 'redis://localhost:6379/0'


Celery configuration: ::

  # List of modules to import when celery starts.
  CELERY_IMPORTS = (..., "moxie_food.tasks")


Import data ::

  >>> from moxie_food.tasks import import_meals
  >>> import_meals.delay()
