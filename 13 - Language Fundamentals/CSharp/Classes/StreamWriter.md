Tags: [[csharp]] 
See also: [[StreamReader]]

This is a class that inherits from the [[TextWriter]] class for use in writing characters to a stream in a particular encoding. The default encoding utilized, when not specified in the constructor or through use of overloads, is [[UTF-8 Encoding]].

This is the recommended class for basic, non-performant writing operations (for text files) by Microsoft. Note that `StreamWriter` is designed for character output in a particular encoding, whereas [[Stream]] objects are designed for byte input and output.

# Basic Constructor

`StreamWriter(String FileName)`
Uses the default encoding and buffer size for the passed file.

`StreamWriter(String FileName, Boolean FileExists, Encoding Type)`
Uses the default buffer size, the passed encoding type, and if the file exists, then whether it should be overwritten or appended, and if it does not, this will create a new file.

`StreamWriter(Stream, Encoding)`
Uses the passed [[Stream]] and encoding type to write to.

# Example Usage


```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace StreamReadWrite
{
    class Program
    {
        static void Main()
        {
        string FileName = "testfile.txt";
        using (var fs = new FileStream(FileName, FileMode.Write)
        {
	        using StreamWriter writer = new StreamWriter(fs);
	        writer.WriteLine("This is new input.");
        }
        }   
    }
}
```

# Properties

`AutoFlush`: Gets or sets a value indicating whether the `StreamWriter` will flush its buffer to the underlying stream after every call to the `Write(Char)` method.

`BaseStream`: Gets the underlying stream object that interfaces with a backing store.

`Encoding`: Gets the encoding type in which the output is written.

`FormatProvider`: Gets an object that controls formatting.

`NewLine`: Gets or sets the line terminator string used by the current [[TextWriter]].

# Main Methods

`Close()`: Closes the current `StreamWriter` object and the underlying stream. Should be run after usage of the `StreamWriter` object is finished, when a whole instance has been created that persists beyond the current scope. This automatically passes `true` to the underlying `Dispose()` method, releasing both [[managed(Csharp)|managed]] and [[unmanaged(Csharp)|unmanaged]] resources.

`Dispose()`: Releases all resources used by [[TextWriter]] object, that being the [[unmanaged(Csharp)|unmanaged resources]]. A boolean may be passed optionally to release the [[managed(Csharp)|managed]] resources as well.

`Write()`: A method that writes data to the stream. There are many overloads for this method

`Write(char[] buffer, int index, int count)`
This takes in a buffer containing the data to write, a value indicating where in the buffer to begin writing from, and a value specifying how many characters to write.

Typically, you might do something like: `Write(buffer, 0, buffer.Length)`

`Write(char?[] buffer)`: Similar implementation as above, but assumes default values and just writes until until the value of the current buffer index is null or the end of stream has been reached.

`Write(char value)`: Writes a character to the stream.

`WriteLine(String input)`: Writes a string to the stream, followed by a line terminator. If the string is empty, then just writes the line terminator.