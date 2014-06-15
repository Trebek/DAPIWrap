#===============================================================================
# DAPIWrap: Doomworld API Wrapper
#-------------------------------------------------------------------------------
# Version: 0.3.0
# Updated: 15-06-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
DAPIWrap, short for "Doomworld API Wrapper", is a simple Python wrapper for the 
Doomworld idgames archive API.

This pacakge is still in the beta stages, so expect changes that may break
things, if you're using it.

Doomworld API documentation:
http://www.doomworld.com/idgames/api/

Doomworld idgames archive:
http://www.doomworld.com/idgames/

Note:

Please don't hammer the Doomworld API with requests. I am not sure what kind 
of traffic their API can handle, so do the right thing, and limit the number 
of requests you make. I don't want this wrapper to be used (abused) to bog down 
their server. Be cool.

This package requires the ``requests`` package:
http://docs.python-requests.org/en/latest/

"""

#===============================================================================
# Imports
#===============================================================================

import requests

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
    SORT_DATE,
    TYPE_AUTHOR,
    TYPE_CREDITS,
    TYPE_DESCRIP,
    TYPE_EDITORS,
    TYPE_EMAIL,
    TYPE_FILE,
    TYPE_TEXT,
    TYPE_TITLE,
)

from dapiwtools import (
    Downwad,
    IOFuncs,
    MiscFuncs,
    SearchFilter
)

#===============================================================================
# DAPIWrap Class
#===============================================================================

class DAPIWrap(object):
    """The main DAPIWrap class."""

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
        self.dl_folder = dl_folder

        # DAPIWrap "tools".
        self.download = Downwad(self)
        self.filter = SearchFilter()
        self.io = IOFuncs()
        self.misc = MiscFuncs(self)

    def about(self):
        """
        Get information about the Doomworld API.

        :returns: Information about the Doomworld API.

        """
        about = self.call(A_ABOUT)

        if not raw and "content" in about:
            return about["content"]
        else:
            return about

    def call(self, action, params=None):
        """
        Calls the API, using the given action/parameters.

        :param action: An action constant from ``dapiwconst``.
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
                    if "type" in params:
                        url += A_SEARCH_TYPE % (params["type"])
                    if "sort" in params:
                        url += A_SEARCH_SORT % (params["sort"])
                    if "dir" in params:
                        url += A_SEARCH_DIRECT % (params["dir"])
                else:
                    url = "%s%s" % (API_URL, A_SEARCH_QUERY % (params))
                url += A_OUT_JSON

        data = requests.get(url).json()

        return data

    def dbping(self):
        """
        Ping the database.

        :returns: Database status.

        """
        return self.call(A_DBPING)

    def get_contents(self, path, raw=False):
        """
        Gets the contents of a given path.

        :param path: The idgames path to get content from.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Directory contents

        """
        contents = self.call(A_GETCONTENTS_NAME, path)

        if not raw and "content" in contents:
            return contents["content"]
        else:
            return contents

    def get_file_path(self, path, raw=False):
        """
        Gets a file from the given path.

        :param path: The full path of the file, including the filename.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Wad info for the given file.

        """
        wad_info = self.call(A_GET_FILE, path)

        if not raw and "content" in wad_info:
            return wad_info["content"]
        else:
            return wad_info

    def get_files(self, path, raw=False):
        """
        Gets the files under a directory of the given path.

        :param path: The idgames path to return files from.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Files under the given path.

        """
        files = self.call(A_GETFILES_NAME, path)

        if not raw and "content" in files:
            if type(files["content"]["file"]) == list:
                return files["content"]["file"]
            else:
                return [files["content"]["file"]]
        else:
            return []

    def get_dirs(self, path, raw=False):
        """
        Gets the directories under a directory of the given path.

        :param path: The idgames path to return directories from.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Subdirectories in a given path.

        """
        dirs = self.call(A_GETDIRS_NAME, path)

        if not raw and "content" in dirs:
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

        if not raw and "content" in wad_info:
            return wad_info["content"]
        else:
            return wad_info

    def get_id_list(self, id_list, raw=False):
        """
        Gets the info for a wad with the given ID.

        :param id_list: A list of wad ID numbers.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: Wad info for the given list of IDs.

        """
        results = []

        for wad_id in id_list:
            wad_info = self.call(A_GET_ID, wad_id)
            if not raw and "content" in wad_info:
                results.append(wad_info["content"])
            else:
                return wad_info

        return results

    def get_latestfiles(self, limit=10):
        """
        Get the latest uploaded files.

        :param limit: The number of items to retrieve.

        :returns: The latest files.

        """
        latest = self.call(A_LATESTFILES, limit)

        if not raw and "content" in latest:
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

        if not raw and "content" in latest:
            return latest["content"]
        else:
            return latest

    def get_parent_dir(self, path, raw=False):
        """
        Gets the parent directory for a given path.

        :param path: The idgames path to return the parent from.
        :param raw: Whether to return the data exactly as recieved (raw), or
        to extract the contents and return just the contents in a list.

        :returns: The parent directory of the given directory path.

        """
        parent_dir = self.call(A_PARENTDIR_FILE, path)

        if not raw and "content" in parent_dir:
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
        Search the idgames archive.

        :param query: The search query.
        :param params: A ``dict`` of search parameters and/or filters.

        ``params`` can be one, or one of each of these keys/values:

        :param type: The type of search (what field your searching in).
            |Accepted Values:
            |TYPE_AUTHOR, TYPE_CREDITS, TYPE_DESCRIP, TYPE_EDITORS,
            |TYPE_EMAIL, TYPE_FILE, TYPE_TEXT, TYPE_TITLE            
        :param sort: What to sort the results by.
            |Accepted Values:
            |SORT_DATE, SORT_FILE, SORT_RATING, SORT_SIZE
        :param dir: The direction to order the results.
            |Accepted Values:
            |DIRECT_ASC, DIRECT_DESC
        :param filter: A filter, or filters (in a tuple/list) to apply to 
            the results. If you are using filters, you must also provide values 
            for the filters, and package them both into a tuple, or list. For 
            example, if you wanted to filter by year - 1994 in this case - you 
            would use this as a value for filter: 
            |(FILTER_YEAR, 1994)
            If you wanted to use more than one filter, in this case by year 
            and game, you would use this:
            |((FILTER_YEAR, 1994), (FILTER_GAME, DOOM))
            Accepted Values:
            |FILTER_GAME, FILTER_GYR, FILTER_YEAR, FILTER_RATING

        :returns: A list of search results.

        """
        params["query"] = query

        results = self.call(A_SEARCH, params)

        if "raw" not in params and "content" in results:
            if type(results["content"]["file"]) == list:
                results = results["content"]["file"]
            else:
                results = [results["content"]["file"]]
            if "filter" in params:
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
            return results
        return []

    def search_author(self, query, params={}):
        """
        Search the idgames archive for the given author, using the 
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
        Search the credits of the files in the idgames archive, using the 
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
        Search the descriptions of files in the idgames archive, using 
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
        Search the idgames archive for the given editors, using the 
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
        Search the idgames archive for the given email, using the 
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

    def search_local(self, items, query, params={}):
        """        
        Search the given items. Can't search the credits, editors, or textfiles 
        of the given items, if they were retrieved using ``DAPIWrap.search``, 
        or ``DAPIWrap.get_files``, because these actions don't return the full 
        info for each wad. Only a brief version, missing those areas mentioned.
        However, if the items were retrieved using ``DAPIWrap.get_id`` or
        ``DAPIWrap.get_file_path``, then you can search those areas as well.

        :param items: A list of wad info to search through.
        :param query: The search query.
        :param params: A ``dict`` of search parameters and/or filters.

        :returns: A list of search results.

        """
        query_lower = query.lower()

        srchtype = params.get("type")
        srchsort = params.get("sort")
        srchdir = params.get("dir")
        srchfilters = params.get("filter")

        # Set up default search parameters, if none given.
        if not srchtype:
            srchtype = TYPE_FILE
        if not srchsort:
            srchsort = SORT_DATE
        if not srchdir:
            srchdir = DIRECT_ASC

        # Search through given items, build a list of results.
        try:
            local_results = [
                x for x in items if query_lower in x[srchtype].lower()
            ]
        except AttributeError:
            pass

        # Filter the results, if called for.
        if srchfilters:
            local_results = self.filter.chain(local_results, srchfilters)

        # Sort the results.
        local_results = sorted(local_results, key=lambda x: x[srchsort])

        # Reverse the results order, if called for.
        if srchdir == DIRECT_DESC:
            return local_results[::-1]
        else:
            return local_results

    def search_text(self, query, params={}):
        """
        Search the idgames archive for the given title, using the 
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
        Search the idgames archive for the given title, using the 
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