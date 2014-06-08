#===============================================================================
# DAPIWConst Global Constants
#-------------------------------------------------------------------------------
# Version: 0.1.0
# Updated: 07-06-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
This file contains all of the constants that are used by DAPIWrap and it's
associated tools, in ``dapiwtools``. Just figured it would be easier to keep them
all consolidated.

"""

#-------------------------------------------------------------------------------
# API URL and API Actions
#-------------------------------------------------------------------------------

# Doomworld API url
API_URL = "http://www.doomworld.com/idgames/api/api.php?action="

# API Actions
A_ABOUT = "about"
A_DBPING = "dbping"
A_GET_ID = "get&id=%d"
A_GET_FILE = "get&file=%s"
A_GETCONTENTS_ID = "getcontents&id=%d"
A_GETCONTENTS_NAME = "getcontents&name=%s"
A_GETDIRS_ID = "getdirs&id=%d"
A_GETDIRS_NAME = "getdirs&name=%s"
A_GETFILES_ID = "getfiles&id=%d"
A_GETFILES_NAME = "getfiles&name=%s"
A_LATESTVOTES = "latestvotes&limit=%d"
A_LATESTFILES = "latestfiles&limit=%d"
A_OUT_JSON = "&out=json"
A_PARENTDIR_ID = "getparentdir&id=%d"
A_PARENTDIR_FILE = "getparentdir&name=%s"
A_PING = "ping"
A_SEARCH = "search&query=%s&type=%s&sort=%s&dir=%s"
A_SEARCH_QUERY = "search&query=%s"
A_SEARCH_DIRECT = "&dir=%s"
A_SEARCH_SORT = "&sort=%s"
A_SEARCH_TYPE = "&type=%s"

#-------------------------------------------------------------------------------
# Download Servers
#-------------------------------------------------------------------------------

# FTP Download servers
DL_FTP_GERMANY = "ftp.fu-berlin.de"
DL_FTP_GREECE = "ftp.ntua.gr"
DL_FTP_TEXAS = "ftp.mancubus.net"
DL_FTP = [DL_FTP_GERMANY, DL_FTP_GREECE, DL_FTP_TEXAS]

# HTTP Download servers
DL_FLORIDA = "http://www.gamers.org/pub/"
DL_GREECE = "http://ftp.ntua.gr/pub/vendors/"
DL_NEWYORK = "http://youfailit.net/pub/"
DL_TEXAS = "http://ftp.mancubus.net/pub/"
DL_HTTP = [DL_FLORIDA, DL_GREECE, DL_NEWYORK, DL_TEXAS]

#-------------------------------------------------------------------------------
# FTP Specific Paths
#-------------------------------------------------------------------------------

FTP_DIR_GERMANY = "pc/games/idgames/"
FTP_DIR_GREECE = "pub/vendors/idgames/"
FTP_DIR_TEXAS = "pub/idgames/"

#-------------------------------------------------------------------------------
# /idgames Paths and Game Names
#-------------------------------------------------------------------------------

# /idgames root
IDGAMES = "idgames/"

# Game path names
DOOM = "doom"
DOOM2 = "doom2"
HACX = "hacx"
HERETIC = "heretic"
HEXEN = "hexen"
STRIFE = "strife"
GAMES = [DOOM, DOOM2, HACX, HERETIC, HEXEN, STRIFE]

# General purpose level paths
LVLS_09 = "levels/%s/0-9/"
LVLS_AC = "levels/%s/a-c/"
LVLS_DF = "levels/%s/d-f/"
LVLS_GI = "levels/%s/g-i/"
LVLS_JL = "levels/%s/j-l/"
LVLS_MO = "levels/%s/m-o/"
LVLS_PR = "levels/%s/p-r/"
LVLS_SU = "levels/%s/s-u/"
LVLS_VZ = "levels/%s/v-z/"
LVLS_DEATH = "levels/%s/deathmatch/"
LVLS_MEGA = "levels/%s/megawads/"
LVLS_PORTS = "levels/%s/Ports/"

# Doom /idgames level paths
DOOM_LVLS_09 = "levels/doom/0-9/"
DOOM_LVLS_AC = "levels/doom/a-c/"
DOOM_LVLS_DF = "levels/doom/d-f/"
DOOM_LVLS_GI = "levels/doom/g-i/"
DOOM_LVLS_JL = "levels/doom/j-l/"
DOOM_LVLS_MO = "levels/doom/m-o/"
DOOM_LVLS_PR = "levels/doom/p-r/"
DOOM_LVLS_SU = "levels/doom/s-u/"
DOOM_LVLS_VZ = "levels/doom/v-z/"
DOOM_LVLS_DEATH = "levels/doom/deathmatch/"
DOOM_LVLS_MEGA = "levels/doom/megawads/"
DOOM_LVLS_PORTS = "levels/doom/Ports/"
DOOM_LVLS = [
    DOOM_LVLS_09, DOOM_LVLS_AC, DOOM_LVLS_DF, DOOM_LVLS_GI,
    DOOM_LVLS_JL, DOOM_LVLS_MO, DOOM_LVLS_PR, DOOM_LVLS_SU,
    DOOM_LVLS_VZ
]
DOOM_LVLS_OTHER = [
    DOOM_LVLS_DEATH, DOOM_LVLS_MEGA, DOOM_LVLS_PORTS
]

# Doom 2 /idgames level paths
DOOM2_LVLS_09 = "levels/doom2/0-9/"
DOOM2_LVLS_AC = "levels/doom2/a-c/"
DOOM2_LVLS_DF = "levels/doom2/d-f/"
DOOM2_LVLS_GI = "levels/doom2/g-i/"
DOOM2_LVLS_JL = "levels/doom2/j-l/"
DOOM2_LVLS_MO = "levels/doom2/m-o/"
DOOM2_LVLS_PR = "levels/doom2/p-r/"
DOOM2_LVLS_SU = "levels/doom2/s-u/"
DOOM2_LVLS_VZ = "levels/doom2/v-z/"
DOOM2_LVLS_DEATH = "levels/doom2/deathmatch/"
DOOM2_LVLS_MEGA = "levels/doom2/megawads/"
DOOM2_LVLS_PORTS = "levels/doom2/Ports/"
DOOM2_LVLS = [
    DOOM2_LVLS_09, DOOM2_LVLS_AC, DOOM2_LVLS_DF, DOOM2_LVLS_GI,
    DOOM2_LVLS_JL, DOOM2_LVLS_MO, DOOM2_LVLS_PR, DOOM2_LVLS_SU,
    DOOM2_LVLS_VZ
]
DOOM2_LVLS_OTHER = [
    DOOM2_LVLS_DEATH, DOOM2_LVLS_MEGA, DOOM2_LVLS_PORTS
]

#-------------------------------------------------------------------------------
# Search Parameters & Filter Stuff
#-------------------------------------------------------------------------------

TYPE_AUTHOR = "author"
TYPE_CREDITS = "credits"
TYPE_DECRIP = "description"
TYPE_EDITORS = "editors"
TYPE_EMAIL = "email"
TYPE_FILE = "filename"
TYPE_TEXT = "textfile"
TYPE_TITLE = "title"

SORT_DATE = "date"
SORT_FILE = "filename"
SORT_RATING = "rating"
SORT_SIZE = "size"

DIRECT_ASC = "asc"
DIRECT_DESC = "desc"

FILTER_DATE = "filter:date"
FILTER_GAME = "filter:game"
FILTER_GYR = "filter:gyr"
FILTER_RATING = "filter:rating"
FILTER_SIZE = "filter:size"
FILTER_VOTES = "filter:votes"
FILTER_YEAR = "filter:year"
FILTERS = [
    FILTER_DATE, FILTER_GAME, FILTER_RATING, 
    FILTER_SIZE, FILTER_VOTES, FILTER_YEAR
]

#===============================================================================
# If Main
#===============================================================================

if __name__ == '__main__':
    print "You're doing it wrong."