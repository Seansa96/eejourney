2024-08-09 14:59

Status: #child

Tags: [[http]] [[webdev]] [[protocols]]

# cookies

This is just a small piece of data typically sent by the server to the user's browser.  Because http is a stateless protocol (and thus each connection lacks information of each client's state), cookies allow for the creation of a pseudo-session, enabling things like a simple cart on an e-commerce site.  Thus, a cookie can allow a browser to store data and info about the client making the request, while also giving the server more flexibility without necessarily introducing a significant amount of overhead into each request/response transaction.

Essentially, the main goal of a cookie (for developers, at least), is to provide a personalized experience (aka, a session) for each user/client.

#### Here's an example of the basic process for exchanging cookies:

![[cookie-basic-example.png]]

#### Creating a cookie

You do this very simply by sending back an HTTP header in the HTTP response called `Set-Cookie`. Then, simply define whatever is relevant to your purposes.  There are some base attributes that you can define for the cookie provided by the HTTP Standard, however.

###### Expires and Max-Age
Expires is a relative time definition, and is generally discouraged since it can cause mismatches between the client and server (if the client believes the cookie to expire at some epoch, while that same epoch is plus or minus 3 hours from the server's time zone, for instance).  Max-Age is generally more utilized, as it simply states how long from session creation the cookie may live.  As long as this is treated much like TTL, where both parties track its state throughout transactions, it is relatively secure. **Important to note Max-Age has precedence when both are set.**

Cookies without these attributes are deleted when the session ends.  This is to prevent against an attacker using an old session to access data they should not have authorization for.  Because the browser may delete the cookie in such an event, it is important for there to be a sufficiently robust session termination/regeneration scheme installed server-side.

Say that a user may initiate a session, leave their machine, then return and close the tab and engage in other business. After a few minutes, for some unknown reason they return to that page. 

For convenience sake, the server may allow a grace period of some time (2-5 minutes is a period that does not compromise security too greatly), allowing for the previous session's cookies to be regenerated while instantiating a new session (by creating a new session ID). Other various time metadata may be kept for further refinement of such a mechanic (time last accessed and whatnot), but it is important that if the user does not consent to a longer period of tracking, that they may still engage in a fresh session to keep cookies as secure as possible.

###### Security flags for cookies
It is common practice to use the `Secure` and `HttpOnly` flags for cookies to prevent against [[Cross-Site Scripting]] and Man-in-the-middle attacks.  `Secure` requires that the cookie be sent only over https (making it **resistant**, not immune), and `HttpOnly` prevents Javascript from acting upon the cookie.  

Without this, one could use Javascript to access the contents of a cookie with something as simple as:

`console.log(Document.cookie);`
Other notable tags include `SameSite=<samesite-value>`, where one may use `Strict`, `Lax`, or `None`.

`Strict` will only send the cookie on same-site requests, no exceptions.

`Lax` will send them only for same-site requests unless a link is followed. This is the default behavior if no `SameSite` attribute is set.

`None` is pretty self-explanatory. Allows for same and different site requests. Has to be accompanied by the `Secure` flag or else it will generate an error.

And `Path=/path/to/dir`, which specifies a part of the URL that must be present for the cookie to be sent by the browser.
## Reference:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies