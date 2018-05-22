from dbconnect import DB
from staticDefs import eventValues

class DBInteract:

    def __init__(self):
        # self._conn = sqlEngine.connect()
        print('init')
        self.DB = DB()

    def testInsert(self):
        # dml pylint error appears to be false positive
        batter = self.DB.Batter(**{'id': '2', 'batter_name': 'Merge Jones'})
        self.DB.session.merge(batter)
        self.DB.session.commit()


    def insertMatchup(self, abStats):
        matchup = self.DB.Matchup( id = abStats['play_guid'], 
            batter_id = abStats['batter'], 
            pitcher_id = abStats['pitcher'], 
            outcome = abStats['event'], 
            outcomeVal = eventValues[abStats['event']])
        self.DB.session.add(matchup)
        self.DB.session.commit()
 
    def insertBatter(self, batterStats):
        batter = self.DB.Batter( id = batterStats['batter'], 
            batter_name = batterStats['name'])
        self.DB.session.add(matchup)
        self.DB.session.commit()
 
    def insertPitch(self, abStats, pitchStats):
        # print(pitchStats)
        valsToInsert = {}

        for column in columns:
            # each column looks like 'pitch.pitch_type'
            curKey = str(column).split('.')[1]
            # todo: change to start_speed

            if curKey == 'p_throws':
                valsToInsert[curKey] = abStats[curKey]
            elif curKey == 'id': 
                valsToInsert[curKey] = pitchStats['play_guid'] + pitchStats[curKey]
            else:
                valsToInsert[curKey] = pitchStats[curKey]

        self.DB.session.add(**valsToInsert)
        self.DB.session.commit()



