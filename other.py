from captains import *

team_pick_captain = ''


def pick_switch():
    global team_pick_captain
    if team_pick_captain == captains[0]:
        team_pick_captain = captains[1]
    elif team_pick_captain == captains[1]:
        team_pick_captain = captains[0]
