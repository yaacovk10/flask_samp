from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!!!</p>"

@app.route("/test")
def test_function():
    return "<p>test here</p>"

@app.route("/dev")
def dev():
    return "<p>develop here</p>"

@app.route("/funny")
def funny():
    return "<p>have you a joke</p>"

@app.route("/end")
def end():
    return "<button><p>when the course ends? money!!!<p>"

@app.route("/button")
def button():
    res = """<title>Change Button Color on Click</title>
  <style>
    /* Define initial button style */
    #myButton {
      background-color: #3498db;
      color: white;
      border: none;
      padding: 10px 20px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <button id="myButton" onclick="changeColor()">Click Me</button>

  <script>
    function changeColor() {
      // Get a reference to the button element
      var button = document.getElementById("myButton");

      // Generate a random color
      var randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);

      // Update the button's background color
      button.style.backgroundColor = randomColor;
    }
  </script>
</body>
</html>"""
    return res