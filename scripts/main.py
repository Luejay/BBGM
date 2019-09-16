from league import *
from player import *
from nation import *
from team import *


all_200 =player("200","200",100,japan,ability=player.return_ability())

stephen_curry = player("Stephen",'Curry',31,usa,ability = player.return_ability(speed = 200,power = 80,jump = 40,three_pt=200,mid_pt=200,dunk=70,layup=170,rebound=70,block=20,steal=140,dribble=184,pas=180) ,height = 190,freethrow_percentage= 92.1)
kevin_durant = player("Kevin","Durant",31,usa,ability=player.return_ability(height = 140,speed =180,power = 170,jump = 170,three_pt=180,mid_pt=194,free_throw=180,dunk=200,layup =180,rebound = 150,block=160,steal=100,dribble = 170,pas = 120),height = 213,freethrow_percentage=89,position = "F")
klay_thompson = player("Klay","Thompson",30,usa,ability=player.return_ability(speed = 130,power = 80,jump = 60,three_pt=180,mid_pt=180,dunk = 130,layup= 148,rebound=80,block=110,steal = 120,dribble = 128, pas = 80 ),height = 201,freethrow_percentage=84.8)
draymond_green = player("Draymond",'Green',30,usa,ability=player.return_ability(height = 110,speed = 70,power = 180,jump = 120,three_pt= 120,mid_pt=140,free_throw= 140,dunk=150,layup=166,rebound=130,block = 200,steal = 170,dribble = 60,pas = 150),position = "PF")
demarcus_cousins = player("Demarcus",'Cousins',28,usa, ability=player.return_ability(speed = 120,power = 180,jump = 140,three_pt= 130,mid_pt=120,dunk =190,layup = 110,rebound = 180,block = 180,steal=90,dribble=70,pas = 60),height = 211,freethrow_percentage=74.6)

kyrie_irving = player("Kyrie",'Irving',27,usa,ability=player.return_ability(speed = 200,power = 80,jump=130,three_pt=150,mid_pt=180,dunk = 110, layup=180,rebound=50,block = 20,steal = 140,dribble = 200,pas = 190),height = 190,freethrow_percentage=91.3)
lebron_james = player('Lebron','James',33,usa,ability=player.return_ability(speed = 180, power = 200,jump = 200,three_pt=140,mid_pt=160,dunk = 200,layup=180,rebound=150,block = 160,steal=130,dribble = 130,pas = 140),freethrow_percentage=73.1,height = 203)

nikola_jokic = player("Nikola",'Jokic',24,serbia,ability = player.return_ability(jump = 160,speed = 130,power = 160,three_pt= 100,mid_pt=140,dunk = 160,layup= 140,rebound = 240,block = 80,steal = 120,dribble = 80,pas = 180),height = 213.36,freethrow_percentage=82.1)

giannis_antetokounmpo = player("Giannis",'Antetokounmpo',24,greece,ability = player.return_ability(jump = 200,speed = 130,power = 180,three_pt=130,mid_pt= 160,dunk = 200,layup=160,rebound=190,block = 140,steal = 140,dribble = 140,pas = 130),height = 211,freethrow_percentage=76,position = "F")

james_harden = player("James",'Harden',29,usa,ability = player.return_ability(jump = 170,speed = 180,power = 160,three_pt= 180,mid_pt=180,dunk = 160,layup = 180,rebound = 140,block = 50,steal = 160,dribble = 190,pas = 140),height = 196,freethrow_percentage=87.9,position = "SG")

anthony_davis = player("Anthony",'Davis',25,usa,ability=player.return_ability(jump = 180,speed = 140,power = 170,three_pt=100,mid_pt=160,dunk = 200,layup = 160,rebound = 200,block = 200,steal = 140,dribble = 100,pas = 80),freethrow_percentage=80,height = 208)

kawhi_leonard = player("Kawhi",'Leonard',27,usa,ability=player.return_ability(jump = 140,speed = 170,power = 150,three_pt=170,mid_pt=180,dunk = 160,layup=170,rebound=160,block = 200,steal = 200,dribble = 120,pas = 80),freethrow_percentage=85.4,height = 201,position = "F")

blake_griffin = player("Blake",'Griffin',29,usa,ability=player.return_ability(jump = 200,speed = 140,power = 160,three_pt=90,mid_pt=140,dunk = 200,layup = 140,rebound = 150,block = 90,steal = 110,pas = 130),height = 208,freethrow_percentage=78,position = "F")

russell_westbrook = player("Russell",'Westbrook',30,usa,ability=player.return_ability(jump = 180,speed = 200,power = 180,three_pt=160,mid_pt=160,dunk = 180,layup = 150,rebound = 170,block = 70,steal = 140,dribble = 140,pas = 200),height=190,freethrow_percentage=65.6,position="G")
paul_george = player("Paul",'George',29,usa,ability=player.return_ability(jump = 160,speed =180,power = 160,three_pt=150,mid_pt=165,dunk = 190,layup = 170,rebound = 170,block = 110,steal = 200,dribble = 110,pas = 80),height = 206,freethrow_percentage=84.4,position="GF")

def debug():
    all_average = player("average",'average',25,usa,ability=player.return_ability(100,100,100,100,100,100,100,100,100,100,100,100,100,100))
    print(all_average)




japan_league = NBC()

for team in japan_league.all_teams:
    team.league = japan_league

japan_league.create_all_roster()



japan_league.create_all_star_team()
japan_league.sort_all_roster()

japan.sort_national_roster()


european_league = EL()


'''
european_league.create_all_roster()
european_league.sort_all_roster()

japan_league.ability_ranking()
print()
european_league.ability_ranking()

print()

nation.national_starting_roster_ranking()

japan.print_national_roster()

japanese_player_on_other_league()
'''
'''
for team in japan_league.all_teams:
    team.calculate_player_value()
    print(team.teamnm+": ")
    team.all_players.sort(key = lambda x: team.player_value[x],reverse = True)
    for player in team.all_players:

        print(team.player_value[player],end = " ")
        print(player)
    print()
'''

average_player = player("Average","average",20,japan,ability = player.return_ability(block = 92))

went_in = 0
times = 10000

for i in range(times):
    if all_200.shoot_ball(0,shot_type = "mid_range"):
        went_in+=1
print("Open mid range: ",end = "")
print((went_in/times)*100)

went_in = 0
times = 10000

for i in range(times):
    if all_200.shoot_ball(0,shot_type='mid_range',opponent_player=average_player):
        went_in+=1
print("Contested mid range: ",end = "")
print((went_in/times)*100)
