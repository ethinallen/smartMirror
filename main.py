import requests
import json
import matplotlib.pyplot as plt
import time
import os


class mirror():

    def __init__(self):
        with open('api.json') as data:
            creds = json.load(data)
            key = creds['key']
            coord = creds['coord']
            self.weatherURL = 'https://api.darksky.net/forecast/' + key + '/' + coord
            self.times = []
            self.temps = []
            self.precip = []
            self.xlabels = []
            self.sun = None

    # update the weather
    def updateForecasts(self):
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            if f == 'weiners.png':
                os.remove(f)
        r = requests.get(self.weatherURL)
        data = r.json()
        # for key in data['daily']:
        #     print(key)
        data = data['hourly']['data']


        i = 0
        j = 0

        # only saves values within a certain time frames
        for index, element in enumerate(data):
            if index < .24 * (len(data)):
                if j == 5:
                    self.xlabels.append(time.strftime('%m-%d %H:%M', time.localtime(element['time'])))
                self.times.append(time.strftime('%m-%d %H:%M', time.localtime(element['time'])))
                self.temps.append(element['temperature'])
                self.precip.append(element['precipProbability'])
            if j > 10:
                j = 0

        # all of the plot attributes
        plt.style.use('dark_background')
        plt.rcParams['axes.facecolor'] = 'black'
        plt.rcParams['savefig.facecolor'] = 'black'

        # Plot the data and set the labels.
        plt.xticks(color='black')
        plt.bar(self.times, self.temps, color='w')
        plt.ylabel('TEMP')
        plt.savefig('templates/weiners.png', dpi = 1800)

if __name__ == '__main__':
    # print('hello')
    m = mirror()
    m.updateForecasts()
