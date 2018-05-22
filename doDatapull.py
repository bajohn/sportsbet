import requests
import xml.etree.ElementTree as ET
# from xml.dom.minidom import parse, parseString
from dbmodify import DBInteract
from helpers_datapull import DataPuller
from staticDefs import eventValues

dbInteractor = DBInteract()
dataPuller = DataPuller()

baseUrl ='http://gd2.mlb.com/components/game/mlb/year_'
year = 2017

debug = True
debugComplete = False

eventList = []
# iterate through months
for month in range(4,12): 
    # iterate through days
    for day in range(1, dataPuller.getDaysOfMonth(month, year)):
        if not debugComplete:
            curUrl = dataPuller.getDateUrl(baseUrl, day, month, year)
            retVal = requests.get(curUrl)

            # print(retVal.status_code)
            retText = retVal.text
            if 'gid' in retText:
                # gids like /gid_2017_04_01_anamlb_lanmlb_1/' taht attach to urls

                gids = dataPuller.getGameIds(retText)
               
                for gid in gids:
                    dataPuller.sendPitchersToDb(curUrl, gid)
                #     inningUrl = curUrl + gid + 'inning/inning_all.xml'
                #     retText = requests.get(inningUrl).text
                #     tree = ET.fromstring(retText)
                #     for atbat in tree.iter('atbat'):
                #         abStats = dataPuller.getAtBatStats(atbat)
                #         print(abStats)
                #         #todo: how many are getting dropped?
                #         if not abStats == 'empty':
                #             abEvent = abStats['event']
                #             if abEvent not in eventValues:
                #                 raise 'Event not found: ' + abEvent
                #             dbInteractor.insertMatchup(abStats)

                #             for pitch in atbat.iter('pitch'):
                #                 pitchStats = dataPuller.getPitchStats(pitch)
                #                 if not pitchStats == 'empty':
                #                     dbInteractor.insertPitch(abStats, pitchStats)

        if debug:
            debugComplete = True

print('done: ', eventList)
# print(tree.get('away_team'))