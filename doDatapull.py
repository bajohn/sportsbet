import requests
import xml.etree.ElementTree as ET
# from xml.dom.minidom import parse, parseString
from dbmodify import DBInteract
from helpers_datapull import DataPuller
from staticDefs import eventValues

dbInteractor = DBInteract()
dataPuller = DataPuller()



debug = True
debugComplete = False

eventList = []

pitcherIterParams = {
    'cb': dataPuller.sendPitcherToDb
}

dataPuller.pitcherIter(pitcherIterParams)





                    
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



print('done: ', eventList)
# print(tree.get('away_team'))