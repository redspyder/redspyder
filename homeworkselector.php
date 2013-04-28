<!DOCTYPE HTML>
<html>
<body>
<form>
<label for="hwselect"></label>
<select id="hwselect">
<?php
	// Connect to db
	// Get homework options
	// for each result
	echo '<option id="'.$hw.'">'.$hw.'</option';
?>
</select>
<input type="submit" value="Get Report"></input>
</form>
</body>
</html>