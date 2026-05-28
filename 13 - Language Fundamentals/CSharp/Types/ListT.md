Tags: [[heap (memory)|heap]] [[csharp]] [[mutable collection]]

A List\<T> object inherits from the [[IEnumerableT]] class. This is a dynamically resizable collection that comes with a variety of constructors, properties and methods and is useful when the size of a given collection may change during runtime or will not be known until then.  This incurs extra overhead however and requires the object to be placed on the heap. However, there are methods to ensure this is placed on the stack, but this also requires the `Capacity` property to remain fixed.

Resizing the `List` can be done with supported methods such as `TrimExcess` or defining the `Capacity` property explicitly, but this does require reallocating the array.  Adding items will also incur new re-allocations.  For performance, it is best to construct the `List` with a fixed size ahead of time, and trim the collection when it is not in active use.

# Declaring a new List

There are a variety of constructors, but the simplest way to create a List\<T> of dynamic size is:

`List<string> strings = new List<string>(); //this create a List that holds strings.`

# Properties

The two main properties of a List\<T> object are:

`List.Count` which returns the number of items within the collection, and

`List.Capacity`, which returns the number of items the collection can maximally hold.

# Common Constructors


# Main Methods

`Add(T item)` This allows you to append an item of the corresponding List's type to the end of the List. This operation re-allocates a new array internally if the `Capacity` is exceeded.  You may also pass an array or some other collection of the List's type in this method, and the overload takes in as many arguments as you desire to pass, so long as there is memory available.

`Remove(T item)`: Removes the first occurrence of a specific object from the List. This does not require a re-allocation, but does mean that the compiler must take the time to iterate over the collection to map the values to their proper positions in the array.

`Insert(int index, T Item)`: Inserts an element at the specified index.

`Find(Predicate<T>match)`: Searches for an element that matches the conditions defined by a specified predicate.

`Sort()`: Sorts the elements in the entire List.

`Clear()`: Removes all elements from the List.

`ToArray()`: Copies the elements of the List to a new array.

`IndexOf(T item)`: Returns the index of the first occurrence of an item in the List.