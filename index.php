<?php
if (isset($_GET['check']))
echo $_POST['name'];
echo $_POST['message'];
?>

<form action ="index.php?check=1" method="post">
name : <input type ="text" name ="name" /> <br />
message : <textarea name ="message"></textarea> <br />
<input type="submit" value ="send Messages" />


</form>
