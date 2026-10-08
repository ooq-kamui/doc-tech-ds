
## csr cre


## case: sakura  -  2026-10

### key pair cre

not pass phrase

```
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out <file-name.key>
```

### csr cre

```
openssl req -new -key <file-name.key> -out <file-name.csr> -sha256
```

ex

```
_ openssl req -new -key skr-ssl.key -out skr-ssl.csr -sha256
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:JP
State or Province Name (full name) [Some-State]:Tokyo
Locality Name (eg, city) []:Komae-shi
Organization Name (eg, company) [Internet Widgits Pty Ltd]:ooq-kamui
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:ooq.jp
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
_
```

confirm

```
openssl req -noout -text -in <file-name.csr>
```


