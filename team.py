class team:

    basic_position = ['PG','SG','SF','PF','C']

    def __init__(self,city_name,team_name,abb,city = None,nation = None):
        self.citynm = city_name
        self.teamnm = team_name
        self.abb = abb

        self.city = city

        self.nation = nation

        self.all_players = []

        self.starting_roster = {'PG':None,'SG':None,'SF':None,'PF':None,'C':None}

        self.bench_roster = {"F1":None,"F2":None,'G1':None,'G2':None,'C1':None,'F3':None,'F4':None,'G3':None,'G4':None,"C2":None}

        self.minor_roster = []

        self.league = None

    def __repr__(self):
        total = self.citynm+ " "+ self.teamnm + "\n"

        total += "Starters:\n"

        total+="PG: " + str(self.starting_roster['PG'])+"\n"
        total+="SG: " + str(self.starting_roster['SG'])+"\n"
        total += "SF: " + str(self.starting_roster['SF']) + "\n"
        total += "PF: " + str(self.starting_roster['PF']) + "\n"
        total += "C: " + str(self.starting_roster['C']) + "\n"

        total+= "\nReserves:\n"

        if self.bench_roster['G1'] is not None:
            total+= "Bench Guard 1: "+ str(self.bench_roster["G1"]) + "\n"
        else:
            total+= "Bench Guard 1: No one\n"

        if self.bench_roster['G2'] is not None:
            total += "Bench Guard 2: " + str(self.bench_roster["G2"]) + "\n"
        else:
            total += "Bench Guard 2: No one\n"

        if self.bench_roster['F1'] is not None:
            total+= "Bench Forward 1: "+ str(self.bench_roster["F1"]) + "\n"
        else:
            total+= "Bench Forward 1: No one\n"

        if self.bench_roster['F2'] is not None:
            total += "Bench Forward 2: " + str(self.bench_roster["F2"]) + "\n"
        else:
            total += "Bench Forward 2: No one\n"

        if self.bench_roster['C1'] is not None:
            total += "Bench Center 1: " + str(self.bench_roster["C1"]) + "\n"
        else:
            total += "Bench Center 1: No one\n"


        total+="\n"


        if self.bench_roster['G3'] is not None:
            total+= "Bench Guard 3: "+ str(self.bench_roster["G3"]) + "\n"
        else:
            total+= "Bench Guard 3: No one\n"

        if self.bench_roster['G4'] is not None:
            total += "Bench Guard 4: " + str(self.bench_roster["G4"]) + "\n"
        else:
            total += "Bench Guard 4: No one\n"

        if self.bench_roster['F3'] is not None:
            total+= "Bench Forward 3: "+ str(self.bench_roster["F3"]) + "\n"
        else:
            total+= "Bench Forward 3: No one\n"

        if self.bench_roster['F4'] is not None:
            total += "Bench Forward 4: " + str(self.bench_roster["F4"]) + "\n"
        else:
            total += "Bench Forward 4: No one\n"



        if self.bench_roster['C2'] is not None:
            total += "Bench Center 2: " + str(self.bench_roster["C2"]) + "\n"
        else:
            total += "Bench Center 2: No one\n"

        total+="\nMinor Roster: \n"

        if len(self.minor_roster) ==0:
            total+= "None"

        for i in self.minor_roster:
            total += str(i)+ "\n"

        return total

    def sort_roster(self):
        list_of_players = []
        for i in self.all_players:
            list_of_players.append(i)

        for i in ["F1","F2",'G1','G2','C1','F3','F4','G3','G4',"C2"]:
            self.bench_roster[i] = None


        self.minor_roster.clear()

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
                self.starting_roster["SF"] = player


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

        for player in list_of_players:
            self.minor_roster.append(player)

    def add_player(self, player, time):
        self.all_players.append(player)

        contract_display= None

        money = player.contract['length']

        if money >= 100:
            contract_display = str(money / 100) + "億"
        else:
            contract_display = str(money*100)+"万"




        player.history.append((str(time[2]) + "年" + str(time[0]) + "月" + str(time[1]) + "日: " + self.citynm+self.teamnm+"と"+str(player.contract['length'])+"年 年俸" + str(player.contract['money_per_year'] )      )                 )
        player.team_history.append()

    def print_starting_roster(self):
        total = self.citynm+ " "+ self.teamnm + "\n"

        total += "Starters:\n"

        total+="PG: " + str(self.starting_roster['PG'])+"\n"
        total+="SG: " + str(self.starting_roster['SG'])+"\n"
        total += "SF: " + str(self.starting_roster['SF']) + "\n"
        total += "PF: " + str(self.starting_roster['PF']) + "\n"
        total += "C: " + str(self.starting_roster['C']) + "\n"

        return total

class all_star_team:
    def __init__(self,name,all_teams):
        self.name = name
        self.all_teams = all_teams
        self.all_players = []

        self.starting_roster = {'PG':None,'SG':None,'SF':None,'PF':None,'C':None}

        self.bench_roster = {"F1":None,"F2":None,'G1':None,'G2':None,'C1':None,'F3':None,'F4':None,'G3':None,'G4':None,"C2":None}



    def __repr__(self):
        total = self.name+"\n"

        total += "Starters:\n"

        total+="PG: " + str(self.starting_roster['PG'])+"\n"
        total+="SG: " + str(self.starting_roster['SG'])+"\n"
        total += "SF: " + str(self.starting_roster['SF']) + "\n"
        total += "PF: " + str(self.starting_roster['PF']) + "\n"
        total += "C: " + str(self.starting_roster['C']) + "\n"

        total+= "\nReserves:\n"

        if self.bench_roster['G1'] is not None:
            total+= "Bench Guard 1: "+ str(self.bench_roster["G1"]) + "\n"
        else:
            total+= "Bench Guard 1: No one\n"

        if self.bench_roster['G2'] is not None:
            total += "Bench Guard 2: " + str(self.bench_roster["G2"]) + "\n"
        else:
            total += "Bench Guard 2: No one\n"

        if self.bench_roster['F1'] is not None:
            total+= "Bench Forward 1: "+ str(self.bench_roster["F1"]) + "\n"
        else:
            total+= "Bench Forward 1: No one\n"

        if self.bench_roster['F2'] is not None:
            total += "Bench Forward 2: " + str(self.bench_roster["F2"]) + "\n"
        else:
            total += "Bench Forward 2: No one\n"

        if self.bench_roster['C1'] is not None:
            total += "Bench Center 1: " + str(self.bench_roster["C1"]) + "\n"
        else:
            total += "Bench Center 1: No one\n"


        total+="\n"


        if self.bench_roster['G3'] is not None:
            total+= "Bench Guard 3: "+ str(self.bench_roster["G3"]) + "\n"
        else:
            total+= "Bench Guard 3: No one\n"

        if self.bench_roster['G4'] is not None:
            total += "Bench Guard 4: " + str(self.bench_roster["G4"]) + "\n"
        else:
            total += "Bench Guard 4: No one\n"

        if self.bench_roster['F3'] is not None:
            total+= "Bench Forward 3: "+ str(self.bench_roster["F3"]) + "\n"
        else:
            total+= "Bench Forward 3: No one\n"

        if self.bench_roster['F4'] is not None:
            total += "Bench Forward 4: " + str(self.bench_roster["F4"]) + "\n"
        else:
            total += "Bench Forward 4: No one\n"



        if self.bench_roster['C2'] is not None:
            total += "Bench Center 2: " + str(self.bench_roster["C2"]) + "\n"
        else:
            total += "Bench Center 2: No one\n"

        return total

    def sort_roster(self):
        list_of_players = []
        for team in self.all_teams:
            for player in team.all_players:
                list_of_players.append(player)

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
                self.starting_roster["SF"] = player

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



