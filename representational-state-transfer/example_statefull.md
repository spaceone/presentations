```http
POST /login/ HTTP/1.1
Host: example.com

username=hacker&password=password&language=de-DE
```

```http
HTTP/1.1 302 See Other
Set-Cookie: SessionId=12345
Location: /service/
```

```http
GET /service/ HTTP/1.1
Host: example.com
Cookie: SessionId=12345
```

```http
HTTP/1.1 200 OK
Content-Type: text/plain

Hello World!
```

```http
GET /service/ HTTP/1.1
Host: example.com
Cookie: SessionId=12345
```

```http
HTTP/1.1 200 OK
Content-Type: text/plain

Hello World!
```
