Tags: [[oop]] [[csharp]][[java]]

Constructors are special methods within a class that are called when an instance of the class is created.  They typically set the initial attributes of that instance of an object, but do not themselves return any values.  In most OOP languages, the `new` keyword will automatically invoke the most appropriate constructor within the class it operates on.

A constructor method must have the same name as the class itself, and it is acceptable to have multiple constructors (called constructor overloading).  ^overloading


A Constructor may also take no arguments, which is referred to as a Default Constructor. This allows the developer to first create the object before injecting attributes into it. This can be useful in situations where the object must be created before any assignments can be made (such as simple validation like checking if the object exists).
