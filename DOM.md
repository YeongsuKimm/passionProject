<html>
<head>
    <title>Message Switcher</title>
    <style>
        /* Add some basic styling */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f2f2f2;
        }
        button {
            padding: 10px 20px;
            background-color: #3498db;
            color: #fff;
            border: none;
            cursor: pointer;
        }
        #status {
            font-size: 24px;
            color: #555;
        }
        /* Create a simple animation for message switching */
        @keyframes switchAnimation {
            0% {
                transform: scale(1);
                opacity: 1;
            }
            50% {
                transform: scale(1.1);
                opacity: 0.5;
            }
            100% {
                transform: scale(1);
                opacity: 1;
            }
        }
    </style>
</head>
<body>
    <button id="switchButton">Switch Message</button>
    <p id="status">Not Switched</p>
    <script>
        const switchButton = document.getElementById("switchButton");
        const status = document.getElementById("status");
        // Function to switch the message and update the status
        function switchMessage() {
            const messages = ["Impressive!", "Cool!", "Awesome!", "Amazing!"];
            const currentMessage = status.innerHTML;
            // Randomly choose a new message that is different from the current one
            let newMessage;
            do {
                newMessage = messages[Math.floor(Math.random() * messages.length)];
            } while (newMessage === currentMessage);
            // Animate the message switching
            status.style.animation = "switchAnimation 0.5s";
            setTimeout(() => {
                status.style.animation = "none";
                status.innerHTML = newMessage;
            }, 500);
        }
        // Add a click event listener to the button
        switchButton.addEventListener("click", switchMessage);
    </script>
</body>
</html>
