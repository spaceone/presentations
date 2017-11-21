def is_administrator(username):
	return bool(ldap_connection.search('(&(objectType=ucsschoolAdministrator)(uid=' + username + '))'))
