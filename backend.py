# gets the data from the website
import requests


def connect():
    html_code = requests.get("https://www.worldometers.info/coronavirus/").text[:100001]
    html_code_line = html_code.split('\n')
    return html_code_line


class global_data:
    def __init__(self, code):
        self.code = code

    def cases(self):
        cases_ = self.code[self.code.index('<h1>Coronavirus Cases:</h1>') + 2]
        cases_ = cases_.replace('<span style="color:#aaa">', '')
        cases_ = cases_.replace('</span>', '')
        return cases_

    def deaths(self):
        deaths_ = self.code[self.code.index('<h1>Deaths:</h1>') + 2]
        deaths_ = deaths_.replace('<span>', '')
        deaths_ = deaths_.replace('</span>', '')
        return deaths_

    def recoveries(self):
        location_recoveries = requests.get("https://www.worldometers.info/coronavirus/").text[:100001].split('\n').index('<h1>Recovered:</h1>')
        recoveries_ = requests.get("https://www.worldometers.info/coronavirus/").text[:100001].split('\n')[location_recoveries + 2]
        recoveries_ = recoveries_.replace('<span>', '')
        recoveries_ = recoveries_.replace('</span>', '')
        return recoveries_


def data_return():
    connected = global_data(connect())
    return connected.cases(), connected.deaths(), connected.recoveries()