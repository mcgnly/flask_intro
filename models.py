from app import db #notice the dependencies here, because that influences where we import this in the app file

class BlogPost(db.Model):

	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)

	def __init__(self, title, description):
		self.title=title
		self.description=description

#this controls how the entries are displayed. the {} get subbed out for the DB entry
	def __repr__(self):
		return '{} :: {}'.format(self.title, self.description)