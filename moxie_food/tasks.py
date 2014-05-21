from celery.utils.log import get_task_logger

from moxie import create_app
from moxie.worker import celery

from moxie_food.services import FoodService


logger = get_task_logger(__name__)

BLUEPRINT_NAME = 'food'


@celery.task
def import_meals():
    app = create_app()
    with app.blueprint_context(BLUEPRINT_NAME):
        service = FoodService.from_context()
        service.import_meals()
