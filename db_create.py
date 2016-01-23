from app import db
from models import BlogPost

#create the db
db.create_all()

#inset something to it
db.session.add(BlogPost("Hi", "this is a post"))

#commit the changes
db.session.commit()

