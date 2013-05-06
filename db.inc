<?php
	$host = "localhost";
	$database = "cs419";
	$username = "LaraMartin";
	$password = "ryleedog";
	
	function showerror() {
		die("Error" . mysqli_errno() . " : " . mysqli_error());
	}
?>