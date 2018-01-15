```http
GET /users/Administrator HTTP/1.1
Host: example.com
Accept: text/ldif
```

```http
HTTP/1.1 200 OK
Date: Sun, 24 Dec 2017 21:49:41 GMT
Server: Apache/2.4.25 (Univention)
Last-Modified: Sun, 24 Dec 2017 21:48:27 GMT
Content-Length: 2402
Content-Type: text/ldif

```
```ldif
dn: uid=Administrator,cn=users,dc=dev,dc=local
uid: Administrator
objectClass: krb5KDCEntry
objectClass: univentionPerson
objectClass: person
objectClass: automount
objectClass: top
objectClass: inetOrgPerson
objectClass: sambaSamAccount
objectClass: organizationalPerson
objectClass: univentionPWHistory
objectClass: univentionMail
objectClass: univentionObject
objectClass: shadowAccount
objectClass: krb5Principal
objectClass: univentionPolicyReference
objectClass: posixAccount
krb5PrincipalName: Administrator@DEV.LOCAL
uidNumber: 2002
sambaAcctFlags: [U          ]
sambaPasswordHistory: E5A5C3CF8AE7D67AE6D618EA715ACD5BB48695C31BEC8D3D6E61654A7B1DDB1B
krb5MaxLife: 86400
cn: Administrator
krb5MaxRenew: 604800
krb5KeyVersionNumber: 1
loginShell: /bin/bash
univentionObjectType: users/user
krb5KDCFlags: 126
sambaPwdLastSet: 1513590788
sambaNTPassword: CAA1239D44DA7EDF926BCE39F5C65D0F
displayName: Administrator
sambaSID: S-1-5-21-1290176872-3541151870-1783641248-500
gecos: Administrator
sn: Administrator
pwhistory: $6$4rKnG/q7gqATKuZo$RbGlZJ8t2XUAku4hj4HsehmINw7NRRR9NZa6GEj3ijaV09tUo5nYGb7TeeBmuSErl3.B4KfY/L1VCBEjWg0R7/
homeDirectory: /home/Administrator
gidNumber: 5000
sambaPrimaryGroupSID: S-1-5-21-1290176872-3541151870-1783641248-512
univentionPolicyReference: cn=default-admins,cn=admin-settings,cn=users,cn=policies,dc=dev,dc=local
univentionUMCProperty: udmUserGridView=default
univentionUMCProperty: favorites=updater,appcenter:appcenter,udm:users/user,udm:groups/group,udm:computers/computer,udm:navigation
```
