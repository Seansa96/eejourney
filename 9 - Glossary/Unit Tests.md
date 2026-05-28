Tags: [[Test Driven Development]]

Unit tests are simply automated tests that serve as the foundation of [[Test Driven Development (TDD)]].

These are built by the developer with a specific goal in mind.  They are then refactored until they successfully achieve that goal, and they often clearly demonstrate what the purpose of a given piece of logic is supposed to accomplish.

Simple example in [[csharp]]:

```
[Fact]
public void AddTwoNumbers()
{
	int a = 2, b = 3;
	int result = a + b;
	Assert.Equals(5, result);
}
```

In C#, for a simple  method like this you need to declare it as a Fact property, and since Fact properties don't take in parameters, you just define custom ones within the test. It's fine that the numbers are hardcoded--the point of most unit tests is not to deal with user inputs (there are tests that do this however, as this is obviously quite useful.)

Assert.Equals takes in the value the function should produce, and the actual result of the logic implemented and compares them, returning true and thus passing the test. Most of the Assert class functions this way.