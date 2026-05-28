2024-09-05 22:53

Status: #baby

Tags: [[html]] [[webdev]] 

# Links in HTML Documents

A link is actually known as a *hyperlink*, a feature available in HTML to create a rich and interactive hypertext construct.  This is just one connection from one resource to another. It may be as simple as a link to something else within the same resource, or a link to another resource.

A link is made of two components, an *anchor* and a *destination*. The anchor is simply the source and the actual entity a user may interact with (an example being the article linked to under the Reference heading), and the destination being any Web resource.

#### Example:

```
<BODY>
_...some text..._
<P>You'll find a lot more in  <A href="chapter2.html">chapter two</A>. 
See also this <A href="../images/forest.gif">map of the enchanted forest.</A>
</BODY>
```
The typical practice is to implement an anchor tag to the, well, [[anchor]], and use the [[href]] attribute to set the destination that it should take the user to, as you can see above.

## Reference:
https://www.w3.org/TR/html401/struct/links.html