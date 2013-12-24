from app import *
import datetime

db.drop_all()
db.create_all()

shane = Country(name='Globex',icon='globex.jpg',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Shane Fry')
alan = Country(name='Shinra',icon='globex.jpg',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Alan You')
db.session.add(shane)
db.session.add(alan)
db.session.commit()



smallworld = Game(name='Small World',icon='static/img/small_world.jpg',difficulty='Medium',points=12,numPlayers='2-5',description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building')
smallworld2 = Game(name='Small World2',icon='static/img/small_world.jpg',difficulty='Medium2',points=12,numPlayers='2-5',description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building')
db.session.add(smallworld)
db.session.add(smallworld2)
db.session.commit()

g1 = Match(gameId=smallworld.id,startTime=datetime.datetime.utcnow())
g2 = Match(gameId=smallworld.id,startTime=datetime.datetime.utcnow())

db.session.add(g1)
db.session.add(g2)
db.session.commit()

p1 = GamePlayers(matchId=g1.id, countryId=alan.id, place=1)
p2 = GamePlayers(matchId=g1.id, countryId=shane.id, place=2)

p3 = GamePlayers(matchId=g2.id, countryId=shane.id, place=1)
p4 = GamePlayers(matchId=g2.id, countryId=alan.id, place=2)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.commit()
