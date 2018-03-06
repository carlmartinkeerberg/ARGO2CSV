import json

def extract(inf):
    global tournament_name, teams, speakers
    #Import json dictionary from .atab to python
    tab=json.load(open(inf, encoding="UTF-8"))

    #Extract tournament title
    tournament_name=tab["title"]

    #Extract sub-dictionaries of tab: teams, judges, players, rounds
    teams_raw=tab["v1"]["teams"]
    judges_raw=tab["v1"]["judges"]
    players_raw=tab["v1"]["players"]
    rounds_raw=tab["v1"]["rounds"]

    #team names and speakers
    teams={}
    for t in teams_raw:
        teams[t["name"]]={}
        players=t["players"]
        speakers=[]
        for p in players:
            speakers.append(players_raw[p]["name"])
        teams[t["name"]]["speakers"]=speakers

    #team ballots and judges
    for r in rounds_raw:
        r_id=rounds_raw.index(r)
        for b in r["ballots"]:
            if b["teams"][0]!=-1:
                prop_team=teams_raw[b["teams"][0]]["name"]
            if b["teams"][1]!=-1:
                opp_team=teams_raw[b["teams"][1]]["name"]
            teams[prop_team][r_id+1]={}
            teams[opp_team][r_id+1]={}
            for v in b["votes"]:
                judge=judges_raw[v["judge"]]["name"]
                prop_ballots=v["prop"]
                opp_ballots=v["opp"]
                teams[prop_team][r_id+1][judge]=prop_ballots
                teams[opp_team][r_id+1][judge]=opp_ballots

    #speaker names and teams
    speakers={}
    for p in players_raw:
        speakers[p["name"]]={}
        if p["team"]!=-1:
            speakers[p["name"]]["team"]=teams_raw[p["team"]]["name"]

    #speaker scores and judges
    for r in rounds_raw:
        r_id=rounds_raw.index(r)
        for b in r["ballots"]:
            prop_team=teams_raw[b["teams"][0]]["name"]
            opp_team=teams_raw[b["teams"][1]]["name"]
            prop_speakers=teams[prop_team]["speakers"]
            opp_speakers=teams[opp_team]["speakers"]
            for s in prop_speakers:
                speakers[s][r_id+1]={}
            for s in opp_speakers:
                speakers[s][r_id+1]={}
            prop_roles=b["roles"][0][:-1]
            opp_roles=b["roles"][1][:-1]
            for v in b["votes"]:
                judge=judges_raw[v["judge"]]["name"]
                prop_scores=v["scores"][0][:-1]
                opp_scores=v["scores"][1][:-1]
                for s in prop_roles:
                    s_index=prop_roles.index(s)
                    speaker=prop_speakers[s]
                    score=prop_scores[s_index]
                    speakers[speaker][r_id+1][judge]=score
                for s in opp_roles:
                    s_index=opp_roles.index(s)
                    speaker=opp_speakers[s]
                    score=opp_scores[s_index]
                    speakers[speaker][r_id+1][judge]=score

def output(outf):
    #output
    f=open(outf, "w", encoding="UTF-8")

    #header
    f.write(tournament_name+"\n")
    f.write("Speaker;Team;R1_1S;R1_2S;R1_3S;R2_1S;R2_2S;R2_3S;R3_1S;R3_2S;R3_3S;R4_1S;R4_2S;R4_3S;R5_1S;R5_2S;R5_3S;R1_1J;R1_2J;R1_3J;R2_1J;R2_2J;R2_3J;R3_1J;R3_2J;R3_3J;R4_1J;R4_2J;R4_3J;R5_1J;R5_2J;R5_3J;R1_1B;R1_2B;R1_3B;R2_1B;R2_2B;R2_3B;R3_1B;R3_2B;R3_3B;R4_1B;R4_2B;R4_3B;R5_1B;R5_2B;R5_3B\n")

    #speaker name, team
    for s in speakers:
        f.write(s+";")
        try:
            f.write(speakers[s]["team"]+";")
        except:
            f.write(";")

    #scores
        for r in range(5):
            try:
                judges=list(speakers[s][r+1].keys())
            except:
                pass
            for j in range(3):
                try:
                    f.write(str(speakers[s][r+1][judges[j]])+";")
                except:
                    f.write(";")

    #judges
        for r in range(5):
            try:
                judges=list(speakers[s][r+1].keys())
            except:
                pass
            for j in range(3):
                try:
                    f.write(judges[j]+";")
                except:
                    f.write(";")

    #ballots
        for r in range(5):
            try:
                judges=list(speakers[s][r+1].keys())
            except:
                pass
            for j in range(3):
                try:
                    team_name=speakers[s]["team"]
                    judges=list(teams[team_name][r+1].keys())
                    f.write(str(teams[team_name][r+1][judges[j]])+";")
                except:
                    f.write(";")
            
        f.write("\n")

    f.close()
