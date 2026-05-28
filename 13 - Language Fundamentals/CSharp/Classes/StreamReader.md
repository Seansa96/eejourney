Tags: [[csharp]]
See also: [[StreamWriter]]


This is a class that inherits from the [[TextReader]] class to read characters from a byte stream in a particular encoding. By default, without use of overloads, the base constructor will default to [[UTF-8 Encoding]].

This is the class specifically outlined by Microsoft for reading lines of information from a text file.

# Basic Constructor

`StreamReader(String FileName, Boolean ByteOrderMarkDetection)
`StreamReader(Stream, Encoding Type, Boolean ByteOrderMarkDetection`

# Example Usage

```
class Example
{
	static async Task Main()
	{
		await ReadAndDisplayFilesAsync()
	}
static async Task ReadAndDisplayFilesAsync()
{
	String filename = "testfile.txt";
	Char[] buffer;

	using (var sr = new StreamReader(filename));
	{
		buffer = new Char[(int)sr.BaseStream.Length];
		await sr.ReadAsync(buffer, 0, (int)sr.BaseStream.Length);
	}
}
	Console.WriteLine(new String(buffer));
}
```

# Main Properties

`BaseStream`: `public virtual System.Io.Stream BaseStream` `{ get; }`. Simply returns the underlying stream. The class as a whole utilizes an internal buffer when translating between the [[Stream]] object and `StreamReader` itself.  Use this when precision is necessary.

`CurrentEncoding`: `public virtual Sysem.Text.Encoding CurrentEncoding { get; }`. Simply returns the current character encoding used by that instance of `StreamReader`.  Note that encoding detection is not done until *after* a `Read` method call.

`EndOfStream`: `public bool EndOfStream { get; }`. Returns a bool indicating if the underlying stream position is at the end of that stream. `true` if so, `false` otherwise.  When accessed, this property issues a synchronous `Read` on the underlying `Stream`.

# Main Methods

`Close()`: An [[override]] of the underlying `Dispose` method inherited from [[TextReader]].  Uses an [[Constructor Methods#^overloading|Overload]] that passes `true` automatically. This will close the `StreamReader` object and the underlying [[Stream]] as well as both [[managed(Csharp)|managed]] and [[unmanaged(Csharp)|unmanaged]] resources.

`Dispose()`: Closes the underlying [[Stream]], releasing the [[unmanaged(Csharp)]] resources associated with it. Optionally, a boolean may be passed to release the [[managed(Csharp)|managed resources]].

`DiscardBufferedData()`: This method will flush the contents of the internal buffer and sync it to that of the underlying [[Stream]].  This is useful (and necessary) when reading from the same file more than once, such as if you're printing specific portions of it at a time.  Without this call, the internal buffer is not reset, and so successive `Read` calls will include the contents of the buffer as well as whatever the underlying `Stream` reads.

`Peek()`: Returns an integer value signifying the state of the next character to be read. Returns `-1` once the end of the file stream has been reached or until no characters can be read. This *does not* consume the characters, as in, it does not move the position of the [[FileStream]] object used by `StreamReader`.  The Int returned is the value of the current index of the underlying buffer, which is a character code. As mentioned, again, this does not consume the character, so a read call must be made to advance the position of the buffer index.

`Read()`: This will read the next character from the input stream and advance the underlying character position by one character. This returns an Int32 value representing that character's ASCII value. Two overloads exist that see frequent use. `Read(Span<char>)`, which reads the characters from the current stream into a [[SpanT|Span]] of type Char, and returns an Int32 of how many characters have been read, or 0 if at the end of the stream and no data was read. This number should be less than or equal to the buffer length.

`ReadAsync()`:

`ReadLine()`: This reads a line of characters from the current stream and returns the data as a string, or null if the end of the input stream is reached.

`ReadToEnd()`: Reads all characters from the current position to the end of the stream. Returns the rest of the stream as a string, from the current position to the end. If the current position is the end of the stream, it'll return an empty string, ("").
