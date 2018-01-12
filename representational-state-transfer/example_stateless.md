```http
GET /service/ HTTP/1.1
Host: example.com
Accept-Language: de-DE
```

```http
HTTP/1.1 401 Unauthenticated
WWW-Authenticate: Basic realm="Service"
```

```http
GET /service/ HTTP/1.1
Host: example.com
Authorization: basic aGFja2VyOnBhc3N3b3JkCg==
Accept-Language: de-DE
```

```http
HTTP/1.1 200 OK
Content-Type: text/plain

Hello World!
```

```http
GET /service/ HTTP/1.1
Host: example.com
Authorization: basic aGFja2VyOnBhc3N3b3JkCg==
Accept-Language: de-DE
```

```http
HTTP/1.1 200 OK
Content-Type: text/plain

Hello World!
```
