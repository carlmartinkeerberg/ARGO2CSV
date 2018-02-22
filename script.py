from tkinter import*
from tkinter.ttk import*
from tkinter import filedialog

root=Tk()
root.withdraw()

inf=filedialog.askopenfilename(initialdir = "/",title = "Vali fail",filetypes = (("ARGO failid","*.atab"),("kõik failid","*.*")))

def match_teams():
    matched={}
    c=0
    for name in teams:
        matched[str(c)]=name
        c+=1
    matched["-1"]="No Team"
    return matched

def match_judges():
    matched={}
    c=0
    for n in judges:
        matched["judge_"+str(c)]=n
        c+=1
    return matched

def match_clubs():
    clubdict={}
    for club in clubs:
        for team in clubs[club]["Teams"]:
            clubdict[team]=club

    return clubdict

def players_in_teams():
    pairs=[]
    for name in players:
        playername=name
        try:
            teamid=match_teams()[players[name]["Team"]]
        except:
            teamid="No Team"
        tmp=[playername, teamid]
        pairs.append(tmp)

    ids=set()
    team_dict={}
    for item in pairs:
        ids.add(item[1])

    for team in ids:
        team_dict[team]=[]

    for team in ids:
        for pair in pairs:
            if pair[1]==team:
                team_dict[team].append(pair[0])

    return team_dict

def match_speaks():
    speaks={}
    for r in rounds:
        speaks[r]={}
        for b in rounds[r]:
            speaks[r][b]={}
            for j in rounds[r][b]["Judges"]:
                speaks[r][b][j]={}
                prop=match_teams()[rounds[r][b]["Teams"][0]]
                opp=match_teams()[rounds[r][b]["Teams"][1]]
                speaks[r][b][j][prop]=rounds[r][b]["Judges"][j]["Scores_Prop"]
                speaks[r][b][j][opp]=rounds[r][b]["Judges"][j]["Scores_Opp"]

    return speaks

raw=open(inf, encoding="UTF-8")
raw_string=str(raw.readlines())

#clubs
clubs_start=raw_string.find(""","clubs":""")
clubs_end=raw_string.find(""","teams":[{"name":""")
clubs_string=raw_string[clubs_start+11:clubs_end-1]
clubs=clubs_string.split(",{")

clubs_dict={}

for item in clubs:
    name=item[7:].split(""","teams":""")
    name=name[0][1:-1]
    clubs_dict[name]={}

    clubs_teams=item.split(""","teams":""")
    clubs_teams=clubs_teams[1].split(""","id":""")
    clubs_teams=clubs_teams[0][1:-1]
    clubs_dict[name]["Teams"]=clubs_teams

    club_id=item.split(""","id":""")
    club_id=club_id[1].split(""","judges":""")
    club_id=club_id[0][1:-1]
    clubs_dict[name]["ID"]=club_id

    club_judges=item.split(""","judges":""")
    club_judges=club_judges[1].split("}")
    club_judges=club_judges[0][1:-1]
    clubs_dict[name]["Judges"]=club_judges

clubs=clubs_dict

#teams
teams_start=raw_string.find(""","teams":[{"name":""")
teams_end=raw_string.find(""","judges":[{""")
teams_string=raw_string[teams_start+10:teams_end-1]
teams=teams_string.split(",{")
teams[0]=teams[0].strip("{")

team_dict={}

for item in teams:
    name=item.strip(""""name":""").split("""","id":""")
    name=name[0]
    team_dict[name]={}

    team_id=item.split(""","id":""")
    team_id=team_id[1].split(""","players":""")
    team_id=team_id[0]
    team_id=team_id[1:-1]
    team_dict[name]["ID"]=team_id

    players=item.split(""","players":""")
    players=players[1].split(""","rounds":""")
    players=players[0].strip("[").strip("]").split(",")
    team_dict[name]["Players"]=players

    rounds=item.split(""","rounds":""")
    rounds=rounds[1].split(""","club":""")
    rounds=rounds[0].split("""},"round_""")
    round1=rounds[0].strip("{")
    round2=""""round_"""+rounds[1]
    round3=""""round_"""+rounds[2]
    round4=""""round_"""+rounds[3]
    round5=""""round_"""+rounds[4].strip("}}")

    round1_id=round1.split(""":{"participates":""")
    round1_id=round1_id[0]
    round1_id=round1_id[1:-1]
    round2_id=round2.split(""":{"participates":""")
    round2_id=round2_id[0]
    round2_id=round2_id[1:-1]
    round3_id=round3.split(""":{"participates":""")
    round3_id=round3_id[0]
    round3_id=round3_id[1:-1]
    round4_id=round4.split(""":{"participates":""")
    round4_id=round4_id[0]
    round4_id=round4_id[1:-1]
    round5_id=round5.split(""":{"participates":""")
    round5_id=round5_id[0]
    round5_id=round5_id[1:-1]
    
    team_dict[name]["Round_1"]={}
    team_dict[name]["Round_2"]={}
    team_dict[name]["Round_3"]={}
    team_dict[name]["Round_4"]={}
    team_dict[name]["Round_5"]={}

    team_dict[name]["Round_1"]["ID"]=round1_id
    team_dict[name]["Round_2"]["ID"]=round2_id
    team_dict[name]["Round_3"]["ID"]=round3_id
    team_dict[name]["Round_4"]["ID"]=round4_id
    team_dict[name]["Round_5"]["ID"]=round5_id

    round1_part=round1.split("""{"participates":""")
    round1_part=round1_part[1].split(""","ballot":""")
    round1_part=round1_part[0]
    round2_part=round2.split("""{"participates":""")
    round2_part=round2_part[1].split(""","ballot":""")
    round2_part=round2_part[0]
    round3_part=round3.split("""{"participates":""")
    round3_part=round3_part[1].split(""","ballot":""")
    round3_part=round3_part[0]
    round4_part=round4.split("""{"participates":""")
    round4_part=round4_part[1].split(""","ballot":""")
    round4_part=round4_part[0]
    round5_part=round5.split("""{"participates":""")
    round5_part=round5_part[1].split(""","ballot":""")
    round5_part=round5_part[0]

    team_dict[name]["Round_1"]["Participates"]=round1_part
    team_dict[name]["Round_2"]["Participates"]=round2_part
    team_dict[name]["Round_3"]["Participates"]=round3_part
    team_dict[name]["Round_4"]["Participates"]=round4_part
    team_dict[name]["Round_5"]["Participates"]=round5_part

    round1_ballot=round1.split(""","ballot":""")
    round1_ballot=round1_ballot[1]
    team_dict[name]["Round_1"]["Ballot"]=round1_ballot
    round2_ballot=round2.split(""","ballot":""")
    round2_ballot=round2_ballot[1]
    team_dict[name]["Round_2"]["Ballot"]=round2_ballot
    round3_ballot=round3.split(""","ballot":""")
    round3_ballot=round3_ballot[1]
    team_dict[name]["Round_3"]["Ballot"]=round3_ballot
    round4_ballot=round4.split(""","ballot":""")
    round4_ballot=round4_ballot[1]
    team_dict[name]["Round_4"]["Ballot"]=round4_ballot
    round5_ballot=round5.split(""","ballot":""")
    round5_ballot=round5_ballot[1]
    team_dict[name]["Round_5"]["Ballot"]=round5_ballot

teams=team_dict

#judges
judges_end=raw_string.find(""","rooms":""")
judges_string=raw_string[teams_end+11:judges_end-1]
judges=judges_string.split(",{")
judges[0]=judges[0][1:]

judges_dict={}

for item in judges:
    name=item.strip(""""name":""").split(""","rank":""")
    name=name[0][:-1]
    judges_dict[name]={}

    rank=item.split(""","rank":""")
    rank=rank[1].split(""","id":""")
    rank=rank[0]
    judges_dict[name]["Rank"]=rank

    judge_id=item.split(""","id":""")
    judge_id=judge_id[1].split(""","rounds":""")
    judge_id=judge_id[0][1:-1]
    judges_dict[name]["ID"]=judge_id

    rounds=item.split(""","rounds":""")
    rounds=rounds[1].split("""},"club":""")
    rounds=rounds[0]
    rounds=rounds.split(""","round_""")
    rounds[0]=rounds[0].strip("""{"round_""")

    round1_id=rounds[0].split(""":{"participates":""")
    round1_id=round1_id[0][:-2]
    round2_id=rounds[1].split(""":{"participates":""")
    round2_id=round2_id[0][:-2]
    round3_id=rounds[2].split(""":{"participates":""")
    round3_id=round3_id[0][:-2]
    round4_id=rounds[3].split(""":{"participates":""")
    round4_id=round4_id[0][:-2]
    round5_id=rounds[4].split(""":{"participates":""")
    round5_id=round5_id[0][:-2]
 
    judges_dict[name]["Round_1"]={}
    judges_dict[name]["Round_2"]={}
    judges_dict[name]["Round_3"]={}
    judges_dict[name]["Round_4"]={}
    judges_dict[name]["Round_5"]={}

    judges_dict[name]["Round_1"]["ID"]=round1_id
    judges_dict[name]["Round_2"]["ID"]=round2_id
    judges_dict[name]["Round_3"]["ID"]=round3_id
    judges_dict[name]["Round_4"]["ID"]=round4_id
    judges_dict[name]["Round_5"]["ID"]=round5_id

    round1_part=rounds[0].split(""":{"participates":""")
    round1_part=round1_part[1].split(""","ballot":""")
    round1_part=round1_part[0]
    round2_part=rounds[1].split(""":{"participates":""")
    round2_part=round2_part[1].split(""","ballot":""")
    round2_part=round2_part[0]
    round3_part=rounds[2].split(""":{"participates":""")
    round3_part=round3_part[1].split(""","ballot":""")
    round3_part=round3_part[0]
    round4_part=rounds[3].split(""":{"participates":""")
    round4_part=round4_part[1].split(""","ballot":""")
    round4_part=round4_part[0]
    round5_part=rounds[4].split(""":{"participates":""")
    round5_part=round5_part[1].split(""","ballot":""")
    round5_part=round5_part[0]

    judges_dict[name]["Round_1"]["Participates"]=round1_part
    judges_dict[name]["Round_2"]["Participates"]=round2_part
    judges_dict[name]["Round_3"]["Participates"]=round3_part
    judges_dict[name]["Round_4"]["Participates"]=round4_part
    judges_dict[name]["Round_5"]["Participates"]=round5_part

    round1_ballot=rounds[0].split(""","ballot":""")
    round1_ballot=round1_ballot[1][:2].strip(",")
    round2_ballot=rounds[1].split(""","ballot":""")
    round2_ballot=round2_ballot[1][:2].strip(",")
    round3_ballot=rounds[2].split(""","ballot":""")
    round3_ballot=round3_ballot[1][:2].strip(",")
    round4_ballot=rounds[3].split(""","ballot":""")
    round4_ballot=round4_ballot[1][:2].strip(",")
    round5_ballot=rounds[4].split(""","ballot":""")
    round5_ballot=round5_ballot[1][:2].strip(",")

    judges_dict[name]["Round_1"]["Ballot"]=round1_ballot
    judges_dict[name]["Round_2"]["Ballot"]=round2_ballot
    judges_dict[name]["Round_3"]["Ballot"]=round3_ballot
    judges_dict[name]["Round_4"]["Ballot"]=round4_ballot
    judges_dict[name]["Round_5"]["Ballot"]=round5_ballot

    if "shadow" in rounds[0]:
        round1_shadow=rounds[0].split(""","shadow":""")
        round1_shadow=round1_shadow[1][:-1]
    else:
        round1_shadow="false"
    if "shadow" in rounds[1]:
        round2_shadow=rounds[1].split(""","shadow":""")
        round2_shadow=round2_shadow[1][:-1]
    else:
        round2_shadow="false"
    if "shadow" in rounds[2]:
        round3_shadow=rounds[2].split(""","shadow":""")
        round3_shadow=round3_shadow[1][:-1]
    else:
        round3_shadow="false"
    if "shadow" in rounds[3]:
        round4_shadow=rounds[3].split(""","shadow":""")
        round4_shadow=round4_shadow[1][:-1]
    else:
        round4_shadow="false"
    if "shadow" in rounds[4]:
        round5_shadow=rounds[4].split(""","shadow":""")
        round5_shadow=round5_shadow[1][:-1]
    else:
        round5_shadow="false"

    judges_dict[name]["Round_1"]["Shadow"]=round1_shadow
    judges_dict[name]["Round_2"]["Shadow"]=round2_shadow
    judges_dict[name]["Round_3"]["Shadow"]=round3_shadow
    judges_dict[name]["Round_4"]["Shadow"]=round4_shadow
    judges_dict[name]["Round_5"]["Shadow"]=round5_shadow

    club=item.split(""","rounds":""")
    club=club[1].split("""},"club":""")
    club=club[1].strip("}")

    judges_dict[name]["Club"]=club

judges=judges_dict

#rooms
rooms_start=judges_end
rooms_end=raw_string.find("""],"players":""")
rooms_string=raw_string[rooms_start+11:rooms_end]
rooms=rooms_string.split(",{")

rooms_dict={}

for item in rooms:
    name=item.split(""","id":""")
    name=name[0][8:-1]
    rooms_dict[name]={}

    rooms_id=item.split(""","id":""")
    rooms_id=rooms_id[1].split(""","floor":""")
    rooms_id=rooms_id[0][1:-1]
    rooms_dict[name]["ID"]=rooms_id

    floor=item.split(""","floor":""")
    floor=floor[1].split(""","rounds":""")
    floor=floor[0][1:-1]
    rooms_dict[name]["Floor"]=floor

    rounds=item.split(""","rounds":""")
    rounds=rounds[1][:-2]
    rounds=rounds.split(""","round_""")
    rounds[0]=rounds[0][8:]

    round1_id=rounds[0].split(""":{"participates":""")
    round1_id=round1_id[0][:-1]
    round2_id=rounds[1].split(""":{"participates":""")
    round2_id=round2_id[0][:-1]
    round3_id=rounds[2].split(""":{"participates":""")
    round3_id=round3_id[0][:-1]
    round4_id=rounds[3].split(""":{"participates":""")
    round4_id=round4_id[0][:-1]
    round5_id=rounds[4].split(""":{"participates":""")
    round5_id=round5_id[0][:-1]

    rooms_dict[name]["Round_1"]={}
    rooms_dict[name]["Round_2"]={}
    rooms_dict[name]["Round_3"]={}
    rooms_dict[name]["Round_4"]={}
    rooms_dict[name]["Round_5"]={}

    rooms_dict[name]["Round_1"]["ID"]=round1_id
    rooms_dict[name]["Round_2"]["ID"]=round2_id
    rooms_dict[name]["Round_3"]["ID"]=round3_id
    rooms_dict[name]["Round_4"]["ID"]=round4_id
    rooms_dict[name]["Round_5"]["ID"]=round5_id

    round1_part=rounds[0].split(""":{"participates":""")
    round1_part=round1_part[1].split(""","ballot":""")
    round1_part=round1_part[0]
    round2_part=rounds[1].split(""":{"participates":""")
    round2_part=round2_part[1].split(""","ballot":""")
    round2_part=round2_part[0]
    round3_part=rounds[2].split(""":{"participates":""")
    round3_part=round3_part[1].split(""","ballot":""")
    round3_part=round3_part[0]
    round4_part=rounds[3].split(""":{"participates":""")
    round4_part=round4_part[1].split(""","ballot":""")
    round4_part=round4_part[0]
    round5_part=rounds[4].split(""":{"participates":""")
    round5_part=round5_part[1].split(""","ballot":""")
    round5_part=round5_part[0]
    
    rooms_dict[name]["Round_1"]["Participates"]=round1_part
    rooms_dict[name]["Round_2"]["Participates"]=round2_part
    rooms_dict[name]["Round_3"]["Participates"]=round3_part
    rooms_dict[name]["Round_4"]["Participates"]=round4_part
    rooms_dict[name]["Round_5"]["Participates"]=round5_part

    round1_ballot=rounds[0].split(""","ballot":""")
    round1_ballot=round1_ballot[1][:-1]
    round2_ballot=rounds[1].split(""","ballot":""")
    round2_ballot=round2_ballot[1][:-1]
    round3_ballot=rounds[2].split(""","ballot":""")
    round3_ballot=round3_ballot[1][:-1]
    round4_ballot=rounds[3].split(""","ballot":""")
    round4_ballot=round4_ballot[1][:-1]
    round5_ballot=rounds[4].split(""","ballot":""")
    round5_ballot=round5_ballot[1][:-1]

    rooms_dict[name]["Round_1"]["Ballot"]=round1_ballot
    rooms_dict[name]["Round_2"]["Ballot"]=round2_ballot
    rooms_dict[name]["Round_3"]["Ballot"]=round3_ballot
    rooms_dict[name]["Round_4"]["Ballot"]=round4_ballot
    rooms_dict[name]["Round_5"]["Ballot"]=round5_ballot

rooms=rooms_dict

#players
players_start=rooms_end
players_end=raw_string.find("""],"rounds":[{""")
players_string=raw_string[players_start+14:players_end]
players=players_string.split(",{")

players_dict={}

for item in players:
    name=item.split(""","id":""")
    name=name[0][8:-1]
    players_dict[name]={}

    player_id=item.split(""","id":""")
    player_id=player_id[1].split(""","team":""")
    player_id=player_id[0][1:-1]
    players_dict[name]["ID"]=player_id

    team=item.split(""","team":""")
    team=team[1].strip("}")
    players_dict[name]["Team"]=team

players=players_dict

#rounds

rounds_start=raw_string.find(""","rounds":[{"id":""")
rounds_end=raw_string.find(""","elimRounds":""")
rounds=raw_string[rounds_start:rounds_end].split("""{"id":"round_""")[1:]
rounds_dict={}

for item in rounds:
    round_id=item.split(""","tableOpts":""")[0][:-1]
    rounds_dict["round_"+round_id]={}

    rounds_ballots=item.split(""","ballots":[{""")[1].split("""],"ballotsPerMatch":""")[0].split(""","skillIndex":""")[:-1]

    for item in rounds_ballots:
        ballot_id=item.split(""","id":""")[1].split(""","votes":""")[0][1:-1]
        rounds_dict["round_"+round_id][ballot_id]={}
        rounds_dict["round_"+round_id][ballot_id]["Judges"]={}

        round_teams=item.split("""teams":[""")[1].split("""],"presence":""")[0].split(",")
        rounds_dict["round_"+round_id][ballot_id]["Teams"]=round_teams

        votes=item.split(""","votes":""")[1].split(""","judges":""")[0].split("""{"judge":""")[1:]

        judge1_id=votes[0].split(""","ballots":""")[0]
        rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge1_id]]={}

        ballots1_prop=votes[0].split(""","prop":""")[1].split(""","opp":""")[0]
        ballots1_opp=votes[0].split(""","opp":""")[1].split(""","scores":""")[0]
        rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge1_id]]["Ballots_Prop"]=ballots1_prop
        rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge1_id]]["Ballots_Opp"]=ballots1_opp

        scores1=votes[0].split(""","scores":[[""")[1].split("""]]}""")[0].split("],[")
        scores1_prop=scores1[0].split(",")
        scores1_opp=scores1[1].split(",")
        rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge1_id]]["Scores_Prop"]=scores1_prop
        rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge1_id]]["Scores_Opp"]=scores1_opp

        roles=item.split(""","roles":[[""")[1].split("""]]""")[0].split("""],[""")
        roles_prop=roles[0].split(",")
        roles_opp=roles[1].split(",")
        rounds_dict["round_"+round_id][ballot_id]["Roles_Prop"]=roles_prop
        rounds_dict["round_"+round_id][ballot_id]["Roles_Opp"]=roles_opp
        
        if len(votes)==3:
            judge2_id=votes[1].split(""","ballots":""")[0]
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge2_id]]={}

            ballots2_prop=votes[1].split(""","prop":""")[1].split(""","opp":""")[0]
            ballots2_opp=votes[1].split(""","opp":""")[1].split(""","scores":""")[0]
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge2_id]]["Ballots_Prop"]=ballots2_prop
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge2_id]]["Ballots_Opp"]=ballots2_opp

            scores2=votes[1].split(""","scores":[[""")[1].split("""]]}""")[0].split("],[")
            scores2_prop=scores2[0].split(",")
            scores2_opp=scores2[1].split(",")
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge2_id]]["Scores_Prop"]=scores2_prop
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge2_id]]["Scores_Opp"]=scores2_opp
            
            judge3_id=votes[2].split(""","ballots":""")[0]
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge3_id]]={}

            ballots3_prop=votes[2].split(""","prop":""")[1].split(""","opp":""")[0]
            ballots3_opp=votes[2].split(""","opp":""")[1].split(""","scores":""")[0]
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge3_id]]["Ballots_Prop"]=ballots3_prop
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge3_id]]["Ballots_Opp"]=ballots3_opp

            scores3=votes[2].split(""","scores":[[""")[1].split("""]]}""")[0].split("],[")
            scores3_prop=scores3[0].split(",")
            scores3_opp=scores3[1].split(",")
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge3_id]]["Scores_Prop"]=scores3_prop
            rounds_dict["round_"+round_id][ballot_id]["Judges"][match_judges()["judge_"+judge3_id]]["Scores_Opp"]=scores3_opp

rounds=rounds_dict

allplayers=list(players.keys())
allteams=list(teams.keys())

team_layout={}

for team in allteams:
    team_layout[team]={}
    team_layout[team]["Names"]=[]
    team_layout[team]["ID"]=[]

    for player in allplayers:
        if match_teams()[players[player]["Team"]]==team:
            team_layout[team]["Names"].append(player)

for team in team_layout:
    for player in team_layout[team]["Names"]:
        i=team_layout[team]["Names"].index(player)
        team_layout[team]["ID"].append(str(i))

for r in rounds:
    for b in rounds[r]:
        tmp_teams=rounds[r][b]["Teams"]
        rounds[r][b]["Teams"]=[match_teams()[rounds[r][b]["Teams"][0]], match_teams()[rounds[r][b]["Teams"][1]]]

for r in rounds:
    for b in rounds[r]:
        id_prop=rounds[r][b]["Roles_Prop"]
        id_opp=rounds[r][b]["Roles_Opp"]
        name_prop=[]
        name_opp=[]
        prop=rounds[r][b]["Teams"][0]
        opp=rounds[r][b]["Teams"][1]
        for p in id_prop:
            name_prop.append(team_layout[prop]["Names"][int(p)])
        for p in id_opp:
            name_opp.append(team_layout[opp]["Names"][int(p)])
        rounds[r][b]["Roles_Prop"]=name_prop
        rounds[r][b]["Roles_Opp"]=name_opp

speaks={}
for r in rounds:
    speaks[r]={}
    for b in rounds[r]:
        speaks[r][b]={}
        for j in rounds[r][b]["Judges"]:
            speaks[r][b][j]={}
            for p in rounds[r][b]["Roles_Prop"]:
                role=rounds[r][b]["Roles_Prop"].index(p)
                speaks[r][b][j][p]=rounds[r][b]["Judges"][j]["Scores_Prop"][role]
            for p in rounds[r][b]["Roles_Opp"]:
                role=rounds[r][b]["Roles_Opp"].index(p)
                speaks[r][b][j][p]=rounds[r][b]["Judges"][j]["Scores_Opp"][role]
            

pers_speaks={}
for r in speaks:
    for b in speaks[r]:
        for j in speaks[r][b]:
            for p in speaks[r][b][j]:
                pers_speaks[p]={}

for p in pers_speaks:
    for r in speaks:
        pers_speaks[p][r]=[]

for r in speaks:
    for b in speaks[r]:
        for j in speaks[r][b]:
            for p in speaks[r][b][j]:
                pers_speaks[p][r].append(speaks[r][b][j][p])

speaksbyround={}
for name in pers_speaks:  
    speaksbyround[name]={}
    for r in speaks:
        allspeaks=pers_speaks[name][r]
        intspeaks=[]
        for score in allspeaks:
            intspeaks.append(int(score))
        try:
            speaksbyround[name][r]=round(sum(intspeaks)/len(intspeaks),2)
        except:
            speaksbyround[name][r]=""

allspeaks={}
for name in pers_speaks:
    totalspeaks=[]
    for r in speaks:
        totalspeaks.append(speaksbyround[name][r])
    try:
        allspeaks[name]=round(sum(totalspeaks)/len(totalspeaks), 2)
    except:
        allspeaks[name]=""
            
    
teamballots={}
for name in teams:
    teamballots[name]={}
    for r in rounds:
        teamballots[name][r]=[]
        for b in rounds[r]:
            for j in rounds[r][b]["Judges"]:
                if name==rounds[r][b]["Teams"][0]:
                    teamballots[name][r].append(rounds[r][b]["Judges"][j]["Ballots_Prop"])
                if name==rounds[r][b]["Teams"][1]:
                    teamballots[name][r].append(rounds[r][b]["Judges"][j]["Ballots_Opp"])
            
speakerjudges={}
for name in players:
    speakerjudges[name]={}
    for r in rounds:
        speakerjudges[name][r]=[]
        for b in rounds[r]:
            for j in rounds[r][b]["Judges"]:
                if name in rounds[r][b]["Roles_Prop"] or name in rounds[r][b]["Roles_Opp"]:
                    speakerjudges[name][r].append(j)

teamwins={}
for name in teams:
    teamwins[name]={}
    for r in rounds:
        ballots=teamballots[name][r]
        newballots=[]
        for b in ballots:
            newballots.append(int(b))
        if sum(newballots)>=2:
            teamwins[name][r]="1"
        else:
            teamwins[name][r]="0"

totalwins={}
for name in teams:
    wins=[]
    for r in rounds:
        for w in teamwins[name][r]:
            wins.append(int(w))
    totalwins[name]=sum(wins)

teamjudges={}
for name in judges:
    teamjudges[name]={}
    for r in rounds:
        teamjudges[name][r]=[]
        for b in rounds[r]:
            if name in list(rounds[r][b]["Judges"].keys()):
                teamjudges[name][r]=rounds[r][b]["Teams"]

opponents={}
for team in teams:
    opponents[team]={}
    for r in rounds:
        for b in rounds[r]:
            if rounds[r][b]["Teams"][0]==team:
                opponents[team][r]=rounds[r][b]["Teams"][1]
            elif rounds[r][b]["Teams"][1]==team:
                opponents[team][r]=rounds[r][b]["Teams"][0]
            
        

outf=filedialog.asksaveasfilename(initialdir = "/",title = "Vali asukoht",filetypes = (("csv fail","*.csv"),("kõik failid","*.*")))               

speaker_header=("SPEAKER;TEAM;SCHOOL;TOTALAVG;R1AVG;R2AVG;R3AVG;R4AVG;R5AVG;R1J1;R1J2;R1J3;R2J1;R2J2;R2J3;R3J1;R3J2;R3J3;R4J1;R4J2;R4J3;R5J1;R5J2;R5J3;R1J;R2J;R3J;R4J;R5J\n")
team_header=("TEAM;TOTAL;R1;R2;R3;R4;R4;R1J1;R1J2;R1J3;R2J1;R2J2;R2J3;R3J1;R3J2;R3J3;R4J1;R4J2;R4J3;R5J1;R5J2;R5J3;R1VS;R2VS;R3VS;R4VS;R5VS\n")
judge_header=("JUDGE;R1P;R1O;R2P;R20;R3P;R3O;R4P;R4O;R5P;R5O\n")

if outf[-4:]!=".csv":
    outf=outf+".csv"

f=open(outf, "w", encoding="UTF-8")

#speakers
c=0
f.write("#;")
f.write(speaker_header)
for speaker in players:
    #id
    f.write(str(c)+";")
    
    #name
    f.write(speaker+";")

    #team
    try:
        f.write(match_teams()[players[speaker]["Team"]]+";")
    except:
        f.write(";")

    #school
    try:
        f.write(match_clubs()[players[speaker]["Team"]]+";")
    except:
        f.write(";")

    #total
    try:
        f.write(str(allspeaks[speaker])+";")
    except:
        f.write(";")

    #round1
    r=list(rounds.keys())[0]
    try:
        f.write(str(speaksbyround[speaker][r])+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][2]+";")
    except:
        f.write(";")

    #round2
    r=list(rounds.keys())[1]
    try:
        f.write(str(speaksbyround[speaker][r])+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][2]+";")
    except:
        f.write(";")

    #round3
    r=list(rounds.keys())[2]
    try:
        f.write(str(speaksbyround[speaker][r])+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][2]+";")
    except:
        f.write(";")

    #round4
    r=list(rounds.keys())[3]
    try:
        f.write(str(speaksbyround[speaker][r])+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][2]+";")
    except:
        f.write(";")

    #round5
    r=list(rounds.keys())[4]
    try:
        f.write(str(speaksbyround[speaker][r])+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(pers_speaks[speaker][r][2]+";")
    except:
        f.write(";")

    #judges
    roundids=list(rounds.keys())
    f.write(str(speakerjudges[speaker][roundids[0]])+";")
    f.write(str(speakerjudges[speaker][roundids[1]])+";")
    f.write(str(speakerjudges[speaker][roundids[2]])+";")
    f.write(str(speakerjudges[speaker][roundids[3]])+";")
    f.write(str(speakerjudges[speaker][roundids[4]])+";")

    #newline
    f.write("\n")

    c+=1

#teams
f.write("#;")
f.write(team_header)

c=0
for team in teams:
    #id
    f.write(str(c)+";")
    
    #name
    f.write(team+";")

    #total
    f.write(str(totalwins[team])+";")

    #wins
    roundids=list(rounds.keys())
    f.write(teamwins[team][roundids[0]]+";")
    f.write(teamwins[team][roundids[1]]+";")
    f.write(teamwins[team][roundids[2]]+";")
    f.write(teamwins[team][roundids[3]]+";")
    f.write(teamwins[team][roundids[4]]+";")

    #round1
    r=list(rounds.keys())[0]

    try:
        f.write(teamballots[team][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][2]+";")
    except:
        f.write(";")

    #round2
    r=list(rounds.keys())[1]

    try:
        f.write(teamballots[team][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][2]+";")
    except:
        f.write(";")

    #round3
    r=list(rounds.keys())[2]

    try:
        f.write(teamballots[team][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][2]+";")
    except:
        f.write(";")

    #round4
    r=list(rounds.keys())[3]

    try:
        f.write(teamballots[team][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][2]+";")
    except:
        f.write(";")

    #round5
    r=list(rounds.keys())[4]

    try:
        f.write(teamballots[team][r][0]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][1]+";")
    except:
        f.write(";")
    try:
        f.write(teamballots[team][r][2]+";")
    except:
        f.write(";")

    #opponents
    roundids=list(rounds.keys())
    try:
        f.write(opponents[team][roundids[0]]+";")
    except:
        f.write(";")
    try:
        f.write(opponents[team][roundids[1]]+";")
    except:
        f.write(";")
    try:
        f.write(opponents[team][roundids[2]]+";")
    except:
        f.write(";")
    try:
        f.write(opponents[team][roundids[3]]+";")
    except:
        f.write(";")
    try:
        f.write(opponents[team][roundids[4]]+";")
    except:
        f.write(";")

    #newline
    f.write("\n")

    c+=1

#judges
f.write("#;")
f.write(judge_header)
c=0

for judge in teamjudges:
    #id
    f.write(str(c)+";")
    f.write(judge+";")

    for r in rounds:
        try:
            f.write(teamjudges[judge][r][0]+";")
            f.write(teamjudges[judge][r][1]+";")
        except:
            f.write(";;")

    #newline
    f.write("\n")

    c+=1

f.close()

root.destroy()
root.mainloop()
