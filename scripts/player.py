from random import randint as rand

class player:
    all_players = []

    def return_ability(height = 200,jump = 200,speed = 200,power = 200,three_pt = 200,mid_pt = 200,free_throw = 200,dunk = 200,layup =200,rebound = 200,block = 200,steal = 200,dribble = 200,pas = 200):
        return {'height':height,'jump':jump,'speed':speed,'power':power,'three_pt':three_pt,'mid_pt':mid_pt,'free_throw':free_throw,'dunk':dunk,'layup':layup,'rebound':rebound,'block':block,'steal':steal,'dribble':dribble,'pass':pas}

    def return_position(self,ability):
        pg_adjust =9.0
        sg_adjust = 9.0
        sf_adjust = 9.0
        pf_adjust =9.0
        c_adjust =9.0



        pg =( (ability['height']*0.2)+ability['jump']*0.2+ability['power']*0.2+ability['speed']+ability['three_pt']*0.9 +ability['mid_pt']*0.9+ability['free_throw'] +(ability['dunk']*0.2)+ability['layup']+ (ability['rebound']*0.1)+(ability['block']*0.1)+ (ability['steal']*0.7)+ability['dribble']*1.2+ability['pass']*1.3  )/pg_adjust


        sg = ( (ability['height']*0.3)+ability['jump']*0.4+ability['power']*0.3+ability['speed']*0.8+ability['three_pt']*1.2 + ability['mid_pt']*1.3+ability['free_throw']*1.1+(ability['dunk']*0.4)+ability['layup']+(ability['rebound']*0.1)+(ability['block']*0.3 ) +(ability['steal']*0.7)+(ability['dribble']*0.5)+(ability['pass']*0.6))/sg_adjust


        sf = (ability['height']*0.5 +ability['jump']+ability['power']*0.6+ability['speed']*0.6 +ability['three_pt']*0.6 + ability['mid_pt']*0.8 + ability['free_throw']*0.8 + ability['dunk']*0.9 + ability['layup']*0.7 + ability['rebound']*0.5 + ability['block']*0.5 + ability['steal']*0.7 + ability['dribble']*0.5 + ability['pass']*0.3)/sf_adjust

        pf = (ability['height']*0.8+ability['jump']*0.8+ability['power']*0.9+ability['speed']*0.5 + ability['three_pt']*0.4 + ability['mid_pt']*0.5 + ability['free_throw']*0.6 + ability['dunk'] + ability['layup'] * 0.7 + ability['rebound']*0.8 + ability['block']*0.8 + ability['steal']*0.7 + ability['dribble']*0.3 + ability['pass']*0.2)/pf_adjust


        c =  (ability['height']+ability['jump']*0.9+ability['power']+ability['speed']*0.3 + ability['three_pt'] * 0.2 + ability['mid_pt']*0.2 + ability['free_throw']*0.4 + ability['dunk']*1.1+ ability['layup']*0.5 + ability['rebound']*1.5 + ability['block']+ability['steal']*0.7 + ability['dribble']*0.1+ability['pass']*0.1)/c_adjust

        pg = round(pg)
        sg = round(sg)
        sf = round(sf)
        pf = round(pf)
        c = round(c)

        suited_position = None
        highest_position_rating = 0

        if c >= pg and c>= sg and c>= sf and c>= pf:
            if c == sf or c == pf:
                suited_position = "FC"
            else:
                suited_position = "C"

            highest_position_rating = c
        elif pg >= sg and pg>= sf and pg>= pf:
            if pg == sf or pg == pf:
                suited_position ='GF'
            elif pg == sg:
                suited_position = "G"
            else:
                suited_position = "PG"
            highest_position_rating = pg

        elif sg >= sf and sg >= pf:
            if sg == sf or sg == pf:
                suited_position ="GF"
            elif sg == pg:
                suited_position = "G"
            else:
                suited_position = "SG"
            highest_position_rating = sg
        elif sf >= pf:
            if sf == pf:
                suited_position = "F"
            else:
                suited_position = "SF"
            highest_position_rating = sf

        else:
            suited_position =  "PF"
            highest_position_rating = pf



        #oval = (ability['height'] + ability['three_pt'] + ability['mid_pt'] + ability['free_throw'] + ability['dunk']+ ability['layup'] + ability['rebound'] + ability['block']+ability['steal'] + ability['dribble']+ability['pass'])/11
        #oval = round(oval)

        #rating =round( (oval + highest_position_rating)/2 )



        #height,stanima,three_pt,mid_pt,dunk,layup,rebound,block,steal,dribble,pass

        return {'PG':pg,'SG':sg,'SF':sf,'PF':pf,'C':c,'suited_position':suited_position,'highest_position_rating':highest_position_rating}

    def return_height(cm):
        result = (2.898550724638*cm) - 469.5652173913
        result = round(result)
        return result

    def return_freethrow(percentage):
        result = (4.545454545454*percentage) - 227.27272727

        result = round(result)
        return result

    def return_height_in_cm(height_ability):
        result = (0.345*height_ability)+162
        return round(result)

    def __init__(self,firstname,lastname,age,nation,ability,height = None,freethrow_percentage = None,position = None,mob_character = False,current_team = None):
        self.firstname =firstname
        self.lastname = lastname

        self.age = age
        self.nation = nation
        self.ability = ability # {height, three_pt,mid_pt,free_throw,dunk,layup, rebound, block, steal, dribble, pass,

        for pos in self.ability:
            if self.ability[pos] < 0:
                self.ability[pos] = 0

        self.position_list = self.return_position(ability)

        if height is not None:
            self.ability['height'] = player.return_height(height)

        if freethrow_percentage is not None:
            self.ability['freethrow'] = player.return_freethrow(freethrow_percentage)

        if position is not None:
            self.position_list['suited_position'] = position

        self.height_in_cm = player.return_height_in_cm(self.ability['height'])

        if mob_character != True:
             nation.all_players.append(self)

        self.current_team = current_team

        self.history = []

        self.team_history = []

        self.contract = {"length":None,'money_per_year':None}

    def __repr__(self):
        total = ""

        total += self.lastname + " "
        total+= self.firstname + " "


        total+= "age:" + str(self.age)+' '
        total+='nationality:'+self.nation.name+' '

        total+= str(self.height_in_cm) + "cm "

        #total+="pg: "+ str(self.position_list['PG']) +" sg: "+ str(self.position_list['SG'])+" sf: "+ str(self.position_list['SF']) +" pf: "+ str(self.position_list['PF'])+" c: "+ str(self.position_list['C'])
        #total+=' oval: '+str(self.position_list['oval'])
        total+= " suited position: "+str(self.position_list['suited_position'])
        total+=" highest position rating: "+ str(self.position_list['highest_position_rating'])
        #total+=' rating: '+str(self.position_list['rating'])

        if self.current_team is not None:
            total+= " current team: " + self.current_team.citynm+" " + self.current_team.teamnm
        else:
            total+=" current team: None"


        return total

    def shoot_freethrow(self):
        perc = (0.225*self.ability['free_throw']) + 50

        if rand(1,100) < perc:
            return True
        else:
            return False

    def display_freethrow_percentage(self):
        total = 0
        time = 40000
        for i in range(time):
            if self.shoot_freethrow():
                total += 1

        print(str(total / (time / 100)) + "%")

    def return_useless_player(nation):
        p = player("モブ","モブ男",20,nation,ability=player.return_ability(0,0,0,0,0,0,0,0,0,0,0,0,0,0),mob_character=True,position = "C")
        return p