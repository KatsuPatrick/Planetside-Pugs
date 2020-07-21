from match import *
from factions import *
from captains import *


team_1 = []
team_2 = []
roster = [team_1, team_2]


def get_roster():
    return roster


def add_roster(player, team):
    add(player, roster[team])
    remove_from_match_list(player)


def clear_roster():
    clear_faction_teams()
    clear_captains()
    clear(team_1)
    clear(team_2)
    clear_match()
