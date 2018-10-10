from urllib.request import Request, urlopen
import re
import ast
from pymongo import MongoClient
import datetime
import threading

def get_stations():
    req = Request("https://slovnaftbajk.sk/mapa-stanic", headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read().decode('utf-8')
    markers = re.findall(r"gMap.markerData[^}]*({[^}]*});", page)
    stations = {}
    for m in markers:
        station = ast.literal_eval(m)
        stations[station['station_nr']] = station
    return stations

def write_stations_to_db():
    threading.Timer(60.0, write_stations_to_db).start()
    current_status = {"stations": get_stations(),
          "timestamp": datetime.datetime.utcnow()}
    status.insert_one(current_status)

client = MongoClient()
db = client.slovnaftbajk
status = db.status
write_stations_to_db()
