<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $text = $_POST["user_text"];
    
    // Сохранение текста в файле
    $file = fopen("saved_text.txt", "w");
    fwrite($file, $text);
    fclose($file);
    
    echo "Text saved successfully!";
}
?>