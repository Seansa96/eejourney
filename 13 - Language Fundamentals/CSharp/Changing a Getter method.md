Tags: [[csharp]] [[oop]]


A basic getter method may look like this: `public string Name { get => _name; //other stuff`

But, like the setter method, you can adjust this to grant more flexibility and functionality. All you need do is define it like you would any method, without using the lamba expression `=>`.

```
public string Name { get
{
	if (someBool) 
	{
		return _name + "is different."
	}
	else
	{
		return _name_
	}
}
}
```
