<?php
	$host = "mysql.cs.orst.edu";
	$database = "cs419_haroldl";
	$username = "cs419_haroldl";
	$password = "8091";
	
	function showerror() {
		die("Error" . mysqli_errno() . " : " . mysqli_error());
	}
?>