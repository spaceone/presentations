<?php
	print("Please specify the name of the file to delete");

	$file = $_GET['filename'];
	system("rm $file");
