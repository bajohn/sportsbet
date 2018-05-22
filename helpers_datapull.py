import requests
# helper functions
class DataPuller():
    
    def padDateEl(self, dateEl):
        # pad with leading 0 
        if dateEl < 10:
            return '0' + str(dateEl)
        else:
            return str(dateEl)
        

    def getDaysOfMonth(self, month, year):
        if month in [1,3,5,7,8,10,12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if year % 4 == 0:
                return 29
            else:
                return 28
        else:
            raise Exception('Invalid month ' + month)

    def getDateUrl(self, baseUrl, day, month, year):

        monthStr = '/month_' + self.padDateEl(month)
        dayStr = '/day_' + self.padDateEl(day)
        return baseUrl + str(year)  + monthStr + dayStr
        
    def getGameIds(self, retTxt):
        retSplit = retTxt.split('gid_')
        retArr = []
        for idx in range(1, len(retSplit)):
            endIdx = retSplit[idx].index('/') + 1
            gid = '/gid_' + retSplit[idx][:endIdx]
            retArr.append(gid)
        return retArr

    def sendPitchersToDb(self, url,  gid):
        curUrl = url + gid + 'pitchers/'
        retVal = requests.get(curUrl)
        print(curUrl, retVal)

    # todo: for these stats, pare down by only pulling stats that are needed
    # also, check ratio of events that are missing some stats, any patterns here could throw
    # things off.
    def getPitchStats(self, pitch):
        retObj = {}
        # full list 
        pitchStatList =['des', 'des_es', 'id', 'type', 'tfs', 'tfs_zulu', 'x', 'y', 'event_num', 'sv_id', 'play_guid', 'start_speed', 'end_speed', 'sz_top', 'sz_bot', 'pfx_x', 'pfx_z', 'px', 'pz', 'x0', 'y0', 'z0', 'vx0', 'vy0', 'vz0', 'ax', 'ay', 'az', 'break_y', 'break_angle', 'break_length', 'pitch_type', 'type_confidence', 'zone', 'nasty', 'spin_dir', 'spin_rate', 'cc', 'mt']

        # list of stats actually used:
        # pitchStatList =['id', 'type', 'pitch_type','start_speed', 'end_speed',  'x0', 'y0', 'z0','px', 'pz','pfx_x', 'pfx_z', 'ax', 'ay', 'az',  'vx0', 'vy0', 'vz0', 'break_y', 'break_angle', 'break_length', 'spin_dir', 'spin_rate',  'play_guid']

        for stat in pitchStatList:
            if stat not in pitch.keys():
                return 'empty'
            else:
                retObj[stat] = pitch.get(stat)

        return retObj
        
        
    def getAtBatStats(self, atbat): 
        abStatList = [ 'batter','pitcher', 'p_throws', 'event', 'play_guid', ]
        retObj = {}
        for stat in abStatList:
            if stat not in atbat.keys():
                return 'empty'
            else:
                retObj[stat] = atbat.get(stat)     
        return retObj

    def printTreeStats(self, statIn):
        print(statIn.keys())