================
DAPIWrap Changes
================

v0.3.0 (15-06-2014)
-------------------

- Consolidated the loose functions, in ``dapiwtools`` into a couple of separate classes.
    - Added the ``IOFuncs`` class, which has the methods ``open_id_list``, ``open_json``, ``save_id_list``, and ``save_json``, for saving/opening wad id lists, and JSON data (raw, or gzipped). These functions can be accessed through a ``DAPIWrap`` instance by using ``DAPIWrap.io.<method>``, where "<method>" is the chosen method.
    - Added the ``MiscFuncs`` class, which just has some miscellaneous methods, such as ``random_wad``, ``print_wad_info``, and ``open_url``. These can be accessed through a ``DAPIWrap`` instance by using ``DAPIWrap.misc.<method>``, where "<method>" is the chosen method.
        - Changed ``random_wad``, so that now you have to provide it with an idgames archive path, or list of paths, to retrieve a random wad from. If provided a list of paths, it will pick one random path, and get a random wad from there.
- Added the method ``search_local`` to ``DAPIWrap``, for searching a given list of wad info items.
    - I added this because, apparently, the Doomworld API only returns the first 100 results when searching. However, if you know the directory you want to search in, you can retrieve a ``list`` of the entire contents of a given directory, with ``DAPIWrap.get_files``, and then search through them, by feeding the ``list`` into ``DAPIWrap.search_local``, along with a search query, and any optional parameters. It works just like ``DAPIWrap.search``, except you also feed it a list of info to search through.
    - Note though, that if you are feeding ``DAPIWrap.search_local`` a list of items retrieved by ``DAPIWrap.search`` or ``DAPIWrap.get_files``, that you can't search the credits, editors, or text files of the items, because those areas are not included in the results of those actions. They only return a brief version of each wad's info, missing those sections.
- Changed the way the ``newdir`` argument works, for the download methods in the ``Downwad`` class, in ``dapiwtools``. 
    - Was set up to create, and download files to a new directory of the same name as the file, if ``newdir=True``. Didn't have anything to do with whether or not the download path you were providing was a new directory. Not really the behaviour you would expect, I don't think. I had it set up that way for my own purposes. Now the ``newdir`` argument simply specifies whether or not you want ``DAPIWrap`` to create a new directory, if the given download path doesn't exist. If ``newdir=False``, and the download path you specify doesn't exist, Python will throw an ``IOError`` exception. By default, ``newdir=True``.
    - Downloading from an FTP server now returns the closed file object, the same way downloading from an HTTP server does.
- Fixed a misspelling in dapiwconst.
- Fixed a few errors in the documentation.

v0.2.0 (11-06-2014)
-------------------

- Got rid of some broken methods. 
    - The methods ``DAPIWrap.get_file_alt``, in ``dapiwrap``, & ``Downwad.filename``, in ``dapiwtools``, didn't really work, because multiple files, in different directories, can have the same filename. Since this method relied on searching to find the file with the given filename, it would often return multiple results, and the only way of knowing which was the right file, was to query the user through the console. I didn't like that.
- Added a few more functions to ``dapiwtools``.
    - Added ``open_id_list`` & ``save_id_list`` for saving/loading a txt file of wad IDs.
        - Can be used to compile a list of IDs, for storing/sharing, that can be opened and fed into ``DAPIWrap.get_id_list`` or ``DAPIWrap.download.id_list``
    - Added ``open_json`` & ``save_json``, for dumping/loading JSON data, either as raw JSON data, or gzipped.
        - Could be used to store retrieved wad data locally.
    - Added ``open_url`` to open the Doomworld archive page of a wad in your default browser.
- Changed the method name ``DAPIWrap.get_file``, in ``dapiwrap``, to ``DAPIWrap.get_file_path``. Was too similar to ``DAPIWrap.get_files``.
- Cleaned up ``dapiwconst``, and removed a number of useless constants, and added some useful ones.
- Removed some unused imports from ``dapiwconst``, in ``dapiwrap`` & ``dapiwtools``.

v0.1.0 (07-06-2014)
-------------------

- Initial release.