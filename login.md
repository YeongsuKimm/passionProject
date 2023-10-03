
<head>
    <title>Biscord Login</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="video-container">
        <iframe width="560" height="200" src="https://www.youtube.com/embed/x7SQaDTSrVg?si=P9QG5xO2NpJu3lrt?&autoplay=1&mute=1&playsinline=1&controls=0&showinfo=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <div class="login-container">
        <img src="https://cdn.discordapp.com/attachments/909947635715153952/1158606984837341204/image_U1SXQCvA_1696303517979_raw.jpg?ex=651cdc57&is=651b8ad7&hm=450290a4c3f2cd7dcc236467ea7218d62f82181d6fdc19ecc9ff901de3700ae6&">
        <h2>Welcome back to Whisp</h2>
        <form>
            <input type="text" placeholder="Email or Phone Number">
            <input type="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
        <p>Forgot your password? <a href="#">Reset it here</a></p>
    </div>
</body>


<style>
    
    .video-container{
        pointer-events: none;
        width: 100vw;
        height: 100vh;
    }
        
    iframe {
        pointer-events: none;
        position: absolute;
        top: 50%;
        left: 50%;
        width: 100vw;
        height: 100vh;
        transform: translate(-50%, -50%);
    }
    .login-container{
        position: absolute;
        color: #FFFFFF;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }
    body {
        background-color: #7289DA;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    .login-container {
        font-family: "calibri";
        background-color: #424549;
        text-align: center;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 1);
        max-width: 300px;
    }

    .login-container img {
        width: 80px;
        height: 80px;
    }

    .login-container h2 {
        color: white;
        font-size: 20px;
    }

    form {
        display: flex;
        flex-direction: column;
        margin-top: 20px;
    }

    input {
        padding: 10px;
        margin: 5px 0;
        border: 1px solid #D1D2D4;
        border-radius: 3px;
        outline: none;
    }

    button {
        background-color: #7289DA;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 3px;
        margin-top: 10px;
        cursor: pointer;
    }

    button:hover {
        background-color: #5F73A1;
    }

    a {
        color: #7289DA;
        text-decoration: none;
    }

    @media (min-aspect-ratio: 16/9) {
    .video-container iframe {
        height: 56.25vw;
    }
}
@media (max-aspect-ratio: 16/9) {
  .video-container iframe {
    width: 177.78vh;
  }
</style>
