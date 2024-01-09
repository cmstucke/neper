from app.models import db, RecipeImage, environment, SCHEMA
from sqlalchemy.sql import text
from random import randint

def seed_recipe_images():

  recipe_image_1 = RecipeImage(
    owner_id = 1,
    recipe_id = 1
  )
