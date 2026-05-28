Tags:[[netsec]]

Pretty simple. The database file itself is encrypted at rest, and accesses to it require decryption to retrieve the desired data from a query.  

Individual tables within a database may also be selectively encrypted.

Record Level Encryption is the encryption of a row within a table. Column level encryption operates on the column within a row (like the SSN of a given customer).