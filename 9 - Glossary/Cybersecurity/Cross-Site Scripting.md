2024-08-12 04:49

Status: #baby

Tags: [[netsec]] [[hacking]]

# Cross-Site Scripting

Cross-Site Scripting, (or XSS) refers to an attack made through usage of some scripting language injected into the HTML of a website.  This can be done in several ways: through some input field, through the request URI, or even through the HTTP Request itself (POST and GET).

Primarily, Javascript is the language of choice for such attacks as it has so many native hooks into HTML and CSS, but it can be done through many others (such as CSS itself).

The method of defense against XSS is typically input sanitization and validation, Content Security Policies, and in-general avoiding direct user input wherever possible.


## Reference:
