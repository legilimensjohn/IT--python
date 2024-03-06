<?php
$servername = "localhost";
$username = "root"; 
$password = ""; 
$dbname = "dataform";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$stmt_users = $conn->prepare("INSERT INTO Users (full_name, email, date_of_birth, gender) VALUES (?, ?, ?, ?)");
$stmt_users->bind_param("ssss", $full_name, $email, $date_of_birth, $gender);

$stmt_addresses = $conn->prepare("INSERT INTO Addresses (user_id, street_address, city, state, country, zip_code) VALUES (?, ?, ?, ?, ?, ?)");
$stmt_addresses->bind_param("isssss", $user_id, $street_address, $city, $state, $country, $zip_code);

$full_name = $_POST['full_name'] ?? '';
$email = $_POST['email'] ?? '';
$date_of_birth = $_POST['date_of_birth'] ?? '';
$gender = $_POST['gender'] ?? '';
$street_address = $_POST['street_address'] ?? '';
$city = $_POST['city'] ?? '';
$state = $_POST['state'] ?? '';
$country = $_POST['country'] ?? '';
$zip_code = $_POST['zip_code'] ?? '';

$stmt_users->execute();
$user_id = $stmt_users->insert_id; 

$stmt_addresses->execute();

$stmt_users->close();
$stmt_addresses->close();
$conn->close();

echo "Registration successful!";
?>