raw=open("tab.atab", encoding="UTF-8")
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
    
        


    

    


