# File Manager API Reference

``` python
class mpf.core.file_manager.FileManager
```

Bases: `object`

Manages file interfaces.

## Methods & Attributes

The File Manager has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`static get_file_interface(filename)`

Return a file interface.

`classmethod init()`

Initialise file interfaces.

`static load(filename, verify_version=False, halt_on_error=True)`

Load a file by name.

`static locate_file(filename) → str`

Find a file location.
Parameters:	filename – Filename to locate

Returns: Location of file

`static save(filename, data)`

Save data to file.
