import requests
import json

class mirror():

    def __init__(self):
        with open('api.json') as data:
            data = json.load(data)
            key = data['key']
            coord = data['coord']
        self.weatherURL = 'https://api.darksky.net/forecast/' + key + '/' + coord

    # update the weather
    def updateWeather(self):
        r = requests.get(self.weatherURL)
        data = r.json()
        todaySummary = data['currently']['summary']
        dailySummary = data['daily']['summary']
        return dailySummary, todaySummary
        print('TODAY:   {}'.format(todaySummary))
        print('DAILY:   {}'.format(dailySummary))


if __name__ == '__main__':
    m = mirror()
    d,t = m.updateWeather()
    print(d, t)
