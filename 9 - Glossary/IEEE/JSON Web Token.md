Tags: [[webdev]] [[netsec]] 

Also called a **JWT**, this is a stateless token supported by asymmetric encryption to transform transactions from exchange of raw data into tokens representing actions.

JWTs rely on "**Claims**", which are assertions made that represent an action or state.  For example, a server could generate a token which represents "logged in as admin", and the user can then provide that token to perform actions or access routes that require admin authorization.

JWTs are typically sent as HTTP-only cookies, preventing [[Cross-Site Scripting]] attacks upon them or general scripting inspection.

They can also be used in the case of third party APIS or unattended processes where a client needs to make calls to a service. In this case, they can use a POST request to access some resource and have an access token generated if they provide a valid JWT assertion, which requires a pre-shared secret from the server.

Example Access Token:

```
{
"access_token": "somelongstrofencodedtext",
"token_type": "Bearer",
"expires_in": 3600
}
```

The client would then pass this token in each call to a service in the Authorization header of their HTTP request using the Bearer schema. 

It is important to note that despite resembling a session in many ways, it only attempts to emulate one and nothing about these exchanges are preserved.  This also means that tokens can be forged through suggestive attacks which resemble a valid JWT, unless a record of currently active tokens is kept, although this defeats the purpose of the JWT.

# Structure

The structure of a JWT is:

**Header**
	**Payload**
		**Signature**

The header contains the algorithm used to generate the signature and the standard for the token. These are represented by `alg` and `type`.

Example Header :

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Payload**

The payload of a JWT contains the claims to be asserted. These can be custom or any of the standard claims defined in the documentation, of which there are 7.

Example Payload:

```
"loggedInAs": "admin",
"iat": 1427872305
```

**Signature**

This is the encoding of the header and payload in base64 separated by a period. This concatenated string is then run through the algorithm specified to produce the signature.
# Standard Claims

| Code                  | Name            | Description                                                                                                                                                                                                                                                                                                                                                    |
| --------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard claim fields |                 | The internet drafts define the following standard fields ("claims") that can be used inside a JWT claim set.                                                                                                                                                                                                                                                   |
| `iss`                 | Issuer          | Identifies principal that issued the JWT.                                                                                                                                                                                                                                                                                                                      |
| `sub`                 | Subject         | Identifies the subject of the JWT.                                                                                                                                                                                                                                                                                                                             |
| `aud`                 | Audience        | Identifies the recipients that the JWT is intended for. Each principal intended to process the JWT **must** identify itself with a value in the audience claim. If the principal processing the claim does not identify itself with a value in the `aud` claim when this claim is present, then the JWT **must** be rejected.                                  |
| `exp`                 | Expiration Time | Identifies the expiration time on and after which the JWT **must not** be accepted for processing. The value must be a NumericDate:[[9]](https://en.wikipedia.org/wiki/JSON_Web_Token#cite_note-rfc-7519-section-4.1.4-9) either an integer or decimal, representing seconds past [1970-01-01 00:00:00Z](https://en.wikipedia.org/wiki/Unix_time "Unix time"). |
| `nbf`                 | Not Before      | Identifies the time on which the JWT will start to be accepted for processing. The value must be a NumericDate.                                                                                                                                                                                                                                                |
| `iat`                 | Issued at       | Identifies the time at which the JWT was issued. The value must be a NumericDate.                                                                                                                                                                                                                                                                              |
| `jti`                 | JWT ID          | Case-sensitive unique identifier of the token even among different issuers.                                                                                                                                                                                                                                                                                    |
