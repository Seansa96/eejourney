Tags: [[lua]] [[control flow statement]]

`for k, v in pairs() do`
`end`

LUA revolves fundamentally around manipulation of tables, which are not sequentially ordered structures. Thus, the iterative control flow statement typically used is similarly modeled after this quirk of the language.

It is thus that, due to the lack of enumeration, one typically uses the `pairs` function for the control flow, placing in the table to traverse as an argument.  Because these tables are not inherently enumerated, the order in which the data may be retrieved is not guaranteed, as it is a hashed structure.

However, LUA does support a more organized way of traversing the table, should that be required, with the `ipairs` function.  This takes in a table and uses it as an index with which to guide the expressions and statements contained within the main body of the for loop.

So, one might declare something like:

```
local counter = { 2000, 2005, 2010, 2015}

for key, value in ipairs(counter), do
print(key .. ": " .. value)
end
```

And instead of it printing possibly: 

2010, 2005, 2000, 2015

It will reliably print out:

2000, 2005, 2010, 2015