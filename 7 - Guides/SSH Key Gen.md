2024-08-14 17:17

Status: #child

Tags: [[guide]] [[ssh]]



## SSH Key Gen

SSH requires a public key and a private key and the authentication is considered asymmetric encryption.  The client needs both the public and private key while the server just needs the public key at some point.

##### Connecting:
To connect, you just do:
`ssh -i "/path/to/key" user@server`, where the server may be the domain name or the IP address. (Works on Linux+Windows)


##### ssh-copy-id
Of course, as per the protocol, the public key needs to be present on the host you're connecting to. You can easily do this with `ssh-copy-id user@remotehost`. (Works on Linux+Windows)

##### ssh-keygen
For generating a key pair, you can do `ssh-keygen -t ed25519`. You can add `-C "user@example.com` to add some metadata as a comment. RSA is generally fine too. (Works on Linux+Windows).







## References:
