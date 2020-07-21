from lobby import *

factions = ['VS', 'NC', 'TR']
factions_match = {factions[0]: None, factions[1]: None, factions[2]: None}
factions_match_db = {}
match_id_pointer = 0


def init_db_match():
    match_id_pointer += 1
    factions_match_db[match_id_pointer] = factions_match
    return match_id


def set_faction(match_id, captain_id, requested_faction):
    if match_id in factions_match_db:
        if factions_match_db[match_id][requested_faction] is not None:
            factions_match_db[match_id][requested_faction] = captain_id
            return True
    return False

    
def get_factions_match_db_match(match_id):
    if match_id in factions_match_db:
        return factions_match_db[match_id]
    return None


def get_faction_from_captain(match_id, captain_id):
    """
        Returns the faction of the captain from the given match on success.
        Returns None if the captain is not yet assigned a faction in the match.
        Returns False if the specified match can't be retrieved.
    """
    match = get_factions_match_db_match(match_id)
    if match is not None:
        if captain_id in match.values():
            for i in match:
                if match[i] == captain_id:
                    return i;
        else:
            return None
    return False


def get_captain_from_faction(match_id, faction):
    """
        Returns the id of the captain of the faction from the given match on success.
        Returns None if no yet-assigned captain for the faction in the match.
        Returns False if the specified match can't be retrieved.
    """
    match = get_factions_match_db_match(match_id)
    if match is not None:
        return match[faction]
    return False
