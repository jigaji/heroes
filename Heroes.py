import requests

url = 'https://superheroapi.com/api/2619421814940190/search/'
heroes = ['Hulk', 'Captain America', 'Thanos']


def the_smartest():
    intel = {}
    for hero in heroes:
        hero_r = requests.get(url + hero)
        response = int(hero_r.json()['results'][0]['powerstats']['intelligence'])
        intel[hero] = response
    smart = max(intel.items(), key=lambda x: x[1])
    return f'Самый умный из героев - {smart[0]} (не зря у него перчатка бесконечности)'
print(the_smartest())