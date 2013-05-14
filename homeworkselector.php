<!DOCTYPE HTML>
<html>
<body>
<form action="gradereport.php" method="post">
<label for="hwselect"></label>
<select id="hwselect" name="assignment">
<?php
	// Session variables
	session_start();
	
	$_SESSION['student'] = 1;
	
	// Connect to db
	require 'db.inc';
	
	$mysqli = mysqli_connect($host, $username, $password, $database);
	
	// Check that connection was successful
	if ($mysqli->connect_errno) {
		echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
	}
	
	// Get homework options
	$query = "SELECT * FROM Assignment;";
	
	$result = $mysqli->query($query);
	
	if ($mysqli->errno) {
		echo "Failed to execute query: (" . $mysqli->errno . ") " . $mysqli->error;
		echo "<br />Query: ".$query;
	}

	// Loop through results and store as options in form
	while($hw = $result->fetch_assoc()) {
		// for each result
		echo '<option id="'.htmlspecialchars($hw['aid']).'" value="'.htmlspecialchars($hw['aid']).'">'.htmlspecialchars($hw['name']).'</option>';
	}
	
	// Free result
	$result->free();
	
	// Close connection
	$mysqli->close();
?>
</select>
<label>Student ID</label>
<input type="text"></input>
<input type="submit" value="Get Report"></input>
</form>
</body>
</html>