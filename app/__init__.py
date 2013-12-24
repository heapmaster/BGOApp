#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/nindoja/projects/bgo/db.sqlite'

db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    icon = db.Column(db.String(300))
    difficulty = db.Column(db.Integer)
    points = db.Column(db.Integer)
    numPlayers = db.Column(db.String(20))
    description = db.Column(db.Text)
    playingTime = db.Column(db.String(30))
    category = db.Column(db.String(100))
    
    def __init__(self, name, icon, difficulty, points, numPlayers, description, playingTime, category):
        self.name = name
        self.icon = icon
        self.difficulty = difficulty
        self.points = points
        self.numPlayers = numPlayers
        self.description = description
        self.playingTime = playingTime
        self.category = category

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'  : self.id,
           'name': self.name,
           'icon': self.icon,
           'difficulty': self.difficulty,
           'points': self.points,
           'numPlayers': self.numPlayers,
           'description': self.description,
           'playingTime': self.playingTime,
           'category': self.category
       }

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    icon = db.Column(db.String(300))
    category = db.Column(db.String(100))
    dateEstablished = db.Column(db.String(100))
    description = db.Column(db.Text)
    quote = db.Column(db.String(200))
    quoteAuthor = db.Column(db.String(100))
    representative = db.Column(db.String(120))

    def __init__(self, name, icon, category, dateEstablished, description, quote, quoteAuthor, representative):
        self.name = name
        self.icon = icon
        self.category = category
        self.dateEstablished = dateEstablished
        self.description = description
        self.quote = quote
        self.quoteAuthor = quoteAuthor
        self.representative = representative

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'icon' : self.icon,
            'category' : self.category,
            'dateEstablished' : self.dateEstablished,
            'representative' : self.name,
            'description' : self.description,
            'quote' : self.quote,
            'quoteAuthor' : self.quoteAuthor
        }

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gameId = db.Column(db.Integer, db.ForeignKey('game.id'))
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    players = db.relationship('GamePlayers',backref='match',lazy='dynamic')
    game = db.relationship('Game')

    def __init__(self, gameId, startTime, endTime=None):
        self.gameId = gameId
        self.startTime = startTime
        self.endTime = endTime

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'startTime' : self.startTime,
            'endTime' : self.endTime,
            'gameId' : self.gameId,
            'countries' : [i.serialize for i in self.players]
        }

class GamePlayers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matchId = db.Column(db.Integer, db.ForeignKey('match.id'))
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'))
    place = db.Column(db.Integer)
    
    company = db.relationship('Company',backref='games')

    def __init__(self, matchId, companyId, place=0):
        self.matchId = matchId
        self.companyId = companyId
        self.place = place

    @property
    def serialize(self):
        return {
            'matchId' : self.matchId,
            'countryId' : self.company.id,
            'place' : self.place,
            'representative' : self.company.representative,
            'country' : self.company.name,
            'points' : max(0, self.match.game.points*(4-self.place)/3)
        }

def calc_user_score(id):
    score = 0
    matches = GamePlayers.query.filter_by(companyId=id).all()
    for match in matches:
        points = Game.query.filter_by(id=match.game.id).first().points
        score = score + max(0, points*(4-match.place)/3)

    return score

@app.route('/games', methods = ['GET'])
def get_games():
    return jsonify( games = [i.serialize for i in Game.query.all()] )

@app.route('/game/<id>/', methods = ['GET'])
def get_game(id):
    return jsonify( game = [i.serialize for i in Game.query.filter_by(id=id)] )

@app.route('/companies', methods = ['GET'])
def get_companies():
    return jsonify( companies = [i.serialize for i in Company.query.all()] )

@app.route('/company/<id>/', methods = ['GET'])
def get_company(id):
    return jsonify( company = [i.serialize for i in Company.query.filter_by(id=id)] )

@app.route('/company/<id>/score')
def get_user_score(id):
    return jsonify(score = calc_user_score(id))

@app.route('/matches', methods = ['GET'])
def get_matches():
    return jsonify( matches = [i.serialize for i in Match.query.all()] )

#@app.route('/matches', methods = ['POST'])
#def create_match():
#    if not request.json:
#        abort(400)

#    m = Match(gameId=request.json['gameId'], startTime=datetime.datetime.utcnow())
#    players = []
#    for player in request.json['players']
#    return jsonify( matches = [i.serialize for i in Match.query.all()] )