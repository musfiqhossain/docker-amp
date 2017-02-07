<?php

//phpinfo();
$servername = "db";
$username = "root";
$password = "hunter2";
$dbname = "database";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * from pet";
$result = $conn->query($sql);

if($result) {
  if ($result->num_rows > 0) {
      // output data of each row
      while($row = $result->fetch_assoc()) {
         // echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
  	var_dump($row);
      }
  } else {
      echo "0 results";
  }
}

$conn->close();
?>
