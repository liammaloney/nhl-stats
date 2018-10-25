import json
import requests
url = 'https://statsapi.web.nhl.com/api/v1/people/8475913/stats?stats=gameLog&season=20182019'

response = requests.get(url).json()
games = response['stats'][0]['splits']

goals = 0
assists = 0

for i in games:
    goals = goals + i['stat']['goals']
    assists = assists + i['stat']['assists']
    # print(type(i['stat']['assists']))

print('Mark Stone\'s Statistics:')
print('Goals: ' + str(goals))
print('Assists: ' + str(assists))
print('Points: ' + str(goals + assists))