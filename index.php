<!DOCTYPE html>
<head>
  <title>Pusher Test</title>
  <script src="https://js.pusher.com/4.1/pusher.min.js"></script>
  <script>

    // Enable pusher logging - don't include this in production
    Pusher.logToConsole = true;

    var pusher = new Pusher('your-appid', {
      cluster: 'us2',
      encrypted: true
    });

    var channel = pusher.subscribe('<?php echo $_GET['channel']; ?>');
    channel.bind('my-event', function(data) {
      alert(data.message);
    });
  </script>
</head>

Your notify link: <a href="https://dev.c0defox.es/push/?channel=<?php echo $_GET['channel']; ?>">Get Notified</a>

<br />

Leave this page open on your phone and go about your day.<br />
When the person who created this push channel writes a message, you will get a notification