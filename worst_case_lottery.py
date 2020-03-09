from helpers.lottery_helper import *

def pretty_print(json_str):
    print(json.dumps(json_str, indent=4, sort_keys=True))
    return(json.dumps(json_str, indent=4, sort_keys=True))

def get_standings(response):
    divisions = response["records"]
    teams = {}

    for i in divisions:
        for j in range(len(i['teamRecords'])):
            teams[i['teamRecords'][j]['team']['name']] = int(i['teamRecords'][j]['leagueRank'])
    return teams
    
def get_odds(position_in_standings):
    return LOTTERY_ODDS[position_in_standings]

def worst_case_lottery():
    url = "https://statsapi.web.nhl.com/api/v1/standings"

    response = requests.get(url).json()
    standings = get_standings(response)

    sens_position = standings["Ottawa Senators"]
    sharks_position = standings["San Jose Sharks"]

    odds = get_odds(sens_position) + get_odds(sharks_position)

    message = 'The odds that the Ottawa Senators pick first overall today are: {}%\n'.format(odds)
    message = message + 'The worst case scenario for 2020 draft position is {} and {}'.format(35 - sens_position, 35 - sharks_position)
    return message

# if __name__ == "__main__":
#     message = worst_case_lottery()
#     print(message)
    # url = "https://statsapi.web.nhl.com/api/v1/standings"

    # response = requests.get(url).json()
    # standings = get_standings(response)

    # sens_position = standings["Ottawa Senators"]
    # sharks_position = standings["San Jose Sharks"]

    # odds = get_odds(sens_position) + get_odds(sharks_position)

    # print('The odds that the Ottawa Senators pick first overall today are: {}%'.format(odds))
    # print('The worst case scenario for 2020 draft position is {} and {}'.format(35 - sens_position, 35 - sharks_position))