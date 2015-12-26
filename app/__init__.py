#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import render_template
from flask import abort
from flask import redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import datetime
import socket
import os

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bgoapp'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')

db = SQLAlchemy(app)

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    icon = db.Column(db.String(300))
    difficulty = db.Column(db.String(40))
    points = db.Column(db.Integer)
    min_players = db.Column(db.Integer)
    max_players = db.Column(db.Integer)
    description = db.Column(db.Text)
    playingTime = db.Column(db.String(30))
    category = db.Column(db.String(100))
    coop = db.Column(db.Boolean)
    
    def __init__(self, name, icon, difficulty, points, min_players, max_players, description, playingTime, category, coop):
        self.name = name
        self.icon = icon
        self.difficulty = difficulty
        self.points = points
        self.min_players = min_players
        self.max_players = max_players
        self.description = description
        self.playingTime = playingTime
        self.category = category
        self.coop = coop

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'  : self.id,
           'name': self.name,
           'icon': self.icon,
           'difficulty': self.difficulty,
           'points': self.points,
           'min_players': self.min_players,
           'max_players': self.max_players,
           'description': self.description,
           'playingTime': self.playingTime,
           'category': self.category,
           'coop': self.coop
       }

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    icon = db.Column(db.String(300))
    category = db.Column(db.String(100))
    dateEstablished = db.Column(db.String(100))
    description = db.Column(db.Text)
    quote = db.Column(db.String(200))
    quoteAuthor = db.Column(db.String(100))
    representative = db.Column(db.String(120))
    score = db.Column(db.Integer, default=0)

    def __init__(self, name, icon, category, dateEstablished, description, quote, quoteAuthor, representative, score=0):
        self.name = name
        self.icon = icon
        self.category = category
        self.dateEstablished = dateEstablished
        self.description = description
        self.quote = quote
        self.quoteAuthor = quoteAuthor
        self.representative = representative
        self.score = score

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'icon' : self.icon,
            'category' : self.category,
            'dateEstablished' : self.dateEstablished,
            'representative' : self.representative,
            'description' : self.description,
            'quote' : self.quote,
            'quoteAuthor' : self.quoteAuthor,
            'points' : self.score
        }

class Match(db.Model):
    __tablename__ = 'match'
    id = db.Column(db.Integer, primary_key=True)
    gameId = db.Column(db.Integer, db.ForeignKey('game.id'))
    duration = db.Column(db.Integer)
    players = db.relationship('GamePlayer',backref='match',lazy='dynamic')
    game = db.relationship('Game')

    def __init__(self, gameId, duration):
        self.gameId = gameId
        self.duration = duration

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'duration' : self.duration,
            'gameId' : self.gameId,
            'countries' : [i.serialize for i in self.players]
        }

class GamePlayer(db.Model):
    __tablename__ = 'game_player'
    id = db.Column(db.Integer, primary_key=True)
    matchId = db.Column(db.Integer, db.ForeignKey('match.id'))
    countryId = db.Column(db.Integer, db.ForeignKey('country.id'))
    place = db.Column(db.Integer)
    points = db.Column(db.Integer)
 
    country = db.relationship('Country',backref='games')

    def __init__(self, matchId, countryId, place=0, points=0):
        self.matchId = matchId
        self.countryId = countryId
        self.place = place
        self.points = points

    @property
    def serialize(self):
        return {
            'matchId' : self.matchId,
            'countryId' : self.country.id,
            'place' : self.place,
            'representative' : self.country.representative,
            'country' : self.country.name,
            #'points' : max(0, self.match.game.points*(4-self.place)/3)/len(GamePlayer.query.filter_by(matchId=self.matchId,place=self.place).all()) if self.place > 0 else 0
            #'points' : max(0, self.match.game.points*(4-self.place)/3)/1 if self.place > 0 else 0
            'points' : self.points 
        }

def calc_country_score(id):
    score = 0
    matches = GamePlayer.query.filter_by(countryId=id).all()
    opponents = set()

    for match in matches:
        #match.points = calc_country_game_score(id,match)
        score = score + match.points
        for player in match.match.players:
            opponents.add(player.countryId)

    #score + social bonus and adjust for player being in opponents list
    return score + max(0,len(opponents)-1)

def calc_country_game_score(countryId, match):
    points = Game.query.get(match.match.gameId).points
    #award points to top 3 players so long as there are at least 3 players
    if(match.place>0 and match.place < 4 and match.place < match.match.players.count()):
        if(Game.query.get(match.match.gameId).coop):
            samePlace = GamePlayer.query.filter_by(matchId=match.matchId,place=match.place).count()            
        else:
            samePlace = 1
        #samePlace = GamePlayer.query.filter_by(matchId=match.matchId,place=match.place).count()
        #samePlace = 1;
        score = (max(0, points*(4-match.place)/3))/samePlace    
        
        matches = GamePlayer.query.filter_by(countryId=countryId).all()
        for i in matches:
            if i.match.gameId == match.match.gameId and i.id < match.id:
                score = score/2
                break

        return score + match.match.duration-1
    #cheater  
    elif (match.place == -1):
        return -5
    
    return match.match.duration-1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/games', methods = ['GET'])
def get_games():
    return jsonify( games = [i.serialize for i in Game.query.all()] )

@app.route('/games/<id>/', methods = ['GET'])
def get_game(id):
    return jsonify(Game.query.get(id).serialize)

@app.route('/countries', methods = ['GET'])
def get_countries():
    return jsonify( countries = [i.serialize for i in Country.query.all()] )

@app.route('/countries/<id>/', methods = ['GET'])
def get_country(id):
    return jsonify(Country.query.get(id).serialize)

@app.route('/country/<id>/score')
def get_country_score(id):
    return jsonify(score = Country.query.get(id).score)

@app.route('/matches', methods = ['GET'])
def get_matches():
    return jsonify( matches = [i.serialize for i in Match.query.all()] )

@app.route('/matches/<id>/')
def get_match(id):
    return jsonify(Match.query.get(id).serialize)

@app.route('/recalculate')
def recalculate():
    for player in GamePlayer.query.all():
        player.points = calc_country_game_score(player.countryId, player)
    for country in Country.query.all():
        country.score = calc_country_score(country.id)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/scores')
def get_scores():
    #name, rank, score, flag
    board = []

    countries = Country.query.all()
    for country in countries:
        score = country.score
        board.append({"id":country.id, "country":country.name, "score":score, "flag":country.icon})
    return jsonify(scores=board)

@app.route('/matches', methods = ['POST'])
def create_match():
    if not request.json:
        abort(400)
    else:
        print "-------------------------------- begin JSON ------------------------------"
        print request.json
        print "-------------------------------- end JSON ------------------------------"

    m = Match(gameId=request.json['game_id'], duration=int(request.json['duration_id']))
    
    #TODO: add transaction around this whole create
    db.session.add(m)
    db.session.commit()

    players = []
    for player in request.json['players']:
        gamePlayer = GamePlayer(matchId=m.id, countryId=player['player_id'],place=player['place'])
        db.session.add(gamePlayer)
	players.append(gamePlayer)
        print "Player " + str(player['player_id']) + " finished in " + str(player['place']) + " place"
    
    db.session.commit()

    print "test2"
    for player in players:
        country = Country.query.get(player.countryId)
        player.points = calc_country_game_score(player.countryId, player)
        db.session.commit()
        print "Adding " + str(player.points) + " points to Country: " + str(country.id)
        country.score = calc_country_score(country.id)
        db.session.commit()
    
    return jsonify(m.serialize),200
