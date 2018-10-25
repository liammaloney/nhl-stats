import json
import requests

ids = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,52,53,54]

def get_player_stats(id):
    url = 'https://statsapi.web.nhl.com/api/v1/people/'+str(id)+'/stats?stats=gameLog&season=20182019'

    response = requests.get(url).json()
    games = response['stats'][0]['splits']

    goals = 0
    assists = 0

    for i in games:
        goals = goals + i['stat']['goals']
        assists = assists + i['stat']['assists']
        # print(type(i['stat']['assists']))

    print('Goals: ' + str(goals))
    print('Assists: ' + str(assists))
    print('Points: ' + str(goals + assists))

def get_player_id(name):
    for i in ids:
        url = 'https://statsapi.web.nhl.com/api/v1/teams/'+str(i)+'/roster'
        response = requests.get(url).json()
        roster = response['roster']   
        # print(roster)  
        for j in roster:
            # print(j['person']['fullName'])
            if j['person']['fullName']==name:
                id=j['person']['id']
                break
    return(id)

print('Enter capitalized full name of an NHL player')
name = input()
player_id = get_player_id(name)
print(name+'\'s Statistics')
get_player_stats(player_id)