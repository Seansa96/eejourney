Tags: [[netsec]]

Encryption in which a public key is exchanged while both members of the exchange have their own private key.  Common Algorithms involved include [[RSA]], [[Diffie-Hellman]], and [[Elliptic Curve Cryptography]].

The recipient's public key is used to encrypt the message, while the private key of the sender is used to sign the message to provide [[nonrepudiation]].  The private key of the recipient is required to decrypt that message, which is why the public key of the recipient is used to encrypt it.

Example:

Johnny wants to send a message to Clair. He asks for Clair's public key to encrypt the message, and signs it with his private key to provide non-repudiation. He sends the message.

Clair receives the message and decrypts it with her private key. She can provide proof that Johnny was the entity who sent her the message due to the signature on the message.

Any interested party who intercepts that message in the interrim cannot realistically crack the message due to lacking the private key of Clair.



