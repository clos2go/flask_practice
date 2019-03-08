# flask_practice


Minimal Flask Operation:
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

To Run application (Mac):
-- cd into project directory and run:
```
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```