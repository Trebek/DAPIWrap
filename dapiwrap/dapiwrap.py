#===============================================================================
# DAPIWrap: Doomworld API Wrapper
#-------------------------------------------------------------------------------
# Version: 0.1.0
# Updated: 07-06-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
A Python wrapper for the Doomworld /idgames archive API.

API documentation:
http://www.doomworld.com/idgames/api/

Doomworld /idgames archive:
http://www.doomworld.com/idgames/

Please, if you are using this, don't hammer the Doomworld API with requests.
I am not sure what kind of traffic their API can handle, so do the right 
thing, and limit the number of requests you make. I don't want this wrapper to 
be used (abused) to bog down their server. Be cool.

This script requires the `requests` package:
http://docs.python-requests.org/en/latest/

"""

#===============================================================================
# Imports
#===============================================================================

# from collections import deque
import random
import requests

from dapiwtools import (
    determine_lvl_path,
    Downwad,
    SearchFilter
)
from dapiwconst import (
    A_ABOUT,
    A_DBPING,
    A_GET_ID,
    A_GET_FILE,
    A_GETCONTENTS_ID,
    A_GETCONTENTS_NAME,
    A_GETDIRS_ID,
    A_GETDIRS_NAME,
    A_GETFILES_ID,
    A_GETFILES_NAME,
    A_LATESTVOTES,
    A_LATESTFILES,
    A_PARENTDIR_ID,
    A_PARENTDIR_FILE,
    A_PING,
    A_SEARCH,
    A_SEARCH_QUERY,
    A_SEARCH_DIRECT,
    A_SEARCH_SORT,
    A_SEARCH_TYPE,
    A_OUT_JSON,
    API_URL,
    DIRECT_ASC,
    DIRECT_DESC,
    FILTER_DATE,
    FILTER_GAME,
    FILTER_RATING,
    FILTER_SIZE,
    FILTER_VOTES,
    FILTER_YEAR,
    SORT_DATE,
    SORT_FILE,
    SORT_RATING,
    SORT_SIZE,
    TYPE_AUTHOR,
    TYPE_CREDITS,
    TYPE_DECRIP,
    TYPE_EDITORS,
    TYPE_EMAIL,
    TYPE_FILE,
    TYPE_TEXT,
    TYPE_TITLE,
)

#===============================================================================
# DAPIWrap Class
#===============================================================================

class DAPIWrap(object):
    """The main DAPIWrap class."""

    # CACHE_LIMIT = 100

    A_NOPARAM = [
        A_ABOUT, A_DBPING, A_PING
    ]

    A_SINGLEPARAM = [
        A_GET_ID, A_GET_FILE, A_GETCONTENTS_ID, A_GETCONTENTS_NAME, 
        A_GETFILES_NAME, A_GETDIRS_ID, A_GETDIRS_NAME, A_GETFILES_ID, 
        A_LATESTFILES, A_LATESTVOTES, A_PARENTDIR_FILE
    ]

    def __init__(self, dl_folder=None):
        """
        The DAPIWrap init method.

        :param dl_folder: The location to download files to.

        """
        # self.search_cache = deque([])
        # self.wadinfo_cache = deque([])
        self.dl_folder = dl_folder

        self.download = Downwad(self)
        self.filter = SearchFilter()

    def about(self):
        """
        Get information about the Doomworld API.

        :returns: Information about the Doomworld API.

        """
        about = self.call(A_ABOUT)

        if not raw and about.get("content"):
            return about["content"]
        else:
            return about

    def call(self, action, params=None):
        """
        Calls the API, using the given action/parameters.

        :param action: An action constant from ``dawglobs``.
        :param params: Any additional parameters for the action.

        :returns: The Doomworld API response.

        """
        if action in self.A_NOPARAM:
            url = "%s%s%s" % (API_URL, action, A_OUT_JSON)
        elif action in self.A_SINGLEPARAM:
            url = "%s%s%s" % (
                API_URL, action % (
                    params
                ), A_OUT_JSON
            )
        else:
            if action == A_SEARCH:
                if type(params) == dict:
                    url = "%s%s" % (API_URL, A_SEARCH_QUERY % (params["query"]))
                    if params.get("type"):
                        url += A_SEARCH_TYPE % (params["type"])
                    if params.get("sort"):
                        url += A_SEARCH_SORT % (params["sort"])
                    if params.get("dir"):
                        url += A_SEARCH_DIRECT % (params["dir"])
                else:
                    url = "%s%s" % (API_URL, A_SEARCH_QUERY % (params))
                url += A_OUT_JSON

        data = requests.get(url).json()

        return data

    # def cache_add(self, cache, items):
    #     """Adds the given items to the given cache."""

    #     if type(items) == list:
    #         [cache.append(x) for x in items if x not in cache]
    #     else:
    #         cache.append(items)

    #     while len(cache) >= self.CACHE_LIMIT:
    #         cache.popleft()

    def dbping(self):
        """
        Ping the database.

        :returns: Database status.

        """
        return self.call(A_DBPING)

    def get_contents(self, path, raw=False):
        """
        Gets the contents of a given path.

        :param path: The /idgames path to get content from.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Directory contents

        """
        contents = self.call(A_GETCONTENTS_NAME, path)

        if not raw and contents.get("content"):
            return contents["content"]
        else:
            return contents

    def get_file(self, path, raw=False):
        """
        Gets a file from the given path.

        :param path: The full path of the file, including the filename.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Wad info for the given file.

        """
        wad_info = self.call(A_GET_FILE, path)
        # self.cache_add(self.wadinfo_cache, wad_info)

        if not raw and wad_info.get("content"):
            # self.cache_add(self.wadinfo_cache, wad_info["content"])
            return wad_info["content"]
        else:
            return wad_info

    def get_file_alt(self, filename, game, raw=False):
        """
        Gets a file using the given filename.

        :param filename: The filename of the wad.
        :param game: The game the wad is for.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Wad info for the filename.

        """
        path = "%s%s" % (determine_lvl_path(filename, game), filename)

        wad_info = self.call(A_GET_FILE, path)

        if not raw and wad_info.get("content"):
            # self.cache_add(self.wadinfo_cache, wad_info["content"])
            return wad_info["content"]
        else:
            return wad_info

    def get_files(self, path, raw=False):
        """
        Gets the files under a directory of the given path.

        :param path: The /idgames path to return files from.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Files under the given path.

        """
        files = self.call(A_GETFILES_NAME, path)

        if not raw and files.get("content"):
            # self.cache_add(self.wadinfo_cache, files["content"]["file"])
            return files["content"]["file"]
        else:
            return files

    def get_dirs(self, path, raw=False):
        """
        Gets the directories under a directory of the given path.

        :param path: The /idgames path to return directories from.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Subdirectories in a given path.

        """
        dirs = self.call(A_GETDIRS_NAME, path)

        if not raw and dirs.get("content"):
            return dirs["content"]
        else:
            return dirs

    def get_id(self, wad_id, raw=False):
        """
        Gets the info for a wad with the given ID.

        :param wad_id: The ID number of a wad.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Wad info for the given ID.

        """
        wad_info = self.call(A_GET_ID, wad_id)
        # self.cache_add(self.wadinfo_cache, wad_info)

        if not raw and wad_info.get("content"):
            # self.cache_add(self.wadinfo_cache, wad_info["content"])
            return wad_info["content"]
        else:
            return wad_info

    def get_latestfiles(self, limit=10):
        """
        Get the latest uploaded files.

        :param limit: The number of items to retrieve.

        :returns: The latest files.

        """
        latest = self.call(A_LATESTFILES, limit)

        if not raw and latest.get("content"):
            # self.cache_add(self.wadinfo_cache, latest["content"])
            return latest["content"]
        else:
            return latest

    def get_latestvotes(self, limit=10):
        """
        Get the latest votes.

        :param limit: The number of items to retrieve.

        :returns: The latest votes.

        """
        latest = self.call(A_LATESTVOTES, limit)

        if not raw and latest.get("content"):
            # self.cache_add(self.wadinfo_cache, latest["content"])
            return latest["content"]
        else:
            return latest

    def get_parent_dir(self, path, raw=False):
        """
        Gets the parent directory for a given path.

        :param path: The /idgames path to return the parent from.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: The parent directory of the given directory path.

        """
        parent_dir = self.call(A_PARENTDIR_FILE, path)

        if not raw and parent_dir.get("content"):
            return parent_dir["content"]
        else:
            return parent_dir

    def ping(self):
        """
        Ping the Doomworld server.

        :returns: The Doomworld server status.

        """
        return self.call(A_PING)

    def search(self, query, params={}):
        """
        Search the /idgames archive.

        :param query: The search query.
        :param params: A ``dict`` of search parameters and/or filters.

        ``params`` can be one, or one of each of these keys/values:

        :param type: The type of search (what field your searching in).
            Accepted Values:
                TYPE_AUTHOR, TYPE_CREDITS, TYPE_DECRIP, TYPE_EDITORS,
                TYPE_EMAIL, TYPE_FILE, TYPE_TEXT, TYPE_TITLE            
        :param sort: What to sort the results by.
            Accepted Values:
                SORT_DATE, SORT_FILE, SORT_RATING, SORT_SIZE
        :param dir: The direction to order the results.
            Accepted Values:
                DIRECT_ASC, DIRECT_DESC
        :param filter: A filter, or filters (in a tuple/list) to apply to 
            the results. If you are using filters, you must also provide values 
            for the filters, and package them both into a tuple, or list. For 
            example, if you wanted to filter by year - 1994 in this case - you 
            would use this as a value for filter: 
                (FILTER_YEAR, 1994)
            If you wanted to use more than one filter, in this case by year 
            and game, you would use this:
                ((FILTER_YEAR, 1994), (FILTER_GAME, DOOM))
            Accepted Values:
                FILTER_GAME, FILTER_GYR, FILTER_YEAR, FILTER_RATING

        :returns: The search results.

        """
        params["query"] = query

        results = self.call(A_SEARCH, params)

        if not params.get("raw") and results.get("content"):
            if type(results["content"]["file"]) == list:
                results = results["content"]["file"]
            else:
                results = [results["content"]["file"]]
            if params.get("filter"):
                if type(params["filter"][0]) not in (tuple, list):
                    srchfilter = params["filter"][0]
                    filterargs = params["filter"][1]
                    results = self.filter.filters[srchfilter](
                        results, filterargs
                    )
                else:
                    for item in params["filter"]:
                        srchfilter = item[0]
                        filterargs = item[1]
                        results = self.filter.filters[srchfilter](
                            results, filterargs
                        )
            # self.cache_add(self.search_cache, results)

        return results

    def search_author(self, query, params={}):
        """
        Search the /idgames archive for the given author, using the 
        default search parameters.

        :param query: The search query.
        :param params: Optional. A ``dict`` of parameters and/or filters.

        :returns: The search results.

        """
        if not params:
            return self.search(query, {"type": TYPE_AUTHOR})
        else:
            params["type"] = TYPE_AUTHOR
            return self.search(query, params)

    def search_credits(self, query, params={}):
        """
        Search the credits of the files in the /idgames archive, using the 
        default search parameters.

        :param query: The search query.
        :param params: Optional. A ``dict`` of parameters and/or filters.

        :returns: The search results.

        """
        if not params:
            return self.search(query, {"type": TYPE_CREDITS})
        else:
            params["type"] = TYPE_CREDITS
            return self.search(query, params)

    def search_descrip(self, query, params={}):
        """
        Search the descriptions of files in the /idgames archive, using 
        the default search parameters.

        :param query: The search query.
        :param params: Optional. A ``dict`` of parameters and/or filters.

        :returns: The search results.

        """
        if not params:
            return self.search(query, {"type": TYPE_DESCRIP})
        else:
            params["type"] = TYPE_DESCRIP
            return self.search(query, params)

    def search_editors(self, query, params={}):
        """
        Search the /idgames archive for the given editors, using the 
        default search parameters.

        :param query: The search query.
        :param params: Optional. A ``dict`` of parameters and/or filters.

        :returns: The search results.

        """
        if not params:
            return self.search(query, {"type": TYPE_EDITORS})
        else:
            params["type"] = TYPE_EDITORS
            return self.search(query, params)

    def search_email(self, query, params={}):
        """
        Search the /idgames archive for the given email, using the 
        default search parameters.

        :param query: The search query.
        :param params: Optional. A ``dict`` of parameters and/or filters.

        :returns: The search results.

        """
        if not params:
            return self.search(query, {"type": TYPE_EMAIL})
        else:
            params["type"] = TYPE_EMAIL
            return self.search(query, params)

    def search_text(self, query, params={}):
        """
        Search the /idgames archive for the given title, using the 
        default search parameters.

        :param query: The search query.
        :param params: Optional. A ``dict`` of parameters and/or filters.

        :returns: The search results.

        """
        if not params:
            return self.search(query, {"type": TYPE_TEXT})
        else:
            params["type"] = TYPE_TEXT
            return self.search(query, params)

    def search_title(self, query, params={}):
        """
        Search the /idgames archive for the given title, using the 
        default search parameters.

        :param query: The search query.
        :param params: Optional. A ``dict`` of parameters and/or filters.

        :returns: The search results.

        """
        if not params:
            return self.search(query, {"type": TYPE_TITLE})
        else:
            params["type"] = TYPE_TITLE
            return self.search(query, params)

#===============================================================================
# If Main
#===============================================================================

if __name__ == '__main__':
    print "You're doing it wrong."