2025-04-22 09:59

Status: #baby

Tags: [[csharp]] [[dotnet]]

Part of the System.ComponentModel namespace. 

Implemented as `public interface INotifyPropertyChanged` typically.

Used to signal to listeners that a property within that object/class has changed. Either create an independent event handler, or utilize this. Do not do both.

Usage in a [[MVVM]] app might look like `public class ExampleClass : INotifyPropertyChanged`




## Reference:

https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanged?view=net-9.0