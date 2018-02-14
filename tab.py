raw=open("tab.atab", encoding="UTF-8")
raw_string=str(raw.readlines())

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

def output():
    f=open("output.csv", "w")
    f.write("Team Name;Team ID;P1;P2;P3;P4;P5;R1 ID;R2 ID;R3 ID;R4 ID;R5 ID;R1 Participates;R2 Participates;R3 Participates;R4 Participates;R5 Participates;R1 Room Strenght;R2 Room Strenght;R3 Room Strenght;R4 Room Strenght;R5 Room Strenght\n")
    for key in teams:
        f.write(key+";")
        f.write(teams[key]["ID"]+";")
        try:
            f.write(teams[key]["Players"][0]+";")
        except:
            f.write(";")
        try:
            f.write(teams[key]["Players"][1]+";")
        except:
            f.write(";")
        try:
            f.write(teams[key]["Players"][2]+";")
        except:
            f.write(";")
        try:
            f.write(teams[key]["Players"][3]+";")
        except:
            f.write(";")
        try:
            f.write(teams[key]["Players"][4]+";")
        except:
            f.write(";")
        f.write(teams[key]["Round_1"]["ID"]+";")
        f.write(teams[key]["Round_2"]["ID"]+";")
        f.write(teams[key]["Round_3"]["ID"]+";")
        f.write(teams[key]["Round_4"]["ID"]+";")
        f.write(teams[key]["Round_5"]["ID"]+";")
        f.write(teams[key]["Round_1"]["Participates"]+";")
        f.write(teams[key]["Round_2"]["Participates"]+";")
        f.write(teams[key]["Round_3"]["Participates"]+";")
        f.write(teams[key]["Round_4"]["Participates"]+";")
        f.write(teams[key]["Round_5"]["Participates"]+";")
        f.write(teams[key]["Round_1"]["Ballot"]+";")
        f.write(teams[key]["Round_2"]["Ballot"]+";")
        f.write(teams[key]["Round_3"]["Ballot"]+";")
        f.write(teams[key]["Round_4"]["Ballot"]+";")
        f.write(teams[key]["Round_5"]["Ballot"])
        
        f.write("\n")
            
    f.close()
    
        


    

    


