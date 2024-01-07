from .db import db, environment, SCHEMA, add_prefix_for_prod

class Comment(db.Model):
  __tablename__ = 'comments'

  if environment == 'production':
  __table_args__ = { 'schema': SCHEMA }

  id = db.Column(db.Integer, primary_key=True)
  owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
  recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)
  interaction = db.Column(db.String, nullable=False)
  content = db.Column(db.String, nullable=False)
  image_url = db.Column(db.String, nullable=True)

  users = db.relationship('User', back_populates='recipes')
  recipes = db.relationship('Recipe', back_populates='recipe_images')

  def to_dict(self):
    return {
      'id': self.id,
      'owner_id': self.owner_id,
      'recipe_id': self.recipe_id,
      'interaction': self.interaction,
      'content': self.content,
      'image_url': self.image_url
    }
