import requests
import json
import matplotlib.pyplot as plt
import time
import os
import twilio

class mirror():

    def __init__(self):
        with open('api.json') as data:
            creds = json.load(data)
            key = creds['key']
            coord = creds['coord']
            self.weatherURL = 'https://api.darksky.net/forecast/' + key + '/' + coord
            self.times = []
            self.temps = ['temperature', []]
            self.precip = ['preicp', []]
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
                self.temps[1].append(element['temperature'])
                self.precip[1].append(element['precipProbability'])
            if j > 10:
                j = 0
        for element in [self.precip, self.temps]:

            if (element[0] == 'precip' and np.mean(element[1]) > .05) or element[0] == 'temperature':

                # all of the plot attributes
                plt.style.use('dark_background')
                plt.rcParams['savefig.facecolor'] = 'black'

                # all of the plot attributes
                plt.style.use('dark_background')
                plt.rcParams['axes.facecolor'] = 'black'
                plt.rcParams['savefig.facecolor'] = 'black'

                # Plot the data and set the labels.
                plt.xticks(color='black')
                plt.bar(self.times, element[1], color='w')
                plt.ylabel(ylabel = '', size=30)
                plt.tick_params(axis='both', which='major', labelsize=20)
                plt.savefig(('templates/' + element[0] + '.png'), dpi = 1800)
                plt.close()

if __name__ == '__main__':
    m = mirror()
    m.updateForecasts()
