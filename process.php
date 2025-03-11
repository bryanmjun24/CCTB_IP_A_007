<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve input values
    $numbers = escapeshellarg($_POST['numbers']);
    $threshold = escapeshellarg($_POST['threshold']);

    // Execute Python script
    $command = "python3 bitwise_operations.py $numbers $threshold";
    $output = shell_exec($command);
} else {
    $output = "<p>Error: Invalid request method.</p>";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Bitwise Operations Results</title>
</head>
<body>
    <h2>Processing Results:</h2>
    <?php echo $output; ?>
</body>
</html>
