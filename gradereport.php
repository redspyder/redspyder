<!DOCTYPE HTML>
<html>
<body>
<?php
// Check for assignment selection
if (isset($_POST['assignment'])) {
	// Session
	session_start();
	
	// Connect to db
	require 'db.inc';
	
	$mysqli = mysqli_connect($host, $username, $password, $database);
	
	// Check that connection was successful
	if ($mysqli->connect_errno) {
		echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
	}
	
	// Get report
	$query = "SELECT * FROM Report WHERE assnId = ".mysql_real_escape_string($_POST['assignment'])." AND stuId = ".mysql_real_escape_string($_SESSION['student']).";";
	
	$result = $mysqli->query($query);
	
	// Check that query successful
	if ($mysqli->errno) {
		echo "Failed to execute query: (" . $mysqli->errno . ") " . $mysqli->error;
		echo "<br />Query: ".$query;
	}

	$row = $result->fetch_assoc();
	
	// Get assignment name
	$query = "SELECT * FROM Assignment WHERE aid = ".mysql_real_escape_string($_POST['assignment']).";";
	
	$assn = $mysqli->query($query);
	
	// Check that query successful
	if ($mysqli->errno) {
		echo "Failed to execute query: (" . $mysqli->errno . ") " . $mysqli->error;
		echo "<br />Query: ".$query;
	}
	
	$name = $assn->fetch_assoc();
	
	// Echo results to screen
	echo '<label for="report">Report for '.$name['name'].': </label>
	<table id="report">
	<tr><th>Stage 1</th><th>Stage 2</th><th>Stage 3</th><th>Stage 4</th></tr>
	<tr><td>'.$row['stage1'].'</td><td>'.$row['stage2'].'</td><td>'.$row['stage3'].'</td><td>'.$row['stage4'].'</td></tr>
	</table>';
	
	// Free results
	$result->free();
	$assn->free();
	
	// Close connection
	$mysqli->close();
}
else {
	// Print error message
	echo 'You must select an assignment first! <a href="homeworkselector.php">Go Back</a>';
}
?>
</body>
</html>