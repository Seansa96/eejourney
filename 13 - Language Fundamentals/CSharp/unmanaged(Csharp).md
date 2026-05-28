Tags: [[csharp]] [[low-level]]

See also: [[managed(Csharp)]]

In the context of C#, this refers specifically to resources that the .NET runtime has no direct control over.  This would be things such as:

* File Handles
* Database Connections
* Websockets
* Windows
* Other OS-level handles
* File Descriptors, Streams, etc

The [[Garbage Collector]] for C# will handle the vast majority of memory (read: [[heap (memory)]]) allocation, with the [[compiler]] itself handling the [[stack]].  

