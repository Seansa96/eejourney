Tags: [[csharp]]

The `using` statement ensures the correct (aka opening, closing and disposing of) an [[IDisposable]] instance.

This is particularly useful in cases where we need the function of a class/method for one use.

# Example

The following is such a case.

```
var numbers = new List<int>();
using (StreamReader reader = File.OpenText("numbers.txt"))
{
    string line;
    while ((line = reader.ReadLine()) is not null)
    {
        if (int.TryParse(line, out int number))
        {
            numbers.Add(number);
        }
    }
}
```

This opens a file, tries to parse the line content to an int, if it's successful, it makes a local int `number`.  Then, it will call the `Add` method, which just appends that number to the `List<int>`. 

Again, note how we only need the `StreamReader`'s `ReadLine` method, and nothing else. Because of this, it doesn't make a great deal of sense to instantiate an entire object and have to manage it ourselves when we can let the compiler do so for us.

In the effort to be more specific, when control leaves the `using` block, that is when the `IDisposable` is disposed of.  

# Asynchronous using

We use `await` to utilize an [[IAsyncDisposable]] instance.  

# Without Braces

You can utilize `using` declarations without braces to keep things terse. Note that the scope of any variables created by `using` is contained within it, and any variables created in this way are thus treated as readonly and cannot be passed by reference or as an `out` parameter.  In regard to a brace-less declaration, the scope is terminated at the end of the associated method call, typically.

So, something such as

`using StreamReader reader = File.OpenText(FilePath);`

The `reader` variable of type `StreamReader` cannot be further re-assigned or passed. However, calling methods from it like `ReadLine()` is legal as this is functionally similar to a static method.

We can do an atomic operation such as this and not need to manually clean up after ourselves, the benefits of which are immediately useful.

