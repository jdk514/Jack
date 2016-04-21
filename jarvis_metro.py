import httplib, urllib, base64, json
import settings
import jarvis_tts as jtts
from datetime import datetime
import time

import pdb

headers = {
            # Request headers
            #Load API Key from settings
            'api_key': os.environ['WMATA_API_KEY'],
        }

#Load default location from settings
def_loc = os.environ['default_location']

#Train object to store train arrivals at a station
class Train:
    cars = ""
    destination = ""
    destination_code = ""
    destination_name = ""
    group = ""
    line = ""
    location_code = ""
    location_name = ""
    arrival = ""

    def __init__(self, train):
        self.cars = train['Car']
        self.destination = train['Destination']
        self.destination_code = train['DestinationCode']
        self.destination_name = train['DestinationName']
        self.group = train['Group']
        self.line = train['Line']
        self.location_code = train['LocationCode']
        self.location_name = train['LocationName']
        self.arrival = train['Min']

    def __repr__(self):
        return "%s, %s - arriving in %s minutes" % (self.destination, self.line, self.arrival)

#Function that returns a dictionary linking station name to station code
def get_stations():
    station_dict = {}
    try:
        conn = httplib.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/Rail.svc/json/jStations", "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        json_data = json.loads(data)
        for station in json_data['Stations']:
            station_dict[station['Name']] = station['Code']
        conn.close()
        return (station_dict)
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

#Function retrieves the trains at a given station, destination, and line
def get_trains(location, destination, line):
    station_code = get_stations()[location]
    try:
        conn = httplib.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/StationPrediction.svc/json/GetPrediction/%s" % station_code, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        json_data = json.loads(data)
        trains = []
        for train in json_data['Trains']:
            curr_train = Train(train)
            if curr_train.line == line and curr_train.destination == destination:
                trains.append(curr_train)
        conn.close()
        return (trains)
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

#Function codifies the results of the predicition api call
def get_train_text(location, destination, line):
    trains = get_trains(location, destination, line)
    train_text = []
    for train in trains:
        train_text.append(train.__repr__())

    if len(train_text) == 0:
        train_text = ["No Trains Currently On The Board"]
    return (train_text)

#NON FUNCTIONING
def get_train(station):
    station_dict = get_stations()
    station_code = station_dict[station]
    trains = get_trains(station_code)

#Function processes metro based commands
def process_command(command):
    #Get the next metro - currently supports default location only
    if "next metro" in command:
        jtts.jarvis_tts(get_train_text(def_loc["station"], def_loc["destination"], def_loc["color"]))


if __name__ == "__main__":
    trains = get_trains('Pentagon City', 'Largo', 'BL')
    this = "hello"
    print(this)
