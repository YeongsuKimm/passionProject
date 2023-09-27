<html>
<head>
    <title>Message Switcher</title>
</head>
<body>
    <button id="switchButton">Switch message</button>
    <p id="status">Not Switched</p>
    <script>
        const status = document.getElementById("status");
        // Function to switch the links and update the status
        function switchMsg() {
            status.innerHTML = "Switched";
        }
        // Add a click event listener to the button
        switchButton.addEventListener("click", switchMsg);
    </script>
</body>
</html>
