from .db import db, environment, SCHEMA, add_prefix_for_prod

class RecipeImages(db.Model):
  __tablename__ = 'recipe_images'

  if environment == 'production':
  __table_args__ = { 'schema': SCHEMA }

  id = db.Column(db.Integer, primary_key=True)
  owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
  recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)
  category = db.Column(db.String, nullable=False)
  description = db.Column(db.String, nullable=False)
  preview_image = db.Column(db.String, nullable=False)

  users = db.relationship('User', back_populates='recipe_images')
  recipes = db.relationship('Recipe', back_populates='recipe_images')

  def to_dict(self):
    return {
      'id': self.id,
      'owner_id': self.owner_id,
      'recipe_id': self.recipe_id,
      'category': self.category,
      'description': self.description,
      'preview_image': self.preview_image
    }
