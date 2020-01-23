import json
import requests
import os
import timeit

ids = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,52,53,54]
def get_player_stats(id):
    url = 'https://statsapi.web.nhl.com/api/v1/people/'+str(id)+'/stats?stats=gameLog&season=20192020'

    response = requests.get(url).json()
    games = response['stats'][0]['splits']

    games_played = 0
    goals = 0
    assists = 0

    for i in games:
        games_played = games_played+1
        goals = goals + i['stat']['goals']
        assists = assists + i['stat']['assists']
        # print(type(i['stat']['assists']))

    print('Games Played:  ' + str(games_played))
    print('Goals:         ' + str(goals))
    print('Assists:       ' + str(assists))
    print('Points:        ' + str(goals + assists))
    print('P/GP           ' + str(round(((goals + assists)/games_played),2)))

def get_player_id(name):
    flag = 0
    count = len(ids)
    while(flag == 0 and count!=0):
        count = count - 1
        id = ids[count]
        url = 'https://statsapi.web.nhl.com/api/v1/teams/'+str(id)+'/roster'
        response = requests.get(url).json()
        roster = response['roster']  
        rcount = len(roster)
        while(flag == 0 and rcount!=0):
            rcount = rcount - 1
            if roster[rcount]['person']['fullName'].lower()==name.lower():
                player_id = roster[rcount]['person']['id']
                flag = 1
    if 'id' in locals():
        return(player_id)
    else:
        print('Player not found')

print('Enter full name of an NHL player')
name = input()
os.system('clear')
player_id = get_player_id(name)

if player_id!=None:
    print(name+'\'s Statistics')
    get_player_stats(player_id)