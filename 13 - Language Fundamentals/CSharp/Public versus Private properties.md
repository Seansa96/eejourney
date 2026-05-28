Tags: [[csharp]] [[oop]]


For properties, you generally only need to make a property private if you want full control over its definition and use. If you're just setting it to a default state like

`public string Foo { get; set;}`

There is no need to make a private variable such as `private string _foo`, as these achieve the same thing, and one just takes more code.  After all, you are still directly accessing the property when you do `obj.Foo = "notfoo"`.