# coding: utf-8

from app import *
import datetime

db.drop_all()
db.create_all()

derek = Country(name='Aperture Science',icon='static/img/aperture_science_flag.jpg',category='Scientific Research Company',dateEstablished='Upper Michigan, USA', description="Aperture Science was founded as Aperture Fixtures in the early 1940s by Cave Johnson. Aperture Fixtures was primarily dedicated to the manufacture and distribution of shower curtains – a low-tech portal between the inside and outside of a shower – with Cave Johnson winning the \"Shower Curtain Salesman of 1943\" award. Some time between 1943 and 1947 the company's name was changed to \"Aperture Science Innovators\". While this was initially done to make their shower curtains sound more hygienic, the company's focus would indeed soon shift to actual science. Cave Johnson purchased a large, abandoned salt mine in Upper Michigan in which Aperture Science's Enrichment Center would be built; however, there was at least one alternate location in Cleveland, Ohio.</p><p>Throughout the late 1940s and the 1950s, Aperture Science would begin its comprehensive testing and research practices. The best possible test subjects, the likes of Olympians, astronauts and war heroes were first chosen. They were also the second largest contractor after Black Mesa for the Department of Defense from 1952 to 1954. Aperture's developments in this period included Repulsion Gel, the Weighted Storage Cube, the 1500 Megawatt Super Colliding Super Button and the Aperture Science Portable Quantum Tunneling Device, an early and significantly larger version of the modern Portal Gun.</p><p>By the 1970s, Aperture Science was financially unstable. The Olympians, astronauts and war heroes that were used as test subjects were replaced with vagrants who were paid $60 for their time. Aperture Science would continue its research and created Propulsion Gel.</p><p>In the 1980s, test participation became mandatory for all staff, raising the quality of the test subjects, but diminishing employee retention. Aperture's financial problems were severe at this time, but development continued. Moon rocks were used to create Conversion Gel, an efficient portal conductor. Cave Johnson would also be poisoned by his experiments with moon rocks and become deathly ill. As his health degraded he delegated his leadership to his assistant Caroline, asking that her consciousness be placed in a computer. Testing continued with the hope that passing through portals repeatedly might somehow cure Cave Johnson of his illness. Aperture Science also began development of its Genetic Lifeform and Disk Operating System, an artificial intelligence which would be used to oversee scientific testing.</p><p>In 1998, GLaDOS was brought online for the first time during Aperture Science's annual bring-your-daughter-to-work-day. GLaDOS instantly became self-aware and homicidal. GLaDOS flooded the enrichment center with a deadly neurotoxin, killing most of the scientists. Aperture Science was effectively shut down and placed into a permanent testing cycle by GLaDOS.", quote="Look at me still talking, when there's science to do.", quoteAuthor='GLaDOS', representative='Derek Alfsen')
alan = Country(name='Buy N Large',icon='static/img/bnl_flag.jpg',category='Friendly Neighborhood Conglomerate',dateEstablished='New Jersey, USA', description="According to The History of Buy n Large, the corporation got its start as a maker of frozen yogurt.It was a small business called Buy Yogurt. Later on, the business eventually acquired Large Industries, a men's suit company. The combined entity became known as Buy n' Large (note how there once was an apostrophe after the n). The dates of Buy Yogurt's founding and its acqusition of Large Industries are unknown. However, by the year 2057, as shown on the Buy n Large website, the conglomerate became a worldwide leader in the fields of aerospace, agriculture, construction, consumer goods, corporate grooming, earth transport, electronics, energy, engineering, finance, food services, fusion research, government, hydro-power, infrastructures, media, medical science, mortage loans, pet care, pharmaceuticals, phsycotherapies, ports and harbors, real estate, repairs, retail, robotics, science/health, space, storage, super centers, super grids, travel services, utilities, and watermills. The corporation's control affected other companies as well. It seemed as though other businesses wanted BnL to buy them out, such as Headr Inc. which gave BnL control of the world news headlines.", quote='Buy, Shop, Live.', quoteAuthor='Buy N Large Slogan', representative='Alan You')
alice = Country(name='CHOAM',icon='static/img/choam_flag.jpg',category='Chartered Company',dateEstablished='Arrakis', description="The Combine Honnete Ober Advancer Mercantiles or CHOAM essentially controls all economic affairs across the cosmos, although it relies upon the Spacing Guild for transport across space due to the Guild's monopoly on faster-than-light travel.</p><p>CHOAM touched almost all products the Guild will transport, from art forms to technology and of course melange.</p><p>Many Houses depend on CHOAM profits, and an enormous proportion of those depend on melange.</p><p>CHOAM directorships were the real evidence of political power in the Imperium, passing with the shifts of voting strength within the Landsraad as it balanced itself against the Emperor and his supporters. Directorship in the CHOAM was the key to wealth, each noble House dipping from the company's coffers whatever it could under this power.</p><p>The corporation's management and board of directors are controlled by the Padishah Emperor and the Landsraad (with the Spacing Guild and the Bene Gesserit as silent partners). Because of its control of inter-planetary commerce, CHOAM is the largest single source of wealth in the Old Empire; as such, influence in CHOAM (through partisans within it and control of directorships) is the central goal of political maneuvering, both to receive dividends and also (it is implied) to skim off profits.</p><p>The structure of CHOAM is similar to that of a publicly-held corporation. It consists of shareholders, and, as in a public company, major shareholders are given directorships to lead in the board of directors. In this case, however, all shareholders are nobles from the Landsraad, which consists of the Minor Houses, the Great Houses and the Imperial House. The Great Houses predictably hold the directorships of the company, but the Emperor is able to give out directorships and revoke directorships at whim. This strains the analogy between CHOAM directors and real-life shareholders: Individuals can be removed from a board of directors, but this does not typically involve revoking their stock.", quote="He who controls the Spice controls the universe.", quoteAuthor='Baron Harkonnen', representative='Alice Weaver')
katie = Country(name='Cyberdyne Systems',icon='static/img/cyberdyne_systems_flag.jpg',category='Manufacturing Corporation',dateEstablished='Sunnyvale, California, USA', description="Cyberdyne is initially a benign manufacturing corporation at 18144 El Camino Real, Sunnyvale, California. Its products are unknown, but from the equipment in its factory and its high tech-sounding name, it seems possible that Cyberdyne might have been some sort of smaller parts producer for larger manufacturers of high tech equipment.</p><p>A Series 800 Terminator, which is sent from the future and designed to kill humans, is crushed in one of the hydraulic presses in Cyberdyne's factory. Thus, the company obtains the machine's wreckage, including its CPU chip and an arm.</p><p>After reverse engineering the Terminator's remains, Cyberdyne reverse engineers its CPU and creates a powerful new microprocessor for weapons systems, becoming a major contractor for the US military.</p><p>Cyberdyne eventually develops Skynet, a network of supercomputers that employ artificial intelligence in order to replace human beings as commercial and military aircraft pilots, and for the control of other military systems, including nuclear missiles. The system goes online on August 4, 1997. On August 29, 1997, Skynet becomes self-aware. In a panic, humans attempt to shut it down, but Skynet retaliates by launching a nuclear attack against Russia, knowing that the Russian counterattack will eliminate its enemies in the United States, initiating an indeterminately long period of global warfare. The battle pits humans against machines, which develop ever-increasing capabilities. The event is later known as Judgment Day.</p><p>In an effort to prevent Judgment Day from occurring, Cyberdyne's headquarters are destroyed by a group of saboteurs in 1995: John Connor, future leader of the human resistance, his mother Sarah Connor, and a second Series 800 Terminator that traveled back in time, with Miles Dyson, Cyberdyne's lead researcher, assisting them in this endeavor.", quote="We are the Global Digital Defense Network.", quoteAuthor='Cyberdyne Systems Motto', representative='Katie Hunt')
lizzy = Country(name='Dunder Mifflin',icon='static/img/dunder_mifflin_flag.jpg',category='Paper Company',dateEstablished='Scranton, Pennsylvania, USA', description="Dunder Mifflin Inc. (stock symbol DMI) is a mid-cap regional paper- and office-supply distributor with an emphasis on servicing small-business clients. With a corporate office in New York City, Dunder Mifflin has branches in Albany, Utica, Scranton, Akron, Nashua, Buffalo and Rochester.</p><p>For years, Dunder Mifflin was a dying company that was unable to compete with modern chains such as Staples and Office Depot. The company still used traditional salesman rather than the Internet, causing most customers to leave for the nation-wide chains, and was unable to adapt to an increasingly paperless world. Ryan Howard, a new employee of Scranton Branch, predicted the company would be obsolete by 2017. In 2007, Ryan became Vice President of Sales and began a massive restructuring of the entire company, including a new website that would help make sales more efficient. However, his website was a failure (due to an ill-advised social networking feature) and he was later arrested for fraud (he had the Scranton branch label sales they made on the phone as website sales).", quote="Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.", quoteAuthor='Michael Scott', representative='Lizzy Varnell')
david = Country(name='Galactic Empire',icon='static/img/galactic_empire_flag.jpg',category='Dark Side Magocracy',dateEstablished='Imperial Center', description="In the war-weary last days of the Galactic Republic, Supreme Chancellor Palpatine declared a New Order of government meant to sweep away the injustices and inefficiencies of its predecessor. He promised that the First Galactic Empire, under his rule, would usher in a thousand years of peace.</p><p>Rather than offer the people of the galaxy newfound hope, the Empire instead became a tyrannical regime. The rule of the people was pulled away from the Senate, and instead given to appointed regional governors.</p><p>Accompanying the growth of the Empire was a huge military buildup. The clone troopers of the Republic became the stormtroopers of the Empire. The Imperial starfleet of Star Destroyers and TIE fighters maintained order in the galaxy. The Emperor hoped that fear of the Death Star's power would crush any thoughts of rebellion.", quote="We are an Empire ruled by the majority! An Empire of laws, not of politicians! An Empire devoted to the preservation of a just society. We are an Empire that will stand for ten thousand years!", quoteAuthor='Emperor Palpatine', representative='David Rooney')
shane = Country(name='Stark Industries',icon='static/img/stark_industries_flag.jpg',category='Weapons and Technology Company',dateEstablished='New York City, New York, USA', description="Stark Industries is a weapons and technology company founded and owned by Howard Stark. In World War II, Stark Industries built 100,000 planes to help the Allies forces, quickly establishing them as a military contractor. Stark Industries also assisted the Strategic Scientific Reserve fight against HYDRA. After Howard's death, ownership passed to his son, Tony and the company was run by Obadiah Stane until Tony was old enough to take over. Under Tony's leadership, Stark Industries became the world leader in the development of manufacturing advanced weapons. Stark Industries quickly branched out into other scientific fields including aeronautics, robotics, micro-technology and fringe science. After returning home from being held captive, Tony stopped Stark Industries from manufacturing weapons and focused instead on clean energy. Later as Tony continues to operate as Iron Man, he realizes that the Paladium core of his Arc reactor is slowly poisoning him and appoints Pepper Potts as Chairman and CEO of Stark Industries, though she later resigned after Tony found a cure for the palladium poisoning that was killing him. After the Battle of New York, Pepper once again became the CEO of Stark Industries.", quote='Better living through technology.', quoteAuthor='Stark Industries Slogan', representative='Shane Fry')
brad = Country(name='The Globex Corporation',icon='static/img/globex_corporation_flag.jpg',category='Friendly and Innocent High-Tech Company',dateEstablished='Cypress Creek, USA', description="The Globex Corporation is a company run by Hank Scorpio. Disguised as a friendly and innocent high-tech company, Globex is actually a front for an evil organization that Hank Scorpio uses to take over the East Coast of America.</p><p>The headquarters of the Globex Corporation is located in Cypress Creek, a company town built to house employees of the Globex Corporation.The \"innocent\" part of Globex Corporation showed that the work in Globex is very casual. The headquarters contains a fitness room, and employees are allowed to dress in casual wear. According to Hank Scorpio, Globex Corporation doesn't believe in walls (only windows, as evident in the headquarters). There is also lots of greenery inside the Globex headquarters.</p><p>The darker side of Globex Corporation is revealed in the form of a large \"doomsday device\" located in a large chamber under a mountain, which Hank Scorpio attempted to use to take over the East Coast, which he does. A reference was made to a Weather Control and Bacteriological Warfare division within the Globex Corporation. The headquarters is powered by its own nuclear generator, once managed by Homer Simpson, who was a temporary employee until his family wanted to leave.</p><p>The United States Army launched a full-on assault on Globex Headquarters at the same time Homer requested Scorpio's advice on the above issue. Presumably the attack failed, since the operation to take the East Coast was successful.", quote="Your dreams may vary from those of Globex Corporation, its subsidiaries and shareholders.", quoteAuthor='Globex Commercial', representative='Brad Garland')
josh = Country(name='The Guild of Calamitous Intent',icon='static/img/guild_calamitous_intent_flag.jpg',category='Evil Organization of Evil',dateEstablished='Unknown Location', description="The Guild of Calamitous Intent is an organization that oversees the operations of super-villains. Led by the Sovereign, this organization is larger than the The Peril Partnership, the Fraternity of Torment and all unlicensed villains combined. Providing organized havoc since 1910, The Monarch, Baron Underbheit, Phantom Limb and many other super villains on the show are or were a part of this organization.</p><p>The original incarnation of the Guild (which did not contain the suffice clause \"of Calamitous Intent\") was a group very similar to The League of Extraordinary Gentlemen, consisting principally of Col. Venture, Fantômas, Sandow, Oscar Wilde, Samuel Clemens, and Aleister Crowley. The Guild was formed to protect a mysterious device known as The Orb, with Lloyd Venture leading the team under the title Grand Protector of the Orb.</p><p>Even though nobody is sure what The Orb actually does, its existence had created a serious rift within the Guild, splitting its members between those who wanted to activate it and those who wanted to keep it safe. In the episode ORB, we see that a great battle had broken out between the disparate members of the Guild over possession of the device. At this time, The Orb was in the possession of Col. Venture and other Guild members aboard Venture's airship. As the battle raged, Fantômas and Samuel Clemens argued that the only way to win was to activate the device. But Col. Venture and Oscar Wilde disagreed, with Wilde exclaiming, \"For shame! This guild was founded to protect and serve man at his best, not to be a guild of calamitous intent!\"</p><p>At some point it seems the Guild splintered, or altered, with the Guild of Calamitous Intent being headed by the usurper, Fantômas.", quote="Hate you can trust.", quoteAuthor='Guild of Calamitous Intent Slogan', representative='Josh Cohen')
bryce = Country(name='Wayne Enterprises',icon='static/img/wayne_enterprises_flag.jpg',category='International Conglomerate',dateEstablished='Gotham City, USA', description="Based in Gotham City, WayneCorp was founded in the 17th century but officially became a company in the 19th century under Alan Wayne. It has grown to become one of the world's top ten multinational conglomerates. Today, WayneCorp continues to achieve excellence across a wide range of industry sectors and markets, employing some 170,000 people in 170 countries. The current CEO and Chairman, Bruce Wayne, is a keen modernizer and continues to grow the business in the financial sector and in high-end technologies. Bruce Wayne maintains a 51% majority ownership/control of the common stock, as the controlling stockholder of Wayne Enterprises. This allows for the prevention of any hostile takeover attempts of the company by a corporate raider or nefarious individual, attempting to seek control of the vast Wayne empire. Another 30% of the common stock is in friendly hands of allies of Bruce Wayne. Therefore, any hostile takeover attempts of Wayne Enterprises would be unlikely. Lucius Fox is the acting CEO and the Senior Vice President of Finance, Miss Wells (Harvard MBA in Economics) works closely with Mr. Wayne to inform and ensure major shareholders vote their proxies in favor of the board of directors, assuring Bruce Wayne and his executives, control and influence of company decisions, policies, and operational procedures.", quote="Mister Wayne, if you don't want to tell me exactly what you're doing, when I'm asked, I don't have to lie. But don't think of me as an idiot.", quoteAuthor='Lucious Fox', representative='Bryce Hunt')
michael = Country(name='Weasleys\' Wizard Wheezes',icon='static/img/weasleys_wizard_wheezes_flag.jpg',category='Joke Shop',dateEstablished='Diagon Alley, London, USA', description="Weasleys' Wizard Wheezes, also known as Weasley and Weasley is a joke shop located at Number 93 Diagon Alley founded by Fred and George Weasley. It sells practical joke objects, such as Extendable Ears, a Reusable Hangman, and Fred and George's special WonderWitch products, such as Love Potions, Ten-Second Pimple Vanishers,  Pygmy Puffs and Skiving Snackboxes. There is also a section of Muggle Magic Tricks \"for freaks like Dad\", which are said to do steady business, despite not being big sellers. The shop also sells a number of defensive magical objects. This establishment started out as an 'owl-post service' led by the twins from The Burrow, their home. A year later the establishment was led by the twins inside Hogwarts, selling joke-products until the final shop was opened.", quote="Why are you worrying about You-Know-who? You should be worrying about U-No-Poo, the constipation sensation that's gripping the nation!", quoteAuthor='Sign outside Weasleys\' Wizard Wheezes', representative='Michael Woodall')
erica = Country(name='Willy Wonka Candy Company',icon='static/img/wonka_flag.jpg',category='Candy Company',dateEstablished='Liverpool, England', description="Willy Wonka began his candy empire in 1985 with a small shop in town. The word spread across the world, Wonka decided to expand. Five years later, he built a chocolate factory, \"fifty times as big as any other.\"</p><p>His recipes were so popular, that competitors were stealing his secret recipes by sending in spies to pose as his workers. Feeling betrayed, Wonka told all his workers to go home and closed the factory in an attempt to save it.</p><p>Some time later, he re-opened the factory and chocolate was created once more. But that left a mystery: no person had been in the factory for 15 years. Yet in the last decade and a half, the candy tasted better and better. It is revealed during a tour that the workers are a race of people called the Oompa-Loompas from Loompaland.", quote="A little nonsense now and then, is relished by the wisest men.", quoteAuthor='Willy Wonka', representative='Erica Lin')

template = Country(name='',icon='static/img/_flag.jpg',category='',dateEstablished='', description="", quote="", quoteAuthor='', representative='')
# scott = Country(name='Globex',icon='static/img/globex_flag.png',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Scott N')
# kim = Country(name='Acme',icon='static/img/shinra_flag.jpg',category='Friendly Neighborhood Conglomerate',dateEstablished='2030 BC', description='Description of Globex goes here', quote='Quote', quoteAuthor='some Author', representative='Kim N')

db.session.add(derek)
db.session.add(alan)
db.session.add(alice)
db.session.add(katie)
db.session.add(lizzy)
db.session.add(david)
db.session.add(shane)
db.session.add(brad)
db.session.add(josh)
db.session.add(bryce)
db.session.add(michael)
db.session.add(erica)

# db.session.add(scott)
# db.session.add(kim)
db.session.commit()


small_world = Game(name='Small World',icon='static/img/small_world.jpg',difficulty='Medium',points=12,min_players=2, max_players=5,description='In Small World, players vie for conquest and control of a world that is simply too small to accommodate them all.</p><p>Designed by Philippe Keyaerts as a fantasy follow-up to his award-winning Vinci, Small World is inhabited by a zany cast of characters such as dwarves, wizards, amazons, giants, orcs, and even humans, who use their troops to occupy territory and conquer adjacent lands in order to push the other races off the face of the earth.</p><p>Picking the right combination from the 14 different fantasy races and 20 unique special powers, players rush to expand their empires - often at the expense of weaker neighbors. Yet they must also know when to push their own over-extended civilization into decline and ride a new one to victory!</p><p>On each turn, you either use the multiple tiles of your chosen race (type of creatures) to occupy adjacent (normally) territories - possibly defeating weaker enemy races along the way, or you give up on your race letting it go "into decline". A race in decline is designated by flipping the tiles over to their black-and-white side.</p><p>At the end of your turn, you score one point (coin) for each territory your races occupy. You may have one active race and one race in decline on the board at the same time. Your occupation total can vary depend on the special abilities of your race and the territories they occupy. After the final round, the player with the most coins wins.', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building', coop=False)
dominion = Game(name='Dominion', icon='static/img/dominion.jpg', difficulty='Medium', points=6, min_players=2, max_players=4, description="You are a monarch, like your parents before you, a ruler of a small pleasant kingdom of rivers and evergreens. Unlike your parents, however, you have hopes and dreams! You want a bigger and more pleasant kingdom, with more rivers and a wider variety of trees. You want a Dominion! In all directions lie fiefs, freeholds, and feodums. All are small bits of land, controlled by petty lords and verging on anarchy. You will bring civilization to these people, uniting them under your banner.</p><p>But wait! It must be something in the air; several other monarchs have had the exact same idea. You must race to get as much of the unclaimed land as possible, fending them off along the way. To do this you will hire minions, construct buildings, spruce up your castle, and fill the coffers of your treasury. Your parents wouldn't be proud, but your grandparents, on your mother's side, would be delighted.</p><p>In Dominion, each player starts with an identical, very small deck of cards. In the center of the table is a selection of other cards the players can \"buy\" as they can afford them. Through their selection of cards to buy, and how they play their hands as they draw them, the players construct their deck on the fly, striving for the most efficient path to the precious victory points by game end.</p><p>Dominion is not a CCG, but the play of the game is similar to the construction and play of a CCG deck. The game comes with 500 cards. You select 10 of the 25 Kingdom card types to include in any given play—leading to immense variety.", playingTime='30 minutes', category='Card Game, Medieval', coop=False)

template = Game(name='', icon='static/img/.jpg', difficulty='Medium', points=, min_players=, max_players=, description="", playingTime=' minutes', category='', coop=False)
# smallworld2 = Game(name='Small World2',icon='static/img/small_world.jpg',difficulty='Medium2',points=12,min_players=2, max_players=5,description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building', coop=True)
# smallworld3 = Game(name='Small World3',icon='static/img/small_world.jpg',difficulty='Medium2',points=12,min_players=2, max_players=9,description='Description of Small World goes here', playingTime='80 minutes', category='Civilization, Fantasy, Territory Building', coop=False)

db.session.add(small_world)

# db.session.add(smallworld2)
# db.session.add(smallworld3)
db.session.commit()


# g1 = Match(gameId=small_world.id,duration=1)
# g2 = Match(gameId=small_world.id,duration=2)

# db.session.add(g1)
# db.session.add(g2)
db.session.commit()


# p1 = GamePlayer(matchId=g1.id, countryId=alan.id, place=1)
# p2 = GamePlayer(matchId=g1.id, countryId=shane.id, place=2)
# p3 = GamePlayer(matchId=g2.id, countryId=shane.id, place=1)
# p4 = GamePlayer(matchId=g2.id, countryId=alan.id, place=2)
# p5 = GamePlayer(matchId=g2.id, countryId=kim.id, place=3)
# p6 = GamePlayer(matchId=g2.id, countryId=scott.id, place=0)

# db.session.add(p1)
# db.session.add(p2)
# db.session.add(p3)
# db.session.add(p4)
# db.session.add(p5)
# db.session.add(p6)
db.session.commit()
