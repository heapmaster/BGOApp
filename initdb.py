from app import *
import datetime

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



smallworld = Game(name='Small World',icon='static/img/small_world.jpg',difficulty='Medium',points=12,min_players=2, max_players=5,description='In Small World, players vie for conquest and control of a world that is simply too small to accommodate them all.</p><p>Designed by Philippe Keyaerts as a fantasy follow-up to his award-winning Vinci, Small World is inhabited by a zany cast of characters such as dwarves, wizards, amazons, giants, orcs, and even humans, who use their troops to occupy territory and conquer adjacent lands in order to push the other races off the face of the earth.</p><p>Picking the right combination from the 14 different fantasy races and 20 unique special powers, players rush to expand their empires - often at the expense of weaker neighbors. Yet they must also know when to push their own over-extended civilization into decline and ride a new one to victory!</p><p>On each turn, you either use the multiple tiles of your chosen race (type of creatures) to occupy adjacent (normally) territories - possibly defeating weaker enemy races along the way, or you give up on your race letting it go "into decline". A race in decline is designated by flipping the tiles over to their black-and-white side.</p><p>At the end of your turn, you score one point (coin) for each territory your races occupy. You may have one active race and one race in decline on the board at the same time. Your occupation total can vary depend on the special abilities of your race and the territories they occupy. After the final round, the player with the most coins wins.', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building', coop=False)
smallworld2 = Game(name='Small World2',icon='static/img/small_world.jpg',difficulty='Medium2',points=12,min_players=2, max_players=5,description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building', coop=True)
smallworld3 = Game(name='Small World3',icon='static/img/small_world.jpg',difficulty='Medium2',points=12,min_players=2, max_players=9,description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building', coop=False)
db.session.add(smallworld)
db.session.add(smallworld2)
db.session.add(smallworld3)
db.session.commit()

g1 = Match(gameId=smallworld.id,duration=1)
g2 = Match(gameId=smallworld.id,duration=2)

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
