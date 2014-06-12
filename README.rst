===============================
DAPIWrap: Doomworld API Wrapper
===============================

**This package is still in the beta stages, so expect updates that may break things, if you're using it.**

DAPIWrap is a fairly simple Python wrapper for the `Doomworld /idgames archive API`_. In addition to allowing you to access the API using Python, it also has a few added features, located in ``dapiwtools``, that aren't provided by the API, such as search filtering, and downloading functions, for downloading wads from the supported mirrors on the `Doomworld /idgames archive`_.

Install/Uninstall with PIP_
===========================

Install
-------
::

    pip install https://github.com/Trebek/DAPIWrap/archive/master.zip

Uninstall
---------
::

    pip uninstall dapiwrap

Basic Usage
===========

These are some brief examples of how to use the functions of DAPIWrap.

Getting Wad Info
----------------

Get Wad Info Using ID
^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    daw = DAPIWrap()

    wad_info = daw.get_id(12815)

Get Wad Info Using Full Path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    daw = DAPIWrap()

    wad_info = daw.get_file("levels/doom2/Ports/v-z/zdmcmp1.zip")

Searching
---------

Basic Search
^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    daw = DAPIWrap()

    results = daw.search("zdmcmp1")

Search with Parameters & Filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    #!/usr/bin/env python

    from dapiwrap import DAPIWrap

    daw = DAPIWrap()

    params = {
        "type": TYPE_TITLE,
        "sort": SORT_RATING,
        "dir": DIRECT_DESC,
        "filter": (FILTER_YEAR, 1995)
    }

    results = daw.search("test", params)

Downloading
-----------

Download a Wad, Using it's ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

Typical Responses
=================

Getting Wad Info
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