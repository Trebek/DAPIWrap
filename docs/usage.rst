==============
DAPIWrap Usage
==============

This document demonstrates how to use the basic functions of DAPIWrap.

----------------

Getting Wad Info
================

Some examples of how to retrieve the info of a wad.

Get Wad Info Using ID
---------------------
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    daw = DAPIWrap()

    wad_info = daw.get_id(12815)

Get Wad Info Using Full Path & Filename
---------------------------------------
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    daw = DAPIWrap()

    wad_info = daw.get_file("levels/doom2/Ports/v-z/zdmcmp1.zip")

Get Wad Info Using Just a Filename
----------------------------------
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    daw = DAPIWrap()

    wad_info = daw.get_file_alt("zdmcmp1.zip")

----------------

Searching
=========

Some examples of how to use the search functions. Results are returned in a ``list``, unless ``"raw": True`` (``"raw": False`` by default), then the results are within a ``list``, within a ``dict`` (JSON), just as they are received from the API.

Search Parameters
-----------------

Search parameters should be packaged in a ``dict``, and can contain one of or each of the following parameters and values.

The default search parameters and values are:
::

    {
        "type": TYPE_FILE
        "sort": SORT_DATE
        "dir": DIRECT_ASC
        "filter": None
        "raw": False
    }

The values of each parameter are constants from ``dapiwconst``, but you could also use their string equivalents, which are often shorter (have less characters) actually. I just made global constants for them all so they were all consolidated, and easier for me to remember.

The other possible values for the parameters:

**type:**
::

    TYPE_AUTHOR = "author"
    TYPE_CREDITS = "credits"
    TYPE_DECRIP = "description"
    TYPE_EDITORS = "editors"
    TYPE_EMAIL = "email"
    TYPE_FILE = "filename"
    TYPE_TEXT = "textfile"
    TYPE_TITLE = "title"

**sort:**
::

    SORT_DATE = "date"
    SORT_FILE = "filename"
    SORT_RATING = "rating"
    SORT_SIZE = "size"

**dir:**
::

    DIRECT_ASC = "asc"
    DIRECT_DESC = "desc"

**filter:**
::

    FILTER_DATE = "filter:date"
    FILTER_GAME = "filter:game"
    FILTER_RATING = "filter:rating"
    FILTER_SIZE = "filter:size"
    FILTER_VOTES = "filter:votes"
    FILTER_YEAR = "filter:year"

Search Filters
--------------

Filters also require a value, packaged with them in a tuple/list. For example, if you wanted to filter by year, and you wanted all of the results from 1994, the value of ``filter`` would be:
::

    (FILTER_YEAR, 1994)

You can also apply a chain of filters by packaging each filter and value into a tuple or list, like so:
::

    ((FILTER_YEAR, 1994), (FILTER_GAME, DOOM))

That would filter out everything except Doom wads, from 1994.

A few of the filters will also accept a range as a value. Those filters are:
::

    FILTER_RATING
    FILTER_SIZE
    FILTER_VOTES
    FILTER_YEAR

You can specify a range (low to high), by packaging the range in a list/tuple like so:
::

    (FILTER_RATING, (3.0, 5.0))

Search Examples
---------------

Basic Search
^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    daw = DAPIWrap()

    results = daw.search("zdmcmp1")

Search with Parameters
^^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap
    from dapiwconst import (
        TYPE_AUTHOR,
        SORT_RATING,
        DIRECT_DESC
    )

    daw = DAPIWrap()

    results = daw.search(
        "BioHazard", 
        {
            "type": TYPE_AUTHOR,
            "sort": SORT_RATING,
            "dir": DIRECT_DESC
        }
    )

Search with Parameters & Filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap
    from dapiwconst import (
        TYPE_AUTHOR,
        SORT_RATING,
        DIRECT_DESC,
        FILTER_GAME,
        DOOM2
    )

    daw = DAPIWrap()

    results = daw.search(
        "BioHazard", 
        {
            "type": TYPE_AUTHOR,
            "sort": SORT_RATING,
            "dir": DIRECT_DESC,
            "filter": (FILTER_GAME, DOOM2)
        }
    )

----------------

Downloading
===========

Some examples of how to use the download functions. All download functions need to be provided with at least the wad id/filename/list of ids and the location of the directory to download to.

Servers
-------

There are a handful of servers you can choose from (the default is ``DL_FTP_GERMANY``), and all have a constant name in ``dapiwconst``. You can use their string equivalent, or just import the constant you need. The constants and string equivalents for the servers are:

**FTP:**
::

    DL_FTP_GERMANY = "ftp.fu-berlin.de"
    DL_FTP_GREECE = "ftp.ntua.gr"
    DL_FTP_TEXAS = "ftp.mancubus.net"

**HTTP:**
::

    DL_FLORIDA = "http://www.gamers.org/pub/"
    DL_GREECE = "http://ftp.ntua.gr/pub/vendors/"
    DL_NEWYORK = "http://youfailit.net/pub/"
    DL_TEXAS = "http://ftp.mancubus.net/pub/"

**Note:**

You probably don't want to run the following scripts without changing ``dl_folder`` (download folder) to a different location. But that's up to you.

Also, don't abuse the download functions. Don't hammer the servers, or download every wad in the archives in a day. If you plan on doing something like that, at least do it slowly, maybe over a period of many days, and maybe rotate servers. I didn't write this wrapper to crash anyone's servers.

Download Examples
-----------------

A few short example scripts, demonstrating how to use the download functions.

Download Wad Using ID
^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    dl_folder = "C:\\games\\doom\\wads\\"

    daw = DAPIWrap()

    daw.download.wad_id(12815, dl_folder)

Download a Wad, Using a Full Path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    dl_folder = "C:\\games\\doom\\wads\\"

    daw = DAPIWrap()

    daw.download.file_path("levels/doom2/Ports/v-z/zdmcmp1.zip", dl_folder)

Download Wad Using Wad Info
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``wad_info`` is just a ``search`` result, or the result of ``get_id``, or any other similar functions that return wad info in ``dict`` (JSON) form.
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    dl_folder = "C:\\games\\doom\\wads\\"

    daw = DAPIWrap()

    results = daw.search("doom")

    wad_info = results[0]

    daw.download.wad_info(wad_info, dl_folder)

Download List of Wad IDs
^^^^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    dl_folder = "C:\\games\\doom\\wads\\"

    daw = DAPIWrap()

    id_list = [12815, 12021, 16429]

    daw.download.id_list(id_list, dl_folder)

Download from a Specified Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap
    from dapiwconst import DL_FLORIDA

    dl_folder = "C:\\games\\doom\\wads\\"

    daw = DAPIWrap()

    daw.download.wad_id(12815, dl_folder, DL_FLORIDA)

----------------

Typical responses
=================

Getting wad info
----------------

Getting a specific wad's full info, using an ID or filename, typically returns a response like this (this is just an example):
::

    {
        u'age': 832402800,
        u'author': u'Some Dude',
        u'base': u'New level from scratch',
        u'bugs': u'No',
        u'buildtime': u'1 hour',
        u'credits': u'iD Software',
        u'date': u'2014-01-01',
        u'description': u'This is a brief description of the wad.',
        u'dir': u'levels/doom2/s-u/',
        u'editors': u'Doom Builder 2',
        u'email': u'SomeDude@someemail.com',
        u'filename': u'test.zip',
        u'id': 12815,
        u'idgamesurl': u'idgames://levels/doom2/s-u/test.zip',
        u'rating': 5.0,
        u'reviews': {u'review': [{u'text': u'cool map', u'vote': 5}]},
        u'size': 67005,
        u'textfile': u"The entirety of the wad's text file would be here.",
        u'title': u'Test',
        u'url': u'http://www.doomworld.com/idgames/?file=levels/doom2/s-u/test.zip',
        u'votes': 2
     }

Or ``None``, if no wad was found.

Searching
---------

A search will yield a list of more brief info for each wad found, like so (this is just an example):
::

    [
        {
            u'age': 832402800,
            u'author': u'Some Dude',
            u'date': u'2014-01-01',
            u'description': u'This is a brief description of the wad.',
            u'dir': u'levels/doom2/s-u/',
            u'email': u'SomeDude@someemail.com',
            u'filename': u'test.zip',
            u'id': 12021,
            u'idgamesurl': u'idgames://levels/doom2/s-u/test.zip',
            u'rating': 5.0,
            u'size': 67005,
            u'title': u'Test',
            u'url': u'http://www.doomworld.com/idgames/?file=levels/doom2/s-u/test.zip',
            u'votes': 2
        },
        {
            u'age': 865432674,
            u'author': u'Another Guy',
            u'date': u'2014-02-02',
            u'description': u'This is a brief description of the wad.',
            u'dir': u'levels/doom2/a-c/',
            u'email': u'SomeDude@someemail.com',
            u'filename': u'anotherwad.zip',
            u'id': 13024,
            u'idgamesurl': u'idgames://levels/doom2/a-c/anotherwad.zip',
            u'rating': 4.8,
            u'size': 76050,
            u'title': u'Another Wad',
            u'url': u'http://www.doomworld.com/idgames/?file=levels/doom2/s-u/anotherwad.zip',
            u'votes': 1
        },
    ]

Or ``[]`` (empty ``list``), if no wads were found.

Downloading
-----------

At the moment, downloading, if through an HTTP server, returns the downloaded zip file object. If you're downloading from an FTP server, the function returns a string, with the `FTP return code`_. I'm going to have to figure out a better system.

.. _Doomworld \/idgames archive: http://www.doomworld.com/idgames/
.. _Doomworld \/idgames archive API: http://www.doomworld.com/idgames/api/
.. _PIP: https://pypi.python.org/pypi/pip/
.. _FTP return code: http://en.wikipedia.org/wiki/List_of_FTP_server_return_codes