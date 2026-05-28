Tags: [[oop]]

Getter and Setter methods are special methods of a class specifically to retrieve the values of private fields.  Because these fields are not available to other classes and parts of the program, there needs to be some way for these fields to be able to interact with them.

These methods are generally made available in the corresponding Properties for these private variables.  The compiler is able to recognize when a Getter or Setter is invoked by specific keywords in each language.  An example would be something like

`private string name = ""`
`public string Name {get ; set ; }`

In the main program function, you can then simply do:

`obj.Name = "Sean"`

And because of the assignment operator, it will know to invoke the setter method. When you attempt to simply pass `obj.Name`, then it will know it should simply invoke the getter method.