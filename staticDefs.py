

eventTypes = ['Strikeout', 'Single', 'Forceout', 'Flyout', 'Lineout', 'Home Run', 'Groundout', 'Double', 'Pop Out', 'Sac Fly', 'Hit By Pitch', 'Grounded Into DP', 'Walk', 'Field Error', 'Double Play', 'Bunt Groundout', 'Strikeout - DP', 'Triple', 'Fielders Choice', 'Runner Out', 'Sac Bunt', 'Fielders Choice Out', 'Bunt Pop Out', 'Catcher Interference']

eventValues = {
# Based on fanduel scoring. 
# todo: RBI's (3.5), runs (3.2), (though these should follow naturally from choosing successful hitters?)
# todo: Steals (6) (would be tough but interesting to find good pitcher / catcher batteries that are easier to steal on)
'Strikeout' : 0,
'Forceout': 0,
'Flyout': 0,
'Lineout': 0,
'Groundout': 0,
'Pop Out': 0,
'Sac Fly': 0,
'Single': 3,
'Double': 6,
'Triple': 9,
'Home Run': 12,
'Hit By Pitch': 3,
'Grounded Into DP': 0, 
'Walk': 3,
'Field Error': 0, 
'Double Play': 0, 
'Bunt Groundout': 0, 
'Strikeout - DP': 0, 
'Fielders Choice': 0, 
'Runner Out': 0, 
'Sac Bunt': 0, 
'Fielders Choice Out': 0, 
'Bunt Pop Out': 0, 
'Catcher Interference': 0
}