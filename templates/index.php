<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link  href="static/style2.css" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100;200;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <title>Virtual Dressing Room</title>
</head>
<body>
    <!-- Add a "Go Back" button with a link to http://africantailor.co.uk -->
    <a href="https://africantailor.co.uk" id="goback-btn">Home</a>
    <button id="fullscreen-btn" onclick="toggleFullScreen()">Toggle Fullscreen</button>
    <img src="{{ url_for('video_feed') }}" id="video-feed">
    <form action="{{ url_for('change_cloth', direction='prev') }}" method="post" onsubmit="showLoader()">
        <button type="submit" class="action-btn2">Previous design</button>
        <div class="loader" id="loader"></div>
    </form>
    <form action="{{ url_for('change_cloth', direction='next') }}" method="post" onsubmit="showLoader()">
        <button type="submit" class="action-btn1">Next design</button>
        <div class="loader" id="loader"></div>
    </form>
    <form action="{{ url_for('upload') }}" method="post" enctype="multipart/form-data" onsubmit="showLoader()">
        <label for="file">Click here to Upload design</label>
        <input type="file" name="file" id="file" accept=".png, .jpg, .jpeg">
        <button class="upload-btn" type="submit">TRY ON</button>
        <div class="loader" id="loader"></div>
    </form>
   


    <!-- JAVASCRIPT FILES -->
    <script src="js2/jquery2.js"></script>
	<script src="js2/bootstrap.min.js"></script>
	<script src="main.js"></script>
    <script src="npm.js"></script>
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/jquery.sticky.js"></script>
    <script src="js/click-scroll.js"></script>
    <script src="js/custom.js"></script>
    <script src="script.js" defer></script>
    <script src="js/scriptcart.js"></script>
    <script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script>
<script src= "https://app.happychat.ai/chat.script.js" data-botid="95fdbc41-9dfc-43b8-9067-9e811f088fba" data-userid="109197138398578273202"> </script>
   
<script id="saia-mtm-integration" async src="https://mtm-widget.3dlook.me/integration.js" data-public-key="ODMwMg:1rKhKl:cTw3WGj1gsqhfo1pCX6rDRmrQH4"></script>

<script type="text/javascript" async>
    <script>
        function showLoader() {
            document.getElementById("loader").style.display = "inline-block";
        }

        function toggleFullScreen() {
            const elem = document.getElementById("video-feed");

            if (!document.fullscreenElement) {
                elem.requestFullscreen().catch(err => {
                    console.error(`Error attempting to enable fullscreen: ${err.message}`);
                });
            } else {
                document.exitFullscreen();
            }
        }
    </script>
    <!-- Add this script tag to your HTML -->
<script type="module">
  import * as pose from '@mediapipe/pose';

  const poseApp = new pose.Pose({
    locateFile: (file) => {
      return `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${file}`;
    },
  });

  poseApp.setOptions({
    modelComplexity: 1,
    smoothLandmarks: true,
    enableSegmentation: false,
    smoothSegmentation: true,
    minDetectionConfidence: 0.5,
    minTrackingConfidence: 0.5,
  });

  poseApp.onResults((results) => {
    // Handle pose estimation results here
    console.log(results);
  });

  navigator.mediaDevices.getUserMedia({ video: {} }).then((stream) => {
    document.body.appendChild(poseApp.video);
    poseApp.video.srcObject = stream;

    // Notify the pose module that the video has started
    poseApp.onVideoStarted();
  });
</script>

</body>
</html>
