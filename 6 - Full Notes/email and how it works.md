2025-02-19 02:25

Status: #baby

Tags: [[networking]] [[email]] [[low-level]]

# email and how it works

Like all software (well, at least how most are designed), there's a client-server relationship.

However, e-mail is a bit more involved, as it requires an MX record from a domain registrar. Obviously, registrars are public as well as private, so this means you can have internal e-mail as well as public, internet-facing e-mail.

It's managed by the various e-mail protocols, mainly [[POP]] and [[IMAP]], with SMTP being used to actually send the email.

Also, nowadays for non-repudiation and authentication, SPF, DMARC, and DKIM are required as additional DNS records for your domain to be propagated and not rejected as spam, generally speaking.

It is difficult to do public, internet-facing self hosted e-mail servers, as not only is this potentially a large amount of traffic and storage required, but most e-mail servers need to go through rigorous validation which typically is also quite expensive.

Free 3rd party solutions like Zoho, Google Workspace, and so on offer e-mail hosting, so that you can register your domain with them by providing your DNS records and having them propagate and validate them.



## Reference:
