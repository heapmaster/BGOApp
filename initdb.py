from app import *
import datetime

if("sqlite" not in app.config['SQLALCHEMY_DATABASE_URI']):
	db.reflect()
db.drop_all()
db.create_all()

shane = Country(name='Stark Industries',icon='static/img/aperture_flag.png',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Shane Fry')
alan = Country(name='Shinra',icon='static/img/bnl_flag.jpg',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Alan You')
scott = Country(name='Globex',icon='static/img/globex_flag.png',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Scott N')
kim = Country(name='Acme',icon='static/img/shinra_flag.jpg',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Kim N')
db.session.add(shane)
db.session.add(alan)
db.session.add(scott)
db.session.add(kim)
db.session.commit()



smallworld = Game(name='Small World',icon='static/img/small_world.jpg',difficulty='Medium',points=12,numPlayers='2-5',description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building')
smallworld2 = Game(name='Small World2',icon='static/img/small_world.jpg',difficulty='Medium2',points=12,numPlayers='2-5',description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building')
db.session.add(smallworld)
db.session.add(smallworld2)
db.session.commit()

g1 = Match(gameId=smallworld.id,duration=50)
g2 = Match(gameId=smallworld.id,duration=45)

db.session.add(g1)
db.session.add(g2)
db.session.commit()

p1 = GamePlayer(matchId=g1.id, countryId=alan.id, place=1)
p2 = GamePlayer(matchId=g1.id, countryId=shane.id, place=2)

p3 = GamePlayer(matchId=g2.id, countryId=shane.id, place=1)
p4 = GamePlayer(matchId=g2.id, countryId=alan.id, place=2)
p5 = GamePlayer(matchId=g2.id, countryId=kim.id, place=3)
p6 = GamePlayer(matchId=g2.id, countryId=scott.id, place=0)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.add(p6)
db.session.commit()
