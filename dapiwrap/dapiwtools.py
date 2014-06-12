#===============================================================================
# DAPIWTools: Useful Helper Functions for DAPIWrap.
#-------------------------------------------------------------------------------
# Version: 0.2.0
# Updated: 11-06-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
This module contains a few useful helper classes/functions used by DAPIWrap 
that aren't provided by the Doomworld API, such as search filters, and a 
download interface.

"""

#===============================================================================
# Imports
#===============================================================================

import ftplib
import gzip
import json
import os
import random
import requests
import time
import webbrowser

from dapiwconst import (
    DL_FLORIDA,
    DL_FTP,
    DL_FTP_GERMANY,
    DL_FTP_GREECE,
    DL_FTP_TEXAS,
    DOOM,
    DOOM2,
    FTP_DIR_GERMANY,
    FTP_DIR_GREECE,
    FTP_DIR_TEXAS,
    FILTER_DATE,
    FILTER_GAME,
    FILTER_RATING,
    FILTER_SIZE,
    FILTER_VOTES,
    FILTER_YEAR,
    GAMES,
    IDGAMES,
    LVLS_09,
    LVLS_AC,
    LVLS_DF,
    LVLS_GI,
    LVLS_JL,
    LVLS_MO,
    LVLS_PR,
    LVLS_SU,
    LVLS_VZ,
    LVLS_ALL
)

#===============================================================================
# SearchFilter Class
#===============================================================================

class SearchFilter(object):
    """Contains methods for filtering search results."""

    def __init__(self):
        """The init method for the SearchFilter class."""

        self.filters = {
            FILTER_DATE: self.date,
            FILTER_GAME: self.game,
            FILTER_RATING: self.rating,
            FILTER_SIZE: self.size,
            FILTER_VOTES: self.votes,
            FILTER_YEAR: self.year
        }

    def chain(self, results, *args):
        """
        Filter given results using given chain of filters & parameters.

        :param results: The results to filter.
        :param *args: The filters to apply to the results.

        :returns: The filtered results.

        """
        for arg in args:
            results = self.filters[arg[0]](results, arg[1])

        return results

    def date(self, results, date="yyyy-mm-dd"):
        """
        Filter given results by given date.

        :param date: The results to filter.
        :param year: The date to filter the results by.

        :returns: The filtered results.

        """
        return [x for x in results if x["date"] == date]

    def year(self, results, year=1994):
        """
        Filter given results by given year.

        :param results: The results to filter.
        :param year: The year to filter the results by. Can be a range,
        low to high, in a tuple/list.

        :returns: The filtered results.

        """
        year_type = type(year)

        if year_type in (tuple, list):
            y_range = list(xrange(year[0], (year[1] + 1), 1))
        else:
            y_range = [year]

        y_range = [str(x) for x in y_range]

        return [x for x in results if x["date"][0:4] in y_range]

    def gyr(self, results, game=DOOM, year=1994, rating=5.0):
        """
        Filter the given results by the given game, year, and rating.

        :param results: The results to filter.
        :param game: The game to filter the results by.
        :param year: The year to filter the results by.
        :param rating: The rating to filter the results by.

        :returns: The filtered results.

        """
        return self.chain(
            results, 
            (FILTER_GAME, game), 
            (FILTER_YEAR, year),
            (FILTER_RATING, rating)
        )

    def game(self, results, game=DOOM):
        """
        Filter the given results by the given game.

        :param game: The game to filter the results by.

        :returns: The filtered results.

        """
        game_path = "%s/" % (game)

        return [x for x in results if game_path in x["dir"]]

    def rating(self, results, rating=5.0):
        """
        Filter the given results by rating.

        :param rating: The rating to filter the results by. Can be a range,
        low to high, in a tuple/list.

        :returns: The filtered results.

        """
        rating_type = type(rating)

        if rating_type in (tuple, list):
            r_range = list(frange(rating[0], rating[1], 0.1))
        else:
            r_range = [rating]

        return [
            x for x in results if trunc_rating(x["rating"]) in r_range
        ]

    def size(self, results, size=1000):
        """
        Filter the given results by file size.

        :param size: The size to filter the results by. Must be at least 1000
        (1kb). Can be a range, low to high, in a tuple/list.

        :returns: The filtered results.

        """
        size_type = type(size)

        if size_type in (tuple, list):
            s_range = list(xrange(size[0], size[1], 1))
        else:
            s_range = [size]

        return [
            x for x in results if (x["size"] / 1000) in s_range
        ]

    def votes(self, results, votes=1):
        """
        Filter the given results by number of votes.

        :param votes: The number of  votes to filter the results by. Can be a 
        range, ow to high, in a tuple/list.

        :returns: The filtered results.

        """
        votes_type = type(votes)

        if votes_type in (tuple, list):
            v_range = list(xrange(votes[0], votes[1], 1))
        else:
            v_range = [votes]

        return [
            x for x in results if x["votes"] in v_range
        ]

#===============================================================================
# Downwad Class
#===============================================================================

class Downwad(object):
    """
    Contains methods for downloading wads from the supported mirrors
    on the Doomworld /idgames archive.

    """
    # Don't set `DL_DELAY` much lower. Don't want to hammer the server.
    DL_DELAY = 5

    def __init__(self, daw):
        """
        The init method for the Downwad class.

        :param daw: An instance of DAPIWrap. Requires this, as this class
        makes use of some of DAPIWrap's functionality.

        """
        self.daw = daw
        self.last_server = None

    def download(
            self, filename, file_dir, dl_folder=None, 
            server=DL_FTP_GERMANY, newdir=True
        ):
        """
        Downloads a wad with the given filename from the given /idgames 
        directory. If `server` is an FTP server address, `download` will
        call `download_ftp`, with the given arguments, instead.

        :param filename: The filename of the file to download.
        :param file_dir: The /idgames path of the file.
        :param dl_folder: Where to download the file to.
        :param server: Which server to download from.
        :param newdir: Whether to make a new subdirectory for the wad, using 
        the wad's filename.

        :returns: The file object, or if FTP is used, the final status of 
        the download.

        """
        if not dl_folder:
            if self.daw.dl_folder:
                dl_folder = self.daw.dl_folder
            else:
                return

        if server not in DL_FTP:

            dl_url = "%s%s%s%s" % (server, IDGAMES, file_dir, filename)

            wad_zip = requests.get(dl_url, stream=True)

            # if newdir:
            #     new = "%s%s" % (dl_folder, filename[:-4])
            #     if not os.path.exists(new):
            #         os.makedirs(new)
            #     save_loc = "%s\%s" % (new, filename)
            # else:
            #     save_loc = dl_folder + filename

            if newdir:
                if not os.path.exists(dl_folder):
                    os.makedirs(dl_folder)

            save_loc = dl_folder + filename

            with open(save_loc, "wb") as new_wad_zip:
                for chunk in wad_zip.iter_content(chunk_size=1024): 
                    if chunk:
                        new_wad_zip.write(chunk)
            return wad_zip
        else:
            return self.ftp_download(
                filename, file_dir, dl_folder, server, newdir
            )

    def ftp_download(
            self, filename, file_dir, dl_folder=None, 
            server=DL_FTP_GERMANY, newdir=True
        ):
        """        
        Downloads a wad with the given filename from the given /idgames 
        directory, from a given FTP server.

        :param filename: The filename of the file to download.
        :param file_dir: The /idgames path of the file.
        :param dl_folder: Where to download the file to.
        :param server: Which server to download from.
        :param newdir: Whether to make a new subdirectory for the wad, using 
        the wad's filename.

        :returns: The final status of the download.

        """
        connection = ftplib.FTP(server)
        connection.login() 

        if server == DL_FTP_GERMANY:
            connection.cwd(FTP_DIR_GERMANY + file_dir)
        elif server == DL_FTP_GREECE:
            connection.cwd(FTP_DIR_GREECE + file_dir)
        elif server == DL_FTP_TEXAS:
            connection.cwd(FTP_DIR_TEXAS + file_dir)
        else:
            return

        # if newdir:
        #     new = "%s%s" % (dl_folder, filename[:-4])
        #     if not os.path.exists(new):
        #         os.makedirs(new)
        #     save_loc = "%s\%s" % (new, filename)
        # else:
        #     save_loc = dl_folder + filename

        if newdir:
            if not os.path.exists(dl_folder):
                os.makedirs(dl_folder)

        save_loc = dl_folder + filename

        status = connection.retrbinary(
            "RETR %s" % (filename), open(save_loc, 'wb').write
        )

        connection.quit()

        return status

    def wad_id(
            self, wad_id, dl_folder=None, server=DL_FTP_GERMANY, 
            newdir=True
        ):
        """
        Downloads a wad with the given ID.

        :param wad_id: The id of the wad to download.
        :param dl_folder: Where to download the file to.
        :param server: Which server to download from.
        :param newdir: Whether to make a new subdirectory for the wad, using 
        the wad's filename.

        :returns: The file object, or if FTP is used, the final status of 
        the download.

        """
        wad_info = self.daw.get_id(wad_id)

        if "error" in wad_info:
            return wad_info

        file_dir = wad_info["dir"]
        filename = wad_info["filename"]

        result = self.download(
            filename, file_dir, dl_folder, server, newdir
        )

        return result

    def id_list(
            self, id_list, dl_folder=None, server=DL_FTP_GERMANY, 
            newdir=True
        ):
        """
        Download wads from a given list/tuple of id numbers.

        :param id_list: The list/tuple of ID numbers of wads to download.
        :param dl_folder: Where to download the file to.
        :param server: Which server to download from.
        :param newdir: Whether to make a new subdirectory for the wad, using 
        the wad's filename.

        :returns: Any errors.

        """
        list_len = len(id_list)
        count = 0
        errors = []

        for wad_id in id_list:
            count += 1
            result = self.wad_id(
                wad_id,
                dl_folder,
                server,
                newdir
            )
            if "error" in result or "warning" in result:
                errors.append(result)
            if count < list_len:
                time.sleep(self.DL_DELAY)

        if errors:
            return errors

    def file_path(
        self, path, dl_folder=None, server=DL_FTP_GERMANY, 
        newdir=True
        ):
        """
        Download a wad, using the given wad info.

        :param path: The full idgames path of the wad, including filename.
        :param dl_folder: Where to download the file to.
        :param server: Which server to download from.
        :param newdir: Whether to a new subdirectory for the wad, using the
        wad's filename.

        :returns: The file object, or if FTP is used, the final status of 
        the download.

        """
        wad_info = self.daw.get_file_path(path)

        wad_dir = wad_info["dir"]
        wad_filename = wad_info["filename"]

        return self.download(wad_filename, wad_dir, dl_folder, server, newdir)

    def folder_year(
            self, year, file_dir=None, dl_folder=None, 
            server=DL_FTP_GERMANY, newdir=True
        ):
        """
        Download all of the wads from a given year, in a given 
        /idgames folder.

        :param year: The year to download wads from.
        :param file_dir: The /idgames path to download from.
        :param dl_folder: Where to download the file to.
        :param server: Which server to download from.
        :param newdir: Whether to make a new subdirectory for each wad, using 
        the wad's filename.

        :returns: None.

        """
        year = str(year)
        files = self.daw.get_files(file_folder)
        files_len = len(files["content"]["file"])
        count = 0
        errors = []
        for item in files["content"]["file"]:
            count += 1
            if item["date"][0:4] == year:
                result = self.download(
                    item["filename"],
                    item["dir"],
                    dl_folder,
                    server,
                    newdir
                )
                if "error" in result or "warning" in result:
                    errors.append(result)
                if count < files_len:
                    time.sleep(self.DL_DELAY)

        if errors:
            return errors

    def wad_info(
            self, wad_info, dl_folder=None, server=DL_FTP_GERMANY, 
            newdir=True
        ):
        """
        Download a wad, using the given wad info.

        :param wad_info: The wad info, in dict (JSON) form.
        :param dl_folder: Where to download the file to.
        :param server: Which server to download from.
        :param newdir: Whether to a new subdirectory for the wad, using the
        wad's filename.

        :returns: The file object, or if FTP is used, the final status of 
        the download.

        """
        wad_dir = wad_info["dir"]
        wad_filename = wad_info["filename"]

        return self.download(wad_filename, wad_dir, dl_folder, server, newdir)

#===============================================================================
# Other Bits & Pieces
#===============================================================================

def frange(start, stop, step, floatfix=True):
    """
    Returns a float range generator.

    :param start: The start of the range.
    :param stop: The end of the range.
    :param step: How much to increment the range each step.
    :param floatfix: This "fixes" the floats so that equality checks work.
    Why this works? I really don't know. But it does.

    :yields: A float range.

    """
    r = start
    while r < stop:
        if floatfix:
            yield float(str(r))
        else:
            yield r
        r += step

def random_wad(daw, game=None):
    """
    Gets the info for a random wad for a given game, or a random game if
    none is given.

    :param daw: An instance of DAPIWrap.
    :param game: The game to get a random wad for.

    :returns: The info for a random wad.

    """
    if not game:
        game = random.choice(GAMES)
    path = random.choice(LVLS_ALL) % (game)
    files = daw.get_files(path)

    return random.choice(files)

def trunc_rating(rating, places=1):
    """
    Truncates the wad ratings to a given number of decimal places.

    :param places: The number of decimal places to truncate to.

    """
    _rating = str(rating).split(".")
    _rating[1] = _rating[1][0:places]
    _rating = float(".".join(_rating))

    return _rating

def print_wad_info(wad_info):
    """
    Prints out the given wad info to the console, in a more readable way.

    :param wad_info: The wad info, in dict (JSON) form, to print.

    :returns: None.

    """
    for key in sorted(wad_info):
        if key != "textfile":
            print "%s: %s" % (key, wad_info[key])
        else:
            print
            print "Textfile: \n"
            print "".join(wad_info[key])
            print    

def open_url(wad_info):
    """
    Opens the page for the wad on the Doomworld idgames archive.

    :param wad_info: The wad info to extract the url from.

    :returns: None

    """
    webbrowser.open(wad_info["url"])

def open_id_list(filename=None):
    """    
    Opens a txt file of ID numbers.

    :param filename: The filename of the file to be opened.

    :returns: A list of the ID numbers.

    """
    if not filename:
        filename = raw_input("Filename: ")
        if filename == "":
            filename = "temp.txt"

    with open(filename, "r") as id_file:
        id_list = id_file.read()
        id_list = id_list.split(", ")
        id_list = [int(x) for x in id_list]
        # print id_list
    
    return id_list
    
def open_json(filename, zipped=True):
    """    
    Opens JSON data.

    :param filename: The filename of the file to be opened.
    :param zipped: Whether or not the file is gzipped.

    :returns: The JSON data.

    """
    if zipped:
        json_gzip = gzip.open(filename, 'rb')
        json_gzip = json.loads(json_gzip.read())
        return json_gzip
    else:
        with open(filename, "r") as json_file:
            return json.load(json_file)

def save_id_list(id_list, filename=None):
    """
    Saved a txt file of ID numbers.

    :param filename: The filename of the file to be saved.

    :returns: The closed file object.

    """
    if not filename:
        filename = raw_input("Filename: ")
        if filename == "":
            filename = "temp.txt"

    with open(filename, "w") as id_file:
        str_ids = [str(x) for x in id_list]
        id_file.write(", ".join(str_ids))
    
    return id_file

def save_json(data, filename, zipped=True):
    """
    Opens JSON data.

    :param filename: The filename of the file to be saved.
    :param zipped: Whether or not to gzip the data.

    :returns: The closed JSON file object.

    """
    if zipped:
        json_gzip = gzip.open(filename, 'wb')
        json_gzip.write(json.dumps(data))
        return json_gzip 
    else:
        with open(filename, "w") as json_file:
            return json.dump(data, json_file)

    return json_file

#===============================================================================
# If Main
#===============================================================================

if __name__ == '__main__':
    print "You're doing it wrong."