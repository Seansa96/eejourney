In the typical "Hello World" example, the simple program:

```
#include <iostream>

int main()
{
	std::cout << "Hello world!";
	return 0;
}
```

the `std` part is called the **namespace**, much like from C#. It just means it's a collection of code with a similar purpose or from a single vendor.  

In the case of the above, this means that the `cout` stream object lives in the `std` namespace. And it is accessed by using the [[Scope Resolution Operator]], `::`. 

