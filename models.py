from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask import Flask
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#



class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    genres = db.Column(db.ARRAY(db.String))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, nullable=False, server_default='FALSE')
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venue', lazy='joined', cascade="all, delete")

    def __repr__(self):
        return f'<Vanue {self.id} {self.name} {self.genres} {self.city} {self.state} \
            {self.address} {self.phone} {self.website_link} {self.image_link} {self.facebook_link} \
                {self.seeking_talent} {self.seeking_description}>'


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True )
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False, server_default='FALSE')
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='artist', lazy='joined', cascade="all, delete")

    def __repr__(self):
        return f'<Artist {self.id} {self.name} {self.genres} {self.city} {self.state} \
            {self.phone} {self.website_link} {self.image_link} {self.facebook_link} \
                {self.seeking_venue} {self.seeking_description}>'


class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable = False)

    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id', ondelete='CASCADE'), nullable = False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id', ondelete='CASCADE'), nullable = False)
    
    def __repr__(self):
        return f'<Show {self.id} {self.venue_id} {self.artist_id} {self.start_time}>'