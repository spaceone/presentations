```http
GET /users/Administrator HTTP/1.1
Host: example.com
Accept: text/plain
```

```http
HTTP/1.1 200 OK
Date: Sun, 24 Dec 2017 21:49:41 GMT
Server: Apache/2.4.25 (Univention)
Last-Modified: Sun, 24 Dec 2017 21:48:27 GMT
Content-Length: 1418
Content-Type: text/html

```
```html
<html>
<head>
	<link rel="parent" href="/users/" />
	<users>
	 	 <title>Benutzer: Administrator</title>
	 	 <link rel="search" href="udm/users/user/"/>
	 	 <link rel="create-form" href="udm/users/user/edit"/>
	 	 <link rel="edit-form" href="udm/users/user/edit"/>
	 	 <link rel="icon" href="udm/users/user.svg"/>
	 	 <link rel="udm/report-types" href="udm/users/user/report-types"/>
	</users>
</head>
<body>
<user dn="uid=Administrator,cn=users,dc=base">
 <link rel="self edit" href="udm/users/user/uid%3DAdministrator%2Ccn%3Dusers%2Cdc%3Dbase"/>
 <link rel="type" href="udm/users/user"/>
 <operations>
  <link rel="edit" href="udm/users/user/uid%3DAdministrator%2Ccn%3Dusers%2Cdc%3Dbase"/>
  <link rel="udm/delete" href="udm/users/user/uid%3DAdministrator%2Ccn%3Dusers%2Cdc%3Dbase"/>
  <link rel="udm/move" href="udm/users/user/uid%3DAdministrator%2Ccn%3Dusers%2Cdc%3Dbase"/>
 </operations>
 <flags>
  <flag>system</flag>
 </flags>
 <name>Administrator</name>
 <path>base://users/</path>
 <options>
  <option>posix</option>
  <option>samba</option>
 </options>
 <policies>
  <link rel="udm/policies prefetch" href="udm/users/user/uid%3DAdministrator%2Ccn%3Dusers%2Cdc%3Dbase/policies/UMC"/>
  <link rel="udm/policies prefetch" href="udm/users/user/uid%3DAdministrator%2Ccn%3Dusers%2Cdc%3Dbase/policies/Passwords"/>
 </policies>
 <properties>
  <unixhome value="/home/Administrator"/>
  <sambahome value="None"/>
  <primaryGroup value="cn=Domain Admins,cn=groups,dc=school,dc=local"/>
  <uidNumber value="2002"/>
  <disabled value="none"/>
  <street value="None"/>
  <postcode value="None"/>
  <scriptpath value="None"/>
  <departmentNumber value="None"/>
  <description value="Built-in account for administering the computer/domain"/>
  <city value="None"/>
  <PasswordRecoveryMobile value="None"/>
  <homeShare value="None"/>
  <homedrive value="None"/>
  <overridePWLength value="None"/>
  <title value="None"/>
  <organisation value="None"/>
  <userexpiry value="None"/>
  <objectFlag value="None"/>
  <test value="None"/>
  <owncloudQuota value="None"/>
  <umcProperty>appcenterDockerSeen = false</umcProperty>
  <shell value="/bin/bash"/>
  <firstname value="None"/>
  <lastname value="Administrator"/>
  <mailHomeServer value="None"/>
  <employeeType value="None"/>
  <gidNumber value="5000"/>
  <birthday value="None"/>
  <employeeNumber value="None"/>
  <groups>
   <group>cn=Domain Admins,cn=groups,dc=school,dc=local</group>
  </groups>
  <PasswordRecoveryEmail value="None"/>
  <locked value="none"/>
  <password value="{crypt}$6$Gp1TqwDaQfg3YjKy$Q3O943/EDGuZulASD0TdNqNJG26oskh3eseVPymIfsQuwxDhSnnGtLsZXNOAyqKKUk2AkqUczop2C1ZDFs.1A/"/>
  <displayName value="Administrator"/>
  <mailPrimaryAddress value="None"/>
  <username value="Administrator"/>
  <owncloudEnabled value="1"/>
  <overridePWHistory value="None"/>
  <jpegPhoto value="None"/>
  <country value="None"/>
  <roomNumber value="None"/>
  <univentionPolicyReference value="cn=default-admins,cn=admin-settings,cn=users,cn=policies,dc=school,dc=local"/>
  <passwordexpiry value="None"/>
  <pwdChangeNextLogin value="None"/>
  <gecos value="Administrator"/>
  <sambaRID value="500"/>
  <profilepath value="None"/>
  <sambaLogonHours value="None"/>
  <homeSharePath value="None"/>
 </properties>
 <references/>
</user>
```
