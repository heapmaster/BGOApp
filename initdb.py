from app import *
import datetime

db.drop_all()
db.create_all()

alan = Country(name='Buy N Large',icon='static/img/bnl_flag.jpg',category='Friendly Neighborhood Conglomerate',dateEstablished='New Jersey, USA', description="According to The History of Buy n Large, the corporation got its start as a maker of frozen yogurt.It was a small business called Buy Yogurt. Later on, the business eventually acquired Large Industries, a men's suit company. The combined entity became known as Buy n' Large (note how there once was an apostrophe after the n). The dates of Buy Yogurt's founding and its acqusition of Large Industries are unknown. However, by the year 2057, as shown on the Buy n Large website, the conglomerate became a worldwide leader in the fields of aerospace, agriculture, construction, consumer goods, corporate grooming, earth transport, electronics, energy, engineering, finance, food services, fusion research, government, hydro-power, infrastructures, media, medical science, mortage loans, pet care, pharmaceuticals, phsycotherapies, ports and harbors, real estate, repairs, retail, robotics, science/health, space, storage, super centers, super grids, travel services, utilities, and watermills. The corporation's control affected other companies as well. It seemed as though other businesses wanted BnL to buy them out, such as Headr Inc. which gave BnL control of the world news headlines.", quote='Buy, Shop, Live.', quoteAuthor='Buy N Large Slogan', representative='Alan You')
shane = Country(name='Stark Industries',icon='static/img/stark_industries_flag.jpg',category='Weapons and Technology Company',dateEstablished='New York City, USA', description="Stark Industries is a weapons and technology company founded and owned by Howard Stark. In World War II, Stark Industries built 100,000 planes to help the Allies forces, quickly establishing them as a military contractor. Stark Industries also assisted the Strategic Scientific Reserve fight against HYDRA. After Howard's death, ownership passed to his son, Tony and the company was run by Obadiah Stane until Tony was old enough to take over. Under Tony's leadership, Stark Industries became the world leader in the development of manufacturing advanced weapons. Stark Industries quickly branched out into other scientific fields including aeronautics, robotics, micro-technology and fringe science. After returning home from being held captive, Tony stopped Stark Industries from manufacturing weapons and focused instead on clean energy. Later as Tony continues to operate as Iron Man, he realizes that the Paladium core of his Arc reactor is slowly poisoning him and appoints Pepper Potts as Chairman and CEO of Stark Industries, though she later resigned after Tony found a cure for the palladium poisoning that was killing him. After the Battle of New York, Pepper once again became the CEO of Stark Industries.", quote='Better living through technology.', quoteAuthor='Stark Industries Slogan', representative='Shane Fry')
scott = Country(name='Globex',icon='static/img/globex_flag.png',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Scott N')
kim = Country(name='Acme',icon='static/img/shinra_flag.jpg',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Kim N')

db.session.add(alan)
db.session.add(shane)
db.session.add(scott)
db.session.add(kim)
db.session.commit()


small_world = Game(name='Small World',icon='static/img/small_world.jpg',difficulty='Medium',points=12,min_players=2, max_players=5,description='In Small World, players vie for conquest and control of a world that is simply too small to accommodate them all.</p><p>Designed by Philippe Keyaerts as a fantasy follow-up to his award-winning Vinci, Small World is inhabited by a zany cast of characters such as dwarves, wizards, amazons, giants, orcs, and even humans, who use their troops to occupy territory and conquer adjacent lands in order to push the other races off the face of the earth.</p><p>Picking the right combination from the 14 different fantasy races and 20 unique special powers, players rush to expand their empires - often at the expense of weaker neighbors. Yet they must also know when to push their own over-extended civilization into decline and ride a new one to victory!</p><p>On each turn, you either use the multiple tiles of your chosen race (type of creatures) to occupy adjacent (normally) territories - possibly defeating weaker enemy races along the way, or you give up on your race letting it go "into decline". A race in decline is designated by flipping the tiles over to their black-and-white side.</p><p>At the end of your turn, you score one point (coin) for each territory your races occupy. You may have one active race and one race in decline on the board at the same time. Your occupation total can vary depend on the special abilities of your race and the territories they occupy. After the final round, the player with the most coins wins.', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building', coop=False)
smallworld2 = Game(name='Small World2',icon='static/img/small_world.jpg',difficulty='Medium2',points=12,min_players=2, max_players=5,description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building', coop=True)
smallworld3 = Game(name='Small World3',icon='static/img/small_world.jpg',difficulty='Medium2',points=12,min_players=2, max_players=9,description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building', coop=False)

db.session.add(small_world)
db.session.add(smallworld2)
db.session.add(smallworld3)
db.session.commit()


g1 = Match(gameId=small_world.id,duration=1)
g2 = Match(gameId=small_world.id,duration=2)

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
