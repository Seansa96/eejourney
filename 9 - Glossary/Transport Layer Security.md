Tags: [[protocols]] [[http]]

The Transport Layer Security protocol (sometimes referred to by its predecessor, SSL or Secure Socket Layer), is a communications protocol used in most secure applications that run over various mediums (email, Instant messaging, Voice over IP, and of course, the internet via HTTPS).

It works through asymmetric encryption and has a defined structure flow referred to as the **Handshake**.

1. ClientHello - Client sends a suggested TLS version, the ciphers it supports, a random number, a optionally a server ID or Server Name Indication.
2. ServerHello - Server sends back the selected TLS version and cipher, the server certificate (usually x.509) and a new random number.
3. Key Exchange Phase - Client validates the certification, uses the cipher selected to encrypt a pre-master secret with the server's public key, then sends it
4. Session Key Generation - Both sides resolve the shared session key from the pre-master secret and the random numbers from Steps 1 and 2.
5. Both parties send a **Finished** message encrypted with the session key to confirm the tunnel has been established correctly.