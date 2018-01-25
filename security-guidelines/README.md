# Security guideleines

"one of the best type of challenges is where you are given the code and you would swear there's nothing wrong with it but you know it is a challenge, so you know to keep trying; programming is like such a challenge but you don't know it is a challenge"

## LDAP ACL's
LDAP ACL's sind die kritischste Angriffsstelle eines UCS-Systems. Sind die LDAP-ACL's nicht sicher genug definiert ist die komplette Domäne in Gefahr.
Wer an den LDAP-ACL's Änderungen vornimmt sollte die manpage `slapd.access` gelesen und verstanden haben.

* `add_content_acl on` muss in der slapd.conf definiert sein, ansonsten werden die ACL's, die den Inhalt eine Objekts einschränken, beim Erstellen vom Objekt nicht ausgewertet!
* TODO: attrs=entry
* TODO: attrs= muss definiert sein, wenn Schreibrechte erlaubt werden
…
{{Bug|20187}}
{{Bug|41725}}
{{Bug|42065}}
{{Bug|41715}}
{{Bug|41797}}
{{Bug|41725}}

### Bekannte Angriffsvektoren
* Erstellen eines Objekts `person` mit `uidNumber=0`
* Erstellen eines Objekts `univentionShare` + `univentionShareNFS` / `univentionShareSamba` mit `univentionShareHost=$ldap_master` und `univentionSharePath=/`
* Erstellen eines Objekts `SambaSamAccount`

## LDAP Filter Escapen
LDAP-Filter müssen immer escaped werden, dafür sind die Funktionen notwendig:
```python
ldap.filter.filter_format('(&(foo=%s)(bar=%s))', [value_foo, value_bar])
```

Wenn `filter_format()` mal nicht benutzt werden kann, gibt es alternativ auch:
```python
'foo=%s' % (ldap.filter.escape_filter_chars(value_foo),)
```

## LDAP DN's Escapen
Beim zusammenbauen von DN's müssen die Komponenten einer DN immer escaped werden:
```python
ldap.dn.dn2str([
    [('cn', 'foo', ldap.AVA_STRING), ('uid', 'bar', ldap.AVA_STRING)],
    [('dc', 'univention', ldap.AVA_STRING)]
])
# erzeugt folgende DN: 'cn=foo+uid=bar,dc=univention'
```
Wenn bereits die restlichen Komponenten der DN feststehen kann auch folgendes benutzt werden, (aber nicht, wenn die DN vorher geparsed wurde):
```python
dn = 'dn=%s,dc=foo,dc=bar' % (ldap.dn.escape_dn_chars(value_foo),)
```
### Vorsicht! ldap.dn.explode_dn() macht bereits escape_dn_chars()!
```python

# Falsch!
>>> ldap.explode_dn('cn=foo\+\,bar,dc=bar', True)[0]
'foo\\+\\,bar'
# Richtig!
>>> ldap.dn.str2dn('cn=foo\+\,bar,dc=bar')[0][0][1]
'foo+,bar'

```

Daher muss das parsen von DN's immer mit `ldap.dn.str2dn()` gemacht werden.

## UCR Variablen setzen
```python
from univention.config_registry.frontend import ucr_update
from univention.config_registry import ConfigRegistry
ucr = ConfigRegistry()
ucr.load()
ucr_update(ucr, {var: value})

```
anstatt
```python
from univention.config_registry import handler_set
handler_set(['%s=%s' % (var, value)])

```

## Shell Code ausführen
Um bestimmte System-Kommandos aus python heraus zu starten sollte niemals `os.system` / `os.popen` / etc. verwendet werden sondern immer `subprocess.call` / `subprocess.Popen`!

### Shell Argumente escapen
Argumente müssen immer z.B. mittels `pipes.quote()` escaped werden
```python
import pipes
import sys
cmd = ' '.join(pipes.quote(x) for x in sys.args)
sys.exit(subprocess.call(['ssh', '1.2.3.4', cmd]))

```

### subprocess
`subprocess.call()` / `subprocess.Popen()` sollten nicht mit dem Argument `shell=True` benutzt werden.
`shell=True` erlaubt z.B. Umgebungsvariablen zu verändern und evaluierung von Shell-Ausdrücken, die zu unabsichtlicher Code-Ausführung führen kann.

Um aus einem String-Kommando eine Liste von Strings zu machen kann z.B. folgendes benutzt werden:
```python
args = shlex.split(cmd)
subprocess.call(args)

```

{{Bug|20483}}
{{Bug|39993}}

## Dateipfade manipulieren
{{Bug|41005}}
{{Bug|28189}}
{{Bug|38270}}
{{Bug|35740}}

Eine effektive basedir-restriction sieht so aus:
```python
BASEDIR = '/foobar/'
if not os.path.abspath(filename).startswith(BASEDIR):
   raise ValueError('hacking attempt!')

```

Alternativ ergibt in manchen Fällen auch folgendes Sinn, allerdings ist das vulnerable für symlink-Attacken!:
```python
os.path.join(basedir, os.path.basename(user_input))

```

### os.path.join()
{{Bug|43039}}
{{Bug|38300}}
{{Bug|39981}}
{{Bug|38441}}
{{Bug|33456}}
{{Bug|32176}}

`os.path.join('/foo', '/bar')` ergibt `'/bar'` und nicht `'/foo/bar'`!

### symlink-Attacken
{{Bug|38291}}

## Code execution

### univention.lib.atjobs
{{Bug|40367}}
{{Bug|40354}}

### python eval()
`eval()` evaluiert python-Ausdrücke (z.B. einzelne statements) z.B. die mit `repr()` erstellt worden sind.

Die Sicherheitsgefahr hierbei liegt, dass `__import__('os').system('id')` auch ein gültiger python-Ausdruck ist.

Alternativen:
`ast.literal_eval(data)` oder `getattr(obj, attr, default)`

{{Bug|31523}}
{{Bug|41736}}
{{Bug|41730}}
{{Bug|22261}}

## Race Conditions
Beim Schreiben von Dateien mit geheimen Inhalten muss vorher die umask gesetzt werden, oder die Datei muss mit entsprechendem Modus geöffnet werden:

Richtig:
```python
import os
fd = os.open(secret_filename, os.O_WRONLY | os.O_CREAT, 0600)
os.write(fd, secret)
os.close(fd)
```

Besser, weil die Zieldatei dann atomar verändert wird, falls sie schon existiert:
```python
import os
import tempfile
import shutil
fd, tmp_filename = tempfile.mkstemp(prefix=os.path.basename(secret_filename), dir=os.path.dirname(secret_filename))
with os.fdopen(fd, 'w') as fd:
	fd.write(secret)
shutil.move(tmp_filename, secret_filename)
```

Falsch:
```python
with open(secret_filename, 'w') as fd:
    os.fchmod(fd.fileno(), 0600)
    fd.write(secret)
```

## Pickle führt Code aus!
{{Bug|36452}}
{{Bug|40583}}
{{Bug|40584}}
{{Bug|40585}}

Alternativ, für simple Datenstrukturen kann JSON benutzt werden. Aber vorsicht, JSON ist ein UTF-8 only Format, jegliche andere Kodierung geht verloren bzw. bytes(str) können nur gedumpt werden, wenn sie UTF-8 kodierbar sind.
```python
import json
import ast
with open(filename, 'w') as fd:
   json.dump(repr(obj), fd)
with open(filename) as fd:
   obj = ast.literal_eval(json.load(fd))
```

### python input()
`input()` ist dasselbe wie `eval(raw_input(prompt))`. `raw_input()` sollte stattdessen verwendet werden.

### Cookies
Vorsicht! Die Python-stdlib führt pickle-Code aus:

```python
from Cookie import Cookie
Cookie('Set-Cookie: foo="cposix\012_exit\012p1\012(I1\012tp2\012Rp3\012."')

```

Niemals `Cookie.Cookie` oder `Cookie.SmartCookie` verwenden. Stattdessen `Cookie.SimpleCookie`!

### Logging
* Passwörter dürfen nicht im Logfile landen
* Benutzereingaben sollten mit `%r` / `repr()` ins Logfile geschrieben werden.
→ `univention.debug.debug(univention.debug.ADMIN, univention.debug.INFO, '\x00')` raised `TypeError`. Dadurch kann DoS erreicht werden.

→ durch bestimmte byte-ketten kann das encoding der Logdatei kaputt gemacht werden, was `UnicodeDecodeError`-Fehler beim Auslesen der Datei erzeugt

## CRLF Injection

{{Bug|29975}}

## Denial of Service
### univention.debug
TypeError wenn Null-Byte geloggt wird.

{{Bug|40367}}

## Manipulationen im LDAP
→ DoS
{{Bug|40354}}


Passwörter erhalten → {{Bug|41336}}

## Web-Sicherheit (HTTP und HTML)

### Cross Site Scripting
Mit den dojo utilities `dojox/html/entities` kann per `entities.encode()` HTML code kodiert werden.

### URL-Kodierung
Parameter in Query-Strings können in Javascript mit `encodeURIComponent()` kodiert werden.
In python mit `urllib.quote()`.

### Cross Site Request Forgery
Der HTTP-Header "Content-Security-Policy" sollte in HTTP-Antworten immer gesetzt sein.
Ebenso die folgenden Header:
```http
HTTP/1.1 200 OK
X-Permitted-Cross-Domain-Policies: master-only
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
```

### Links mit target="_blank"
Immer noopener noreferrer mitgeben!
```html
<a href="..." target="_blank" rel="noopener noreferrer">...</a>
```
See also:
https://mathiasbynens.github.io/rel-noopener/

### Content-Security-Policy
See also:
https://developers.google.com/web/fundamentals/security/csp/

## SSL / TLS
z.B.: MITM
{{Bug|36452}} {{Bug|43031}} {{Bug|43033}} {{Bug|43035}}

## C Code
z.B. Buffer overflow {{Bug|34041}}

## XML External Entity attacks

{{Bug|43315}}
* `defusedxml` anstatt `xml.etree.ElementTree` verwenden.
