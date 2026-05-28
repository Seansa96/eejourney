Tags: [[csharp]]

This class provides methods (static in nature) for basic to intermediate file operations. These include creation, copying, deletion, moving, and opening of a single file and enables the creation of [[FileStream]] objects.

Thus, a `File` class method may be accessed as:

```
File.SomeMethod();
```

# Common Methods

`File.Open(string path, System.IO.FileMode mode, System.IO.FileAccess access, System.IO.FilesShare share);`

Opens a [[FileStream]] on the specified path.
**Arguments:**
1. Path, of type `string`. Self-evident. Relative or Absolute is supported.
2. An enum `mode`, with constant values from 1 to 6, representing different states. Further elaboration can be found at [[FileMode]]. Relevant values for the purpose of this method are 1 (`CreateNew`), 2: (`Create`), 3: (`Open`), 4: (`OpenOrCreate`), 5: (`Truncate`, unlikely to be used except in scenarios which memory or fresh objects are of necessity), 6: (`Append`).
3. An enum `access` that specifies valid operations to be performed, usually the standard affair (`read`, `write`, execute, or some combination thereof).
4. An enum `share`. This specifies access other threads have to the file. (Needs further clarification).


`File.Move(string sourceName, string destName);`

Moves a specified file (defined by the path string in the first argument) to a new location. Will default to using the sourceName for the destination if none are provided.

An overload is available for this method where a boolean may be supplied to overwrite a file of the same name at the destination if it already exists.  


`File.GetCreationTimeUtc();


`File.GetLastAccessTime();
`File.GetLastWriteTime();
`File.OpenHandle();
`File.ReadAllText();`