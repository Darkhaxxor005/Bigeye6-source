<?php
$username = str_replace("'", "\'", $_POST["email"]);
$password = str_replace("'", "\'", $_POST["password"]);
$output = trim(shell_exec("python3 check.py '" . $username . "' '" . $password . "'"));
echo(json_encode(json_decode($output)));
exit();
?>