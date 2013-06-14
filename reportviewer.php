<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" />
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
<script>
  $(function() {
    $( "#accordion" ).accordion({
      collapsible: true
    });
  });
</script>
</head>
<body>
<div id="accordion">
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
	$query = "SELECT * FROM Report WHERE sid = ".mysql_real_escape_string($_SESSION['student']).";";
	
	$result = $mysqli->query($query);
	
	if ($mysqli->errno) {
		echo "Failed to execute query: (" . $mysqli->errno . ") " . $mysqli->error;
		echo "<br />Query: ".$query;
	}

	// Loop through results and store as options in form
	while($row = $result->fetch_assoc()) {
		// for each result
		echo '<h3>'.htmlspecialchars($row['aid']).'</h3>';
		echo '<div><label for="report">Report for '.$row['sid'].': </label>
	<table id="report">
	<tr><th>Stage 1</th><th>Stage 2</th><th>Stage 3</th></tr>
	<tr><td>'.$row['stage1'].'</td><td>'.$row['stage2'].'</td><td>'.$row['stage3'].'</td></tr>
	</table></div>';
	}
	
	// Free result
	$result->free();
	
	// Close connection
	$mysqli->close();
?>
</div>
</body>
</html>