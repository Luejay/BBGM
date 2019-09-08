from random import randint as rand
from random import uniform as ranf
from random import choice

import player as pl
from firstname import *
from lastname import *


class nation:

    all_nations = []
    total_level = 0




    def __init__(self,name,abb,first_name,last_name,level,city = None):

        self.name = name
        self.abb = abb

        self.first_name = first_name
        self.last_name = last_name

        self.level = level

        self.all_players = []

        nation.all_nations.append(self)
        nation.total_level+=level

        self.starting_roster={'PG':None,'SG':None,'SF':None,'PF':None,'C':None}

        self.bench_roster = {"F1":None,"F2":None,'G1':None,'G2':None,'C1':None,'F3':None,'F4':None,'G3':None,'G4':None,"C2":None}

        self.city = city

    def sort_national_roster(self):
        list_of_players = []
        for i in self.all_players:
            list_of_players.append(i)

        if len(list_of_players) < 15:
            for i in range(15 - len(list_of_players)):
                p =pl.player.return_useless_player(self)
                list_of_players.append( p )

        for i in ["F1","F2",'G1','G2','C1','F3','F4','G3','G4',"C2"]:
            self.bench_roster[i] = None

        self.starting_roster['PG'] = None
        self.starting_roster['SG'] = None
        self.starting_roster['SF'] = None
        self.starting_roster['PF'] = None
        self.starting_roster['C'] = None

        for pos in ['PG','SG','SF','PF','C']:
            list_of_players.sort(key = lambda x: x.position_list[pos],reverse = True)
            player = list_of_players[0]

            if (pos == "PG") and (player.position_list['suited_position'] == "PG" or player.position_list['suited_position'] == "G" or player.position_list['suited_position'] == "GF"):
                self.starting_roster["PG"] = player


                list_of_players.remove(player)
            elif (pos == "SG") and (player.position_list['suited_position'] == "SG" or player.position_list['suited_position'] == "G" or player.position_list['suited_position'] == "GF"):
                self.starting_roster["SG"] = player

                list_of_players.remove(player)
            elif (pos == "SF") and (player.position_list['suited_position'] == "SF" or player.position_list['suited_position'] == "F" or player.position_list['suited_position'] == "GF"or player.position_list['suited_position'] == "FC"):
                self.starting_roster['SF'] = player

                list_of_players.remove(player)
            elif (pos == "PF") and (player.position_list['suited_position'] == "PF" or player.position_list['suited_position'] == "F" or player.position_list['suited_position'] == "GF" or player.position_list['suited_position'] == "FC"):
                self.starting_roster["PF"] = player

                list_of_players.remove(player)

            elif (pos == "C") and (player.position_list['suited_position'] == "C" or  player.position_list['suited_position'] == "FC"):
                self.starting_roster['C'] = player

                list_of_players.remove(player)

        for pos in ['PG','SG','SF','PF','C']:
            if self.starting_roster[pos] is None:

                list_of_players.sort(key=lambda x: x.position_list[pos],reverse = True)
                player = list_of_players[0]
                self.starting_roster[pos] = player
                list_of_players.remove(player)

        # for starters






        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: player.position_list['C'], reverse=True)
            for player in list_of_players:
                if player.position_list['suited_position'] == "C" or player.position_list[
                    'suited_position'] == "FC":
                    self.bench_roster['C1'] = player
                    list_of_players.remove(player)
                    break

        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: (player.position_list['PG']+player.position_list['SG']), reverse=True)
            for player in list_of_players:
                if player.position_list['suited_position'] =="PG" or player.position_list['suited_position'] == "SG" or player.position_list['suited_position'] == "GF" or player.position_list['suited_position'] == "G":
                    self.bench_roster['G1'] = player
                    list_of_players.remove(player)
                    break

        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: (player.position_list['SF']+player.position_list['PF']), reverse=True)
            for player in list_of_players:

                if player.position_list['suited_position'] == "SF" or player.position_list['suited_position'] == "PF" or player.position_list['suited_position'] == "GF" or player.position_list['suited_position'] == "F" or player.position_list['suited_position'] == "FC":
                    self.bench_roster['F1'] = player
                    list_of_players.remove(player)

                    break

        # F1,G1,C1

        if len(list_of_players) >0:
            if self.bench_roster['F1'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['SF'] + player.position_list['PF']),reverse=True)
                self.bench_roster['F1'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])

        if len(list_of_players) > 0:
            if self.bench_roster['G1'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['SG'] + player.position_list['PG']),reverse=True)
                self.bench_roster['G1'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])

        if len(list_of_players) > 0:
            if self.bench_roster['C1'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['C']),reverse=True)
                self.bench_roster['C1'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])



        # F1, G1, C1 adjust





        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: (player.position_list['SF']+player.position_list['PF']), reverse=True)
            for player in list_of_players:

                if player.position_list['suited_position'] == "SF" or player.position_list['suited_position'] == "PF" or player.position_list['suited_position'] == "GF" or player.position_list['suited_position'] == "F" or player.position_list['suited_position'] == "FC":
                    self.bench_roster['F2'] = player
                    list_of_players.remove(player)

                    break

        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: (player.position_list['PG']+player.position_list['SG']), reverse=True)
            for player in list_of_players:
                if player.position_list['suited_position'] =="PG" or player.position_list['suited_position'] == "SG" or player.position_list['suited_position'] == "GF" or player.position_list['suited_position'] == "G":
                    self.bench_roster['G2'] = player
                    list_of_players.remove(player)
                    break

        # F2, G2



        if len(list_of_players) > 0:
            if self.bench_roster['G2'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['SG'] + player.position_list['PG']),reverse=True)
                self.bench_roster['G2'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])

        if len(list_of_players) >0:
            if self.bench_roster['F2'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['SF'] + player.position_list['PF']),reverse=True)
                self.bench_roster['F2'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])
        # F2,G2 adjust




        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: player.position_list['C'], reverse=True)
            for player in list_of_players:
                if player.position_list['suited_position'] == "C" or player.position_list[
                    'suited_position'] == "FC":
                    self.bench_roster['C2'] = player
                    list_of_players.remove(player)
                    break

        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: (player.position_list['PG']+player.position_list['SG']), reverse=True)
            for player in list_of_players:
                if player.position_list['suited_position'] =="PG" or player.position_list['suited_position'] == "SG" or player.position_list['suited_position'] == "GF" or player.position_list['suited_position'] == "G":
                    self.bench_roster['G3'] = player
                    list_of_players.remove(player)
                    break

        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: (player.position_list['SF']+player.position_list['PF']), reverse=True)
            for player in list_of_players:

                if player.position_list['suited_position'] == "SF" or player.position_list['suited_position'] == "PF" or player.position_list['suited_position'] == "GF" or player.position_list['suited_position'] == "F" or player.position_list['suited_position'] == "FC":
                    self.bench_roster['F3'] = player
                    list_of_players.remove(player)

                    break





        # F3,G3,C2

        if len(list_of_players) >0:
            if self.bench_roster['F3'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['SF'] + player.position_list['PF']),reverse=True)
                self.bench_roster['F3'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])

        if len(list_of_players) > 0:
            if self.bench_roster['G3'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['SG'] + player.position_list['PG']),reverse=True)
                self.bench_roster['G3'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])

        if len(list_of_players) > 0:
            if self.bench_roster['C2'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['C']),reverse=True)
                self.bench_roster['C2'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])



        # F3, G3, C2 adjust



        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: (player.position_list['SF'] + player.position_list['PF']),
                                 reverse=True)
            for player in list_of_players:

                if player.position_list['suited_position'] == "SF" or player.position_list['suited_position'] == "PF" or \
                        player.position_list['suited_position'] == "GF" or player.position_list[
                    'suited_position'] == "F" or player.position_list['suited_position'] == "FC":
                    self.bench_roster['F4'] = player
                    list_of_players.remove(player)

                    break

        if len(list_of_players) > 0:
            list_of_players.sort(key=lambda player: (player.position_list['PG'] + player.position_list['SG']),
                                 reverse=True)
            for player in list_of_players:
                if player.position_list['suited_position'] == "PG" or player.position_list['suited_position'] == "SG" or \
                        player.position_list['suited_position'] == "GF" or player.position_list[
                    'suited_position'] == "G":
                    self.bench_roster['G4'] = player
                    list_of_players.remove(player)
                    break

        # F4, G4

        if len(list_of_players) > 0:
            if self.bench_roster['G4'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['SG'] + player.position_list['PG']),
                                     reverse=True)
                self.bench_roster['G4'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])


        if len(list_of_players) > 0:
            if self.bench_roster['F4'] is None:
                list_of_players.sort(key=lambda player: (player.position_list['SF'] + player.position_list['PF']),
                                     reverse=True)
                self.bench_roster['F4'] = list_of_players[0]
                list_of_players.remove(list_of_players[0])



        # F2,G2 adjust

    def print_national_roster(self):

        total = self.name + "\n"

        total += "Starters:\n"

        total+="PG: "+ str(self.starting_roster['PG'])+"\n"
        total+="SG: " +str(self.starting_roster['SG'])+"\n"
        total += "SF: "  +str(self.starting_roster['SF']) + "\n"
        total += "PF: "  +str(self.starting_roster['PF']) + "\n"
        total +=  "C: " + str(self.starting_roster['C']) + "\n"

        total+= "\nReserves:\n"

        if self.bench_roster['G1'] is not None:
            total+= "Bench Guard 1: "+" " +str(self.bench_roster["G1"]) + "\n"
        else:
            total+= "Bench Guard 1: No one\n"

        if self.bench_roster['G2'] is not None:
            total += "Bench Guard 2: " +" " +str(self.bench_roster["G2"]) + "\n"
        else:
            total += "Bench Guard 2: No one\n"

        if self.bench_roster['F1'] is not None:
            total+= "Bench Forward 1: "+" " +str(self.bench_roster["F1"]) + "\n"
        else:
            total+= "Bench Forward 1: No one\n"

        if self.bench_roster['F2'] is not None:
            total += "Bench Forward 2: "  +str(self.bench_roster["F2"]) + "\n"
        else:
            total += "Bench Forward 2: No one\n"

        if self.bench_roster['C1'] is not None:
            total += "Bench Center 1: " +" "+ str(self.bench_roster["C1"]) + "\n"
        else:
            total += "Bench Center 1: No one\n"


        total+="\n"


        if self.bench_roster['G3'] is not None:
            total+= "Bench Guard 3: "+str(self.bench_roster["G3"]) + "\n"
        else:
            total+= "Bench Guard 3: No one\n"

        if self.bench_roster['G4'] is not None:
            total += "Bench Guard 4: " +str(self.bench_roster["G4"]) + "\n"
        else:
            total += "Bench Guard 4: No one\n"

        if self.bench_roster['F3'] is not None:
            total+= "Bench Forward 3: " +str(self.bench_roster["F3"]) + "\n"
        else:
            total+= "Bench Forward 3: No one\n"

        if self.bench_roster['F4'] is not None:
            total += "Bench Forward 4: " +" "+ str(self.bench_roster["F4"]) + "\n"
        else:
            total += "Bench Forward 4: No one\n"



        if self.bench_roster['C2'] is not None:
            total += "Bench Center 2: " +str(self.bench_roster["C2"]) + "\n"
        else:
            total += "Bench Center 2: No one\n"


        print(total)

    def return_nation(non_nation = None):
        total =0

        for i in nation.all_nations:
            if non_nation == None or i not in non_nation:
                total+= i.level

        index  = rand(1,total)
        for i in nation.all_nations:
            if (non_nation == None or  i not in non_nation) and i.level < index:
                index -= i.level

            elif (non_nation == None or  i not in non_nation) and i.level>= index :
                return i

        print("OUT OF LOOP")

    def print_percentage_of_nations(non_nation = None):
        total = {}

        times = 300000

        for i in range(times):
            n = nation.return_nation(non_nation)
            if n.name not in total:
                total[n.name] = 1
            else:
                total[n.name] += 1

        for name, value in sorted(total.items(), key=lambda x: x[1], reverse=True):
            print(name + ": " + str((value / times) * 100) + "%")

    def __repr__(self):

        total = self.name

        for i in self.all_players:
            total+="\n"+ i.firstname+" " + i.lastname +" age:"+ str(i.age)+" position: "+ i.position_list['suited_position']+ " rating: "+str(i.position_list['highest_position_rating'])

        return total

    def return_firstname(self):
        return choice(self.first_name)
    def return_lastname(self):
        return choice(self.last_name)
    def sort_all_national_roster():
        for i in nation.all_nations:
            i.sort_national_roster()

    def national_starting_roster_ranking():
        nation.sort_all_national_roster()
        list_of_teams = []

        for team in nation.all_nations:
            list_of_teams.append(team)

        list_of_teams.sort(key= lambda team: team.starting_roster['PG'].position_list['PG']+team.starting_roster['SG'].position_list['SG']+team.starting_roster['SF'].position_list['SF']+team.starting_roster['PF'].position_list['PF']+team.starting_roster['C'].position_list['C'],reverse = True)

        for index,team in enumerate(list_of_teams):
            print(str(index+1) + " "+ team.name)
            print()
            print("PG: "+str(team.starting_roster['PG']))
            print("SG: " + str(team.starting_roster['SG']))
            print("SF: " + str(team.starting_roster['SF']))
            print("PF: " + str(team.starting_roster['PF']))
            print("C: " + str(team.starting_roster['C']))
            print()





















japan = nation("日本","JPN",japan_firstname,japan_lastname,15,city = ["北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県","茨城県","栃木県","群馬県","埼玉県","千葉県","東京都"," 神奈川県","新潟県","富山県","石川県","福井県","山梨県","長野県","岐阜県","静岡県","愛知県","三重県","滋賀県","京都府"," 大阪府","兵庫県","奈良県","和歌山県","鳥取県","島根県","岡山県","広島県","山口県","徳島県","香川県","愛媛県","高知県"," 福岡県","佐賀県","長崎県","熊本県","大分県","宮崎県","鹿児島県","沖縄県"])

usa = nation("アメリカ合衆国","USA",usa_firstname,usa_lastname,90)#
spain = nation("スペイン","SPA",spain_firstname,spain_lastname,35)#
france = nation("フランス",'FRA',france_firstname,france_lastname,32)#

serbia = nation("セルビア","SER",serbia_firstname,serbia_lastname,30)#
argentina = nation("アルゼンチン","ARG",spain_firstname,spain_lastname,29)#

lithuania =nation("リトアニア",'LIT',lithuania_firstname,russia_lastname,29)#
slovenia = nation("スロベニア","SLO",russia_firstname,russia_lastname,29)#

greece = nation("ギリシャ","GRE",greece_firstname,greece_lastname,28)#

croatia = nation("クロアチア","CRO",croatia_firstname,serbia_lastname,27)#unoriginal

russia = nation("ロシア","RUS",russia_firstname,russia_lastname,25)#
australia = nation("オーストラリア","AUS",australia_firstname,australia_lastname,25)#

brazil = nation("ブラジル","BRA",spain_firstname,spain_lastname,25)#unoriginal

italy = nation("イタリア","ITA",italy_firstname,italy_lastname,24)#

mexico = nation('メキシコ',"MEX",spain_firstname,spain_lastname,24)#

latvia = nation("ラトビア",'LAT',serbia_firstname,serbia_lastname,23)#unoriginal

puerto_rico = nation("プエルトリコ","PUE",spain_firstname,spain_lastname,22)#unoriginal

turkey = nation("トルコ","TUR",turkey_firstname,turkey_lastname,21)#

dominican_republic = nation("ドミニカ共和国",'DOM',spain_firstname,spain_lastname,20)#unoriginal

ukraine = nation("ウクライナ","URK",ukraine_firstname,serbia_lastname,19)# unoriginal
venezuela =nation("ベネズエラ",'VEN',venezuela_firstname,spain_lastname,18)#unoriginal

finland = nation("フィンランド","FIN",finland_firstname,finland_lastname,17)#
germany = nation("ドイツ","GER",germany_firstname,germany_lastname,16)#
canada = nation("カナダ","CAN",canada_firstname,canada_lastname,16)#
czech_republic = nation("チェコ共和国",'CZE',czech_firstname,czech_lastname,14)#

europe = [spain,france,serbia,lithuania,slovenia,greece,croatia,russia,italy,latvia,ukraine,finland,germany,czech_republic]

america = [usa,brazil,mexico,argentina,puerto_rico,dominican_republic,venezuela,canada]

asia = [japan,australia,turkey]


def japanese_player_on_other_league():
    print("Japanese Players on international")
    total = []
    for player in japan.all_players:
        if player.current_team is not None and player.current_team.league.name != "日本バスケットボールコーポレーション":
            total.append(player)

    for p in total:
        print(p)
