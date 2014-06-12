#===============================================================================
# DAPIWConst Global Constants
#-------------------------------------------------------------------------------
# Version: 0.2.0
# Updated: 11-06-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
This file contains all of the constants that are used by DAPIWrap and it's
associated tools, in ``dapiwtools``. I just figured it would be easier to keep 
them all consolidated. Users can just import the ones they need.

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

# idgames root
IDGAMES = "idgames/"

# Game path names
DOOM = "doom"
DOOM2 = "doom2"
HACX = "hacx"
HERETIC = "heretic"
HEXEN = "hexen"
STRIFE = "strife"
GAMES = [DOOM, DOOM2, HACX, HERETIC, HEXEN, STRIFE]

# Level paths
LVLS = "levels/%s/"
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
LVLS_DEATH_09 = "levels/%s/deathmatch/0-9/"
LVLS_DEATH_AC = "levels/%s/deathmatch/a-c/"
LVLS_DEATH_DF = "levels/%s/deathmatch/d-f/"
LVLS_DEATH_GI = "levels/%s/deathmatch/g-i/"
LVLS_DEATH_JL = "levels/%s/deathmatch/j-l/"
LVLS_DEATH_MO = "levels/%s/deathmatch/m-o/"
LVLS_DEATH_PR = "levels/%s/deathmatch/p-r/"
LVLS_DEATH_SU = "levels/%s/deathmatch/s-u/"
LVLS_DEATH_VZ = "levels/%s/deathmatch/v-z/"
LVLS_DEATH_MEGA = "levels/%s/deathmatch/megawads/"
LVLS_DEATH_PORTS_09 = "levels/%s/deathmatch/Ports/0-9/"
LVLS_DEATH_PORTS_AC = "levels/%s/deathmatch/Ports/a-c/"
LVLS_DEATH_PORTS_DF = "levels/%s/deathmatch/Ports/d-f/"
LVLS_DEATH_PORTS_GI = "levels/%s/deathmatch/Ports/g-i/"
LVLS_DEATH_PORTS_JL = "levels/%s/deathmatch/Ports/j-l/"
LVLS_DEATH_PORTS_MO = "levels/%s/deathmatch/Ports/m-o/"
LVLS_DEATH_PORTS_PR = "levels/%s/deathmatch/Ports/p-r/"
LVLS_DEATH_PORTS_SU = "levels/%s/deathmatch/Ports/s-u/"
LVLS_DEATH_PORTS_VZ = "levels/%s/deathmatch/Ports/v-z/"
LVLS_DEATH_PORTS_MEGA = "levels/%s/deathmatch/Ports/megawads/"
LVLS_MEGA = "levels/%s/megawads/"
LVLS_PORTS = "levels/%s/Ports/"
LVLS_PORTS_09 = "levels/%s/Ports/0-9/"
LVLS_PORTS_AC = "levels/%s/Ports/a-c/"
LVLS_PORTS_DF = "levels/%s/Ports/d-f/"
LVLS_PORTS_GI = "levels/%s/Ports/g-i/"
LVLS_PORTS_JL = "levels/%s/Ports/j-l/"
LVLS_PORTS_MO = "levels/%s/Ports/m-o/"
LVLS_PORTS_PR = "levels/%s/Ports/p-r/"
LVLS_PORTS_SU = "levels/%s/Ports/s-u/"
LVLS_PORTS_VZ = "levels/%s/Ports/v-z/"
LVLS_PORTS_MEGA = "levels/%s/Ports/megawads/"

#-------------------------------------------------------------------------------
# Level Path Lists
#-------------------------------------------------------------------------------

# Alphabetical paths under "levels/<GAME>/"
LVLS_ALPHA = [
    LVLS_09, LVLS_AC, LVLS_DF, LVLS_GI, LVLS_JL, LVLS_MO, LVLS_PR, LVLS_SU,
    LVLS_VZ
]

# Alphabetical paths under "levels/<GAME>/deathmatch/"
LVLS_DEATH_ALPHA = [
    LVLS_DEATH_09, LVLS_DEATH_AC, LVLS_DEATH_DF, LVLS_DEATH_GI, LVLS_DEATH_JL,
    LVLS_DEATH_MO, LVLS_DEATH_PR, LVLS_DEATH_SU, LVLS_DEATH_VZ
]

# Alphabetical paths under "levels/<GAME>/deathmatch/Ports/"
LVLS_DEATH_PORTS_ALPHA = [
    LVLS_DEATH_PORTS_09, LVLS_DEATH_PORTS_AC, LVLS_DEATH_PORTS_DF,
    LVLS_DEATH_PORTS_GI, LVLS_DEATH_PORTS_JL, LVLS_DEATH_PORTS_MO,
    LVLS_DEATH_PORTS_PR, LVLS_DEATH_PORTS_SU, LVLS_DEATH_PORTS_VZ
]

# Alphabetical paths under "levels/<GAME>/Ports/"
LVLS_PORTS_ALPHA = [
    LVLS_PORTS_09, LVLS_PORTS_AC, LVLS_PORTS_DF, LVLS_PORTS_GI, LVLS_PORTS_JL, 
    LVLS_PORTS_MO, LVLS_PORTS_PR, LVLS_PORTS_SU, LVLS_PORTS_VZ
]

# All paths under "levels/"
LVLS_ALL = (
    LVLS_ALPHA + [LVLS_MEGA] + LVLS_DEATH_ALPHA + [LVLS_DEATH_MEGA] + 
    LVLS_DEATH_PORTS_ALPHA + [LVLS_DEATH_PORTS_MEGA] + LVLS_PORTS_ALPHA + 
    [LVLS_PORTS_MEGA]
)

#-------------------------------------------------------------------------------
# Search Parameters
#-------------------------------------------------------------------------------

# Search types
TYPE_AUTHOR = "author"
TYPE_CREDITS = "credits"
TYPE_DECRIP = "description"
TYPE_EDITORS = "editors"
TYPE_EMAIL = "email"
TYPE_FILE = "filename"
TYPE_TEXT = "textfile"
TYPE_TITLE = "title"

# Search sorting methods
SORT_DATE = "date"
SORT_FILE = "filename"
SORT_RATING = "rating"
SORT_SIZE = "size"

# Sort direction
DIRECT_ASC = "asc"
DIRECT_DESC = "desc"

#-------------------------------------------------------------------------------
# Filter Stuff
#-------------------------------------------------------------------------------

# Filter names
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