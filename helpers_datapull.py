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
        print(curUrl) #, retVal.text)

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

    # dateUrl: string like http://gd2.mlb.com/components/game/mlb/year_2017/month_04/day_04/ 
    # iterate with cbFunc(text) for each url
    def getPitchers(self):

        def pitcherCb(curUrl):
            print(curUrl)
            # curUrl = dataPuller.getDateUrl(baseUrl, day, month, year)
            # retVal = requests.get(curUrl)

            # # print(retVal.status_code)
            # retText = retVal.text
            # if 'gid' in retText:
            # # gids like /gid_2017_04_01_anamlb_lanmlb_1/' that attach to urls

            # gids = dataPuller.getGameIds(retText)

            # for gid in gids:
            # dataPuller.sendPitchersToDb(curUrl, gid)
        iterParams = {
            'startYear': 2017,
            'endYear': 2017,
            'cb': pitcherCb,
            'debug': True
        }
        self.dayIter(iterParams)

    # feed cbFunc with dateUrls, like http://gd2.mlb.com/components/game/mlb/year_2017/month_04/day_04/ 
    def dayIter(self, params):
        baseUrl ='http://gd2.mlb.com/components/game/mlb/year_'
        debugComplete = False
        for year in range(params['startYear'], params['endYear']+1):
            # iterate through months
            for month in range(4,12): 
                # iterate through days
                for day in range(1, self.getDaysOfMonth(month, year)):
                    curUrl = self.getDateUrl(baseUrl, day, month, year)
                    if not debugComplete:
                        params['cb'](curUrl)

                

                        if params['debug']:
                            debugComplete = True



    def printTreeStats(self, statIn):
        print(statIn.keys())
