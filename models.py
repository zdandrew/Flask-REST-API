from app import db


# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

tags = db.Table('tags',
    db.Column('tag_id', db.String(100), db.ForeignKey('tag.id'), primary_key=True),
    db.Column('club_code', db.String(100), db.ForeignKey('club.code'), primary_key=True)
)

users = db.Table('users',
    db.Column('club_code', db.String(100), db.ForeignKey('club.code'), primary_key=True),
    db.Column('user_id', db.String(100), db.ForeignKey('user.id'), primary_key=True)
)

class Club(db.Model):
    code = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('clubs', lazy=True))
    users = db.relationship('User', secondary=users, lazy='subquery',
        backref=db.backref('clubs', lazy=True))

    def __repr__(self):
        return '<Club %r>' % self.name

class Tag(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    def __repr__(self):
        return '<Tag %r>' % self.id

class User(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.id