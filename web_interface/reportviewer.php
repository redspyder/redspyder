<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet" href="jquery-ui-1.10.3.custom/css/redmond/jquery-ui-1.10.3.custom.min.css" />
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
<script>
  $(function() {
    $( "#accordion" ).accordion({
      collapsible: true
    });
  });
</script>
<style>
body {
	background-color: rgb(46, 110, 158);
	color: #ffffff;
}
#label {
	font-size: 24px;
	font-weight: bold;
	padding-top: 24px;
}
#accordion {
	padding-top: 24px;
}
table td, th {
	border-style: solid;
	border-width: thin;
	border-collapse: collapse;
}
.stage {
	max-width: 350px;
	text-wrap: true;
}
</style>
</head>
<body>

<?php
	// Session variables
	session_start();
	
	$_SESSION['student'] = 'Student1';
	
	// Connect to db
	require 'db.inc';
	
	$mysqli = mysqli_connect($host, $username, $password, $database);

	// Check that connection was successful
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: (" . mysqli_connect_errno() . ") " . mysqli_connect_error();
	}
	
	// Get homework options
	$query = "SELECT * FROM Reports WHERE sid = '".mysql_real_escape_string($_SESSION['student'])."'";

	$result = $mysqli->query($query);
	
	if ($mysqli->errno) {
		echo "Failed to execute query: (" . $mysqli->errno . ") " . $mysqli->error;
		echo "<br />Query: ".$query;
	}
	echo '<div id="label"><label>Displaying available reports for '.$_SESSION['student'].': </label></div><div id="accordion">';
	// Loop through results and store as options in form
	while($row = $result->fetch_assoc()) {
		// for each result
		echo '<h3>'.htmlspecialchars($row['aid']).'</h3>';
		echo '<div><table id="report">
	<tr><th>Stage 1</th><th>Success?</th><th>Stage 2</th><th>Success?</th><th>Stage 3</th><th>Success?</th></tr>
	<tr><td class="stage">'.$row['stage1'].'</td><td>'.$row['status1'].'</td><td class="stage">'.$row['stage2'].'</td><td>'.$row['status2'].'</td><td class="stage">'.$row['stage3'].'</td><td>'.$row['status3'].'</td></tr>
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