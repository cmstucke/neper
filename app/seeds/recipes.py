from app.models import db, Recipe, environment, SCHEMA
from sqlalchemy.sql import text
from random import randint

def seed_recipes():

  recipe_1 = Recipe(
    owner_id = 1,
    title = 'Egg Over Easy',
    category = 'Breakfast',
    description = 'Easy, cheap, delicious protein commonly eaten as part of breakfast.',
    ingredients = '1_Tablespoon_Butter|||||1_Egg|||||1_Pinch_Salt|||||1_Pinch_Black_Pepper',
    steps = 'Let a skillet come up to temperature over a medium-low heat.|||||Once the skillet is thoroughly heated, drop in the butter and let heat until the butter stops foaming.|||||Crack the egg gently into the pan being careful not to break the yolk.|||||Season the egg with salt and pepper, and optionally break the inner white to help it set before the yolk.|||||Once the whites of the egg are set, gently turn egg by tossing gently or turning with a spatula.|||||Let the other side cook for about 30 seconds and then kill heat or remove the pan.|||||Let the residual heat cook the egg till done, then remove from pan.',
    background = 'A breakfast quintessential. Have it on a piece of toast, on top of a lovely hash, on a bagel sandwich, you name it.'
  )

  all_recipes = [recipe1]
  add_recipes = [db.session.add(recipe) for recipe in all_recipes]
  db.session.commit()

def undo_recipes():
  if environment == 'production':
    db.session.execute(f"TRUNCATE table {SCHEMA}.shops RESTART IDENTITY CASCADE;")
  else:
    db.session.execute(text("DELETE FROM shops"))

  db.session.commit()
