wc_teams=["India","Bangladesh","Australia","England","Pakistan","Newzeland"]
wc_wins=[2,0,5,1,0,1]

print(type(wc_teams),wc_teams)

wc_teams.append("Srilanka")
wc_teams[4]="Scotland"
print(wc_teams)
wc_teams.insert(2,"West Indies")
print(wc_teams)
wc_teams.extend(["USA","Nepal"])
print(wc_teams)

wc_teams.sort()
print("ascending order : ",wc_teams)
teams=":".join(wc_teams)  #converting list into a string
print(teams)

print(" No. of teams participating in wc: ",len(wc_teams))
print("4th team in wc : ",wc_teams[3])
print("last team in wc : ", wc_teams[-1])
print("Teams who listed from 3rd to last : ",wc_teams[3:])

i_players = ["Rohit","Virat","Rahul","Hardik"]
a_players = ["Pat","Starc","Wanner","Stoinis"]
t_squad = [i_players,a_players]
print(t_squad)

print(wc_teams.pop())
print(wc_teams)
wc_teams.remove("England")
print(wc_teams)

list1=[0,1,2,3,4,5]
list1[1]=3
print(list1)
















