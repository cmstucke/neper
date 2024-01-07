from .db import db, environment, SCHEMA, add_prefix_for_prod

class Recipe(db.Model):
  __tablename__ = 'recipes'

  if environment == 'production':
  __table_args__ = { 'schema': SCHEMA }

  id = db.Column(db.Integer, primary_key=True)
  owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
  title = db.Column(db.String, nullable=False)
  category = db.Column(db.String, nullable=False)
  description = db.Column(db.String, nullable=False)
  ingredients = db.Column(db.String, nullable=False)
  steps = db.Column(db.String, nullable=False)
  background = db.Column(db.String, nullable=False)

  users = db.relationship('User', back_populates='recipes')
  recipe_images = db.relationship('RecipeImage', back_populates='recipes', cascade='all, delete')
  comments = db.relationship('Comment', back_populates='recipes', cascade='all, delete')

  def to_dict(self):
    return {
      'id': self.id,
      'owner_id': self.owner_id,
      'title': self.title,
      'category': self.category,
      'description': self.description,
      'ingredients': self.ingredients,
      'steps': self.steps,
      'background': self.background
    }
