Tags: [[csharp]] [

Provides a [[Stream]] for a file, which support synchronous and asynchronous read/write operations.

Inherits from [[Stream]].

# Properties

`CanRead`
Gets a value that indicates whether the current stream supports reading.

`CanSeek`
Gets a value that indicates whether the current stream supports seeking.

`CanWrite`
Gets a value that indicates whether the current stream supports writing. Gets a value that indicates whether the current stream supports reading.

`IsAsync`
Gets a value that indicates whether the current stream was opened synchronously or asynchronously.

`Length`
Gets the length in bytes of the stream.

`Name`
Gets the path of the file opened in the FileStream

`SafeFileHandle`
The modern version of `Handle`. Gets an object representing the OS file handler for the current FileStream object.


# Example of usage

