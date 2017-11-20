<?php

$username = $_POST['username'];
$password = $_POST['password'];

$query = 'SELECT * from users where username="' . $username . '" AND password="' . $password . '" LIMIT 1';

if ($user = $db->select($query)) {
	printf("You are logged in %s", $user['username']);
}
