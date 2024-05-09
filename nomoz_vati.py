import requests
from pprint import pprint as print


def namoz_time(txt):
    url = f"https://islomapi.uz/api/present/day?region={txt}"
    response = requests.get(url)
    # print(response.json())
    if 'error' in response:
        return False
    prabel = '  '
    output = {}
    times_j = response.json()["times"]
    times = []
    for time in times_j.items():
        # print(time)
        times.append(f"{prabel}{time[0]} : {time[1]}")
    output["times"] = "\n".join(times)
    output['weekday'] = response.json()['weekday']
    output['date'] = response.json()['date']
    output['region'] = response.json()['region']
    # print(output)
    return output



