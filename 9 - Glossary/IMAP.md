Tags: [[email]] [[protocols]]

Port number is 143 (non-secure)
IMAPS port number is 993 (secure/encrypted)

IMAP (Internet Message Access Protocol) allows you to manipulate and access messages on the e-mail server.

The request type format is very similar to [[HTTP Protocol (History and Versions)]], with various request types such as:

`FETCH`
`STORE`
`COPY
APPEND
EXPUNGE
SEARCH`

IMAP *does* return the full message body to the requesting client.  Typically this is in MIME format with the raw byte data, and needs to be decoded according to the specified character set (such as [[UTF-8 Encoding]]).

However, usually this is done by the protocol/client itself so that's simply a matter of abstraction in the actual pipeline itself.

While the raw data is indeed returned and theoretically able to be manipulated in any context, the protocol itself does not manage the data itself, just the state. A client would need to implement caching/download to store that data client side.

This is why typically, IMAP is designed around simply viewing the data on the e-mail server itself (which it does by first asking the client/user for their credentials, logging them in, and having them select an `INBOX`).  They then get an associated command tag (much like a shell) that they issue commands from.

Admins can and typically do disable the ability to do so by forcing users to view their messages in a web interface, in which the rendered HTML is the only way to view the content and is non-trivial for most users to bypass, but even in this case, the HTML can be accessed and thus the message content can be extracted.

In this way, IMAP is able to serve simultaneous devices and clients, as each transaction is ephemeral and clearly defined.


