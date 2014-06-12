================
DAPIWrap Changes
================

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