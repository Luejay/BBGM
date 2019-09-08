from scripts.nation import *
from scripts.team import *
from scripts.player import *

def rand_num(range,times):
    total = 0
    for i in range(times):
        total+= rand(-1*range,range)

    return total

class league:
    international_freeagents = []

    roster_maximum = 15
    minor_limit = 10

    age_range = [19,20,21,22,22,23,23,24,24,24,25,25,25,25,26,26,26,27,27,27,27,28,28,28,28,29,29,29,29,30,30,30,30,31,31,31,32,32,32,33,33,34,35,36,37,38,39,40]

    def __init__(self):
        self.all_teams = None

    def print_all_players_of_team(self,team):
        print(team.citynm+" "+team.teamnm)
        for player in team.all_players:
            print(player)
    def print_all_players_of_all_teams(self):
        for tm in self.all_teams:
            self.print_all_players_of_team(tm)
            print()

    def starting_roster_ranking(self):

        list_of_teams = []
        for team in self.all_teams:
            list_of_teams.append(team)

        list_of_teams.sort(key= lambda team: team.starting_roster['PG'].position_list['PG']+team.starting_roster['SG'].position_list['SG']+team.starting_roster['SF'].position_list['SF']+team.starting_roster['PF'].position_list['PF']+team.starting_roster['C'].position_list['C'],reverse = True)

        for index,team in enumerate(list_of_teams):
            print(str(index+1) + " "+ team.citynm+" "+team.teamnm)
            print()
            print("PG: "+str(team.starting_roster['PG']))
            print("SG: " + str(team.starting_roster['SG']))
            print("SF: " + str(team.starting_roster['SF']))
            print("PF: " + str(team.starting_roster['PF']))
            print("C: " + str(team.starting_roster['C']))
            print()

    def ability_ranking(self):
        self.all_players.sort(key = lambda player: player.position_list['highest_position_rating'],reverse = True)
        for index in range(20):
            print(str(index+1)+ " " + str(self.all_players[index]))

    def sort_all_roster(self,exception = []):

        for i in self.all_teams:
            if i not in exception:
                i.sort_roster()

    def create_all_roster(self):
        for i in self.all_teams:
            self.create_new_roster(i)

    def height_ranking(self):
        self.all_players.sort(key = lambda player:player.height_in_cm,reverse = True)
        print("Height Ranking: \n")
        for index in  range(10):
            print(str(index+1) + " " + str(self.all_players[index]))


class ABC(league):
    name = "アメリカンバスケットボールコーポレーション"
    abb = "ABC"

    maximum_contract = 4000 # 40 million 四十億

    minumum_contract = 75 # 0.75 億

    salary_cap = 12000 # 120 million

    talent= {'superstar':150,'average':120,'minor':90}

    nation_list = [usa]

    def __init__(self):
        self.all_players = []
        self.free_agent = []

        san_francisco_gold = team('サンフランシスコ','ゴールド','SF')
        los_angeles_woods = team("ロサンゼルス",'ウッズ','LA')
        san_jose_bears = team("サンホセ",'ベアーズ','SJ')
        san_diego_oceans = team("サンディエゴ",'オーシャンズ','SD')
        seattle_space = team("シアトル",'スペース','SEA')
        las_vegas_paradise = team("ラスベガス",'パラダイス','LV')
        salt_lake_city_forests = team("ソルトレイクシティ",'フォレストズ','SLC')
        phoenix_prairies = team("フェニックス",'プレイリーズ','PHO')
        denver_rocks = team("デンバー",'ロックス','DEN')
        oklahoma_city_chiefs = team("オクラホマシティ",'チーフス','OKC')
        el_paso_cats = team("エルパソ",'キャッツ','ELP')
        houston_smoke_fire = team("ヒューストン","スモークファイヤー",'HOU')
        dallas_hooves = team('ダラス','フーブス','DAL')
        san_antonio_river_walks = team("サンアントニオ",'リバーウォークス','SAN')
        omaha_trains = team("オマハ",'トレインズ','OMA')

        kansas_city_stars = team("カンサスシティ",'スターズ','KC')
        new_orleans_bourbons = team('ニューオーリンズ',"ブルボンズ","NO")
        chicago_sprawl = team("シカゴ",'スプロール','CHI')
        





class EL(league):
    name = "ヨーロピアンリーグ"
    abb = "EL"

    maximum_contract = 1000
    minimum_contract = 10

    foreign_player_limit = 2

    talent = {"superstar":110,'average':80,'minor':50}

    salary_cap = 3000

    nation_list = europe

    def __init__(self):

        self.all_players = []
        self.free_agent = []

        # lithuania,slovenia,croatia,latvia,finland

        madrid_chariots = team("マドリード",'チャリオッツ',"MAD",nation = spain)
        barcelona_ponies = team("バルセロナ","ポニーズ","BAR",nation = spain)

        paris_saints = team("パリ",'セインツ','PAR',nation = france)
        marseille_port = team("マルセイユ",'ポート',"MAR",nation = france)

        berlin_united = team("ベルリン","ユナイテッド","BER",nation = germany)
        munich_royals = team("ミュンヘン","ロイヤルズ","MUN",nation = germany)

        belgrade_riverside = team("ベオグラード",'リバーサイド','BGL',nation = serbia)

        athens_angels = team("アテネ","エンジェルズ",'ATH',nation = greece)

        kiev_goldengates = team("キエフ",'ゴールデンゲーツ',"KIV",nation = ukraine)

        moscow_reds = team("モスクワ",'レッズ','MOS',nation = russia)
        petersburg_horseman = team("ペテルブルグ",'ホースマン',"PET",nation = russia)

        prague_libraries = team("プラハ","ライブラリーズ",'PRA',nation = czech_republic)

        rome_gladiators = team("ローマ",'グラディエーターズ','ROM',nation = italy)
        milan_magic = team("ミラノ",'マジック','MIL',nation = italy)

        london_towers = team("ロンドン",'タワーズ','LON')

        bucharest_hunters = team("ブカレスト",'ハンターズ','BUC')

        stockholm_islanders = team("ストックホルム",'アイランダーズ','STO')
        warsaw_gardens = team("ワルシャワ",'ガーデンズ','WAR')
        wien_symphony = team("ウィーン",'シンフォニー','WIE')
        lisbon_reconquers= team("リスボン",'レコンキスターズ','LIS')

        self.eastern_conference = {'name':"西地区",'abb':"西",'team':[belgrade_riverside,athens_angels,kiev_goldengates,moscow_reds,petersburg_horseman,prague_libraries,bucharest_hunters,stockholm_islanders,warsaw_gardens,wien_symphony]}

        self.western_conference = {'name':"東地区",'abb':"東",'team':[madrid_chariots,barcelona_ponies,paris_saints,marseille_port,munich_royals,london_towers,rome_gladiators,milan_magic,lisbon_reconquers,berlin_united]}

        self.all_teams = self.eastern_conference['team']+self.western_conference['team']

        for tm in self.all_teams:
            tm.league = self

    def create_new_roster(self,team):
        star_percentage = 2
        average_percentage =18
        minor_percentage = 80

        height = 0
        jump = 0
        speed = 0
        power=0
        three_pt = 0
        mid_pt = 0
        free_throw= 0
        dunk = 0
        layup = 0
        rebound =0
        block =0
        steal = 0
        dribble = 0
        pas = 0

        foreign_counter =0



        for i in range(5):

            for pos in ['PG','SG','SF','PF','C']:
                is_foreign = foreign_counter<EL.foreign_player_limit and(rand(1,25) <= 2)

                if not is_foreign:
                    nation_of_p = choice(EL.nation_list)
                else:
                    nation_of_p = nation.return_nation(EL.nation_list)
                    foreign_counter+=1

                age = choice(league.age_range)


                perc = rand(1,100)


                if star_percentage >= perc:
                    talent_num = EL.talent['superstar']

                elif average_percentage >= perc-star_percentage:
                    talent_num = EL.talent['average']

                else:
                    talent_num = EL.talent['minor']

                if pos == "PG":
                    height = rand(0,80)+ rand(-15,15) # 40
                    jump = talent_num + rand(-50,0)
                    speed = talent_num+ rand(-10,20)

                    power = talent_num+ rand(-50,0)
                    three_pt =talent_num+ rand(-15,15)

                    mid_pt = talent_num + rand(-10,20)

                    free_throw = rand(100,150) + rand(-30,30) + rand(-20,20)
                    dunk = talent_num+ rand(-30,0)

                    layup = talent_num+ rand(0,30)
                    rebound = talent_num+ rand(-30,0)

                    block = talent_num+ rand(-50,0)

                    steal = talent_num+ rand(-15,15)

                    dribble = talent_num + rand(0,25)  # 15
                    pas = talent_num+ rand(-10,35) # 15


                elif pos == "SG":
                    height = rand(20, 80)+ rand(-15,15)# 50
                    jump = talent_num + rand(-30, 0)
                    speed = talent_num + rand(-15,20)

                    power = talent_num + rand(-30, 0)
                    three_pt = talent_num + rand(0, 30)+rand(0,10)

                    mid_pt = talent_num + rand(0,35)

                    free_throw  = rand(90,160) + rand(-20,20)+ rand(-20,20)
                    dunk = talent_num + rand(-15,15)

                    layup = talent_num + rand(-10, 20) #10
                    rebound = talent_num + rand(-30, 0)

                    block = talent_num + rand(-30, 0) # -15

                    steal = talent_num + rand(-15, 15)

                    dribble = talent_num + rand(-15,15)
                    pas = talent_num + rand(-25,5)

                elif pos == "SF":
                    height = rand(50, 100) + rand(-15,15)# 100
                    jump = talent_num + rand(-15,60)
                    speed = talent_num +rand(-5,35)

                    power = talent_num + rand(-10,30)


                    mid_pt = talent_num + rand(-5,35)

                    free_throw = rand(50,120) + rand(-30,30)+ rand(-20,20)
                    dunk = talent_num + rand(-5,40)

                    layup = talent_num + rand(-10,45)
                    rebound = talent_num + rand(-15,15)

                    block = talent_num + rand(-10,20)

                    steal = talent_num + rand(-15, 15)

                    dribble = talent_num + rand(-5,25)
                    pas = talent_num + rand(-20,10) #-10

                elif pos == "PF":
                    height = rand(40, 120)+ rand(-15,15) #120
                    jump = talent_num + rand(-10,35)
                    speed = talent_num + rand(-5,30)

                    power = talent_num + rand(-10,35)
                    three_pt = talent_num + rand(-15,15)

                    mid_pt = talent_num + rand(-5,30)

                    free_throw = rand(30,100) + rand(-30,30) + rand(-20,20)
                    dunk = talent_num + rand(-5,30)

                    layup = talent_num + rand(-15,30) # -15
                    rebound = talent_num + rand(-15,25) # 10

                    block = talent_num + rand(-10,20)

                    steal = talent_num + rand(-15,15)

                    dribble = talent_num + rand(-30,0) #-15
                    pas = talent_num + rand(-15,15)#-15

                elif pos == "C":
                    height = rand(80, 175) + rand(-25,25) # 120
                    jump = talent_num + rand(-25,5)
                    speed = talent_num + rand(-40, 0)

                    power = talent_num + rand(-15,30)
                    three_pt = talent_num + rand(-50, 0)

                    mid_pt = talent_num + rand(-50, 0)

                    free_throw =  rand(-20,50) + rand(-30,30) + rand(-20,20)
                    dunk = talent_num + rand(0, 30)

                    layup = talent_num + rand(-20, 10)  # -15
                    rebound = talent_num + rand(0,35)  # 10

                    block = talent_num + rand(-15,30)

                    steal = talent_num + rand(-30, 0)

                    dribble = talent_num + rand(-60, 0)  # -15
                    pas = talent_num + rand(-60, 0)  # -20

                p = player(nation_of_p.return_firstname(),nation_of_p.return_lastname(),age,nation_of_p,ability=player.return_ability(height,jump,speed,power,three_pt,mid_pt,free_throw,dunk,layup,rebound,block,steal,dribble,pas),current_team = team)
                team.all_players.append(p)
                self.all_players.append(p)



class NBC(league):
    name = "日本バスケットボールコーポレーション"
    abb = "NBC"

    nation_list = [japan]

    maximum_contract = 400 # 4 million

    minimum_contract = 5 # 0.05 million 五百万

    salary_cap = 1200 # 12 million
    foreign_player_limit = 3



    talent = {"superstar":80,'average':50,'minor':20}

    def __init__(self):

        self.all_players = []

        self.free_agent = []


        hokkaido_braves = team('北海道', 'ブレーブズ', '北海道', japan,"北海道")
        sendai_bears = team('仙台', 'ベアーズ', '仙台', japan, "宮城県")
        niigata_wyverns = team('新潟', 'ワイバーンズ', '新潟', japan, "新潟県")
        iwate_legends = team('岩手', 'レジェンズ', '岩手', japan, "岩手県")
        akita_reds = team('秋田', 'レッズ', '秋田', japan, "秋田県")
        tochigi_wonderlands = team('栃木', 'ワンダーランズ', '栃木', japan, "栃木県")
        aomori_blackstones = team('青森', 'ブラックストーンズ', '青森', japan, "青森県")

        jpn_northnorth = {"name": '北北地区',"abb":"北北",
                          'teams': [hokkaido_braves, sendai_bears, niigata_wyverns, iwate_legends, akita_reds,
                                    tochigi_wonderlands, aomori_blackstones]}


        tokyo_mastertowers = team('東京', 'マスタータワーズ', '東京', japan,"東京都")
        shinjuku_thunders = team("新宿", 'サンダー', '新宿', japan,"東京都")
        funabasi_greens = team("船橋", 'グリーンズ', '船橋', japan,"千葉県")
        kawasaki_factories = team("川崎", 'ファクトリーズ', '川崎', japan, "神奈川県")
        yokohama_flash = team('横浜', 'フラッシュ', '横浜', japan, "神奈川県")
        saitama_wildcats = team('埼玉', 'ワイルドキャッツ', '埼玉', japan,"埼玉県")
        ibaragi_bastion = team('茨城', 'バスティオン', '茨城', japan,"茨城県")

        jpn_northeast = {"name": "北東地区",'abb':"北東",
                         'teams': [tokyo_mastertowers, shinjuku_thunders, funabasi_greens, kawasaki_factories,
                                   yokohama_flash, saitama_wildcats, ibaragi_bastion]}




        sizuoka_turtles = team('静岡', 'タートルズ', '静岡', japan,"静岡県")
        osaka_knights = team('大阪', 'ナイツ', '大阪', japan, "大阪府")
        nagoya_serpents = team('名古屋', 'サーペントズ', '名古屋', japan,"愛知県")
        kyoto_goldentemples = team('京都', 'ゴールデンテンプルズ', '京都', japan,"京都府")
        nagano_lynx = team('長野', 'リンクス', '長野', japan,"長野県")
        gifu_ducks = team('岐阜', 'ダックス', '岐阜', japan,"岐阜県")
        mie_aquadreams = team('三重', 'アクアドリームズ', '三重', japan, "三重県")

        jpn_southeast = {"name": '南西地区', 'abb':'南西',
                         'teams': [sizuoka_turtles, osaka_knights, nagoya_serpents, kyoto_goldentemples, nagano_lynx,
                                   gifu_ducks, mie_aquadreams]}



        hyogo_burners = team('兵庫', 'バーナーズ', '兵庫', japan, "兵庫県")
        fukuoka_searoads = team('福岡', 'シーローズ', '福岡', japan,"福岡県")
        hiroshima_acrokant = team('広島', 'アクロカント', '広島', japan,"広島県")
        ehime_orangedevils = team('愛媛', 'オレンジデビルズ', '愛媛', japan,"愛媛県")
        okayama_heroes = team('岡山', 'ヒーローズ', '岡山', japan,"岡山県")
        kumamoto_castles = team('熊本', 'キャッスルズ', '熊本', japan, "熊本県")
        kagoshima_beast = team('鹿児島', 'ビースト', '鹿児島', japan, "鹿児島県")

        jpn_southsouth = {'name': '南南地区',"abb":"南南",
                          'teams': [hyogo_burners, fukuoka_searoads, hiroshima_acrokant, ehime_orangedevils,
                                    okayama_heroes, kumamoto_castles, kagoshima_beast]}

        self.northern_conference =  {"name":"北コンファレンス","abb":"北コ",'region' :[jpn_northeast,jpn_northnorth],'all_star_team':all_star_team("ノーザンオールスター",(jpn_northnorth['teams']+jpn_northeast['teams']) ) }

        self.southern_conference = {'name':"南コンファレンス","abb":"南コ",'region':[jpn_southeast,jpn_southsouth],'all_star_team':all_star_team("サウザンオールスター",(jpn_southeast['teams']+jpn_southsouth['teams']) ) }

        self.all_teams = [hokkaido_braves, sendai_bears, niigata_wyverns, iwate_legends, akita_reds,tochigi_wonderlands, aomori_blackstones,tokyo_mastertowers, shinjuku_thunders, funabasi_greens, kawasaki_factories,
                                   yokohama_flash, saitama_wildcats, ibaragi_bastion,sizuoka_turtles, osaka_knights, nagoya_serpents, kyoto_goldentemples, nagano_lynx,
                                   gifu_ducks, mie_aquadreams,hyogo_burners, fukuoka_searoads, hiroshima_acrokant, ehime_orangedevils,
                                    okayama_heroes, kumamoto_castles, kagoshima_beast]



    def create_new_roster(self,team):
        star_percentage = 2
        average_percentage =18
        minor_percentage = 80

        height = 0
        jump = 0
        speed = 0
        power=0
        three_pt = 0
        mid_pt = 0
        free_throw= 0
        dunk = 0
        layup = 0
        rebound =0
        block =0
        steal = 0
        dribble = 0
        pas = 0

        foreign_counter = 0



        for i in range(5):

            for pos in ['PG','SG','SF','PF','C']:
                is_foreign = foreign_counter<NBC.foreign_player_limit and (rand(1,25) <= 3)

                if not is_foreign:
                    nation_of_p = choice(NBC.nation_list)
                else:
                    nation_of_p = nation.return_nation(NBC.nation_list)
                    foreign_counter+=1

                age = choice(league.age_range)


                perc = rand(1,100)


                if star_percentage >= perc:
                    talent_num = NBC.talent['superstar']

                elif average_percentage >= perc-star_percentage:
                    talent_num = NBC.talent['average']

                else:
                    talent_num = NBC.talent['minor']

                if is_foreign:
                    talent_num+= rand(6,15)

                if pos == "PG":
                    height = rand(0,80)+ rand(-15,15) # 40
                    jump = talent_num + rand(-50,0)
                    speed = talent_num+ rand(-10,20)

                    power = talent_num+ rand(-50,0)
                    three_pt =talent_num+ rand(-15,15)

                    mid_pt = talent_num + rand(-10,20)

                    free_throw = rand(100,150) + rand(-30,30) + rand(-20,20)
                    dunk = talent_num+ rand(-30,0)

                    layup = talent_num+ rand(0,30)
                    rebound = talent_num+ rand(-30,0)

                    block = talent_num+ rand(-50,0)

                    steal = talent_num+ rand(-15,15)

                    dribble = talent_num + rand(0,25)  # 15
                    pas = talent_num+ rand(-10,35) # 15


                elif pos == "SG":
                    height = rand(20, 80)+ rand(-15,15)# 50
                    jump = talent_num + rand(-30, 0)
                    speed = talent_num + rand(-15,20)

                    power = talent_num + rand(-30, 0)
                    three_pt = talent_num + rand(0, 30)+rand(0,10)

                    mid_pt = talent_num + rand(0,35)

                    free_throw  = rand(90,160) + rand(-20,20)+ rand(-20,20)
                    dunk = talent_num + rand(-15,15)

                    layup = talent_num + rand(-10, 20) #10
                    rebound = talent_num + rand(-30, 0)

                    block = talent_num + rand(-30, 0) # -15

                    steal = talent_num + rand(-15, 15)

                    dribble = talent_num + rand(-15,15)
                    pas = talent_num + rand(-25,5)

                elif pos == "SF":
                    height = rand(50, 100) + rand(-15,15)# 100
                    jump = talent_num + rand(-15,60)
                    speed = talent_num +rand(-5,35)

                    power = talent_num + rand(-10,30)


                    mid_pt = talent_num + rand(-5,35)

                    free_throw = rand(50,120) + rand(-30,30)+ rand(-20,20)
                    dunk = talent_num + rand(-5,40)

                    layup = talent_num + rand(-10,45)
                    rebound = talent_num + rand(-15,15)

                    block = talent_num + rand(-10,20)

                    steal = talent_num + rand(-15, 15)

                    dribble = talent_num + rand(-5,25)
                    pas = talent_num + rand(-20,10) #-10

                elif pos == "PF":
                    height = rand(40, 120)+ rand(-15,15) #120
                    jump = talent_num + rand(-10,35)
                    speed = talent_num + rand(-5,30)

                    power = talent_num + rand(-10,35)
                    three_pt = talent_num + rand(-15,15)

                    mid_pt = talent_num + rand(-5,30)

                    free_throw = rand(30,100) + rand(-30,30) + rand(-20,20)
                    dunk = talent_num + rand(-5,30)

                    layup = talent_num + rand(-15,30) # -15
                    rebound = talent_num + rand(-15,25) # 10

                    block = talent_num + rand(-10,20)

                    steal = talent_num + rand(-15,15)

                    dribble = talent_num + rand(-30,0) #-15
                    pas = talent_num + rand(-15,15)#-15

                elif pos == "C":
                    height = rand(80, 175) + rand(-25,25) # 120
                    jump = talent_num + rand(-25,5)
                    speed = talent_num + rand(-40, 0)

                    power = talent_num + rand(-15,30)
                    three_pt = talent_num + rand(-50, 0)

                    mid_pt = talent_num + rand(-50, 0)

                    free_throw =  rand(-20,50) + rand(-30,30) + rand(-20,20)
                    dunk = talent_num + rand(0, 30)

                    layup = talent_num + rand(-20, 10)  # -15
                    rebound = talent_num + rand(0,35)  # 10

                    block = talent_num + rand(-15,30)

                    steal = talent_num + rand(-30, 0)

                    dribble = talent_num + rand(-60, 0)  # -15
                    pas = talent_num + rand(-60, 0)  # -20

                p = player(nation_of_p.return_firstname(),nation_of_p.return_lastname(),age,nation_of_p,ability=player.return_ability(height,jump,speed,power,three_pt,mid_pt,free_throw,dunk,layup,rebound,block,steal,dribble,pas),current_team = team)
                team.all_players.append(p)
                self.all_players.append(p)

    def count_talent():
        talent_total = {"PG":0,"SG":0,'SF':0,'PF':0,'C':0}

        for teams in NBC.all_teams:
            for player in teams.all_players:
                talent_total[player.position_list['suited_position']] += player.position_list[player.position_list['suited_position']]

        for p in talent_total:
            print(p + ": "+ str(talent_total[p]))

    def create_all_star_team(self):
        self.northern_conference['all_star_team'].sort_roster()
        self.southern_conference['all_star_team'].sort_roster()

