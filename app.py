from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hellp world"

# added new function
@app.route('/chandra')
def chandra():
    return "hellp chandra"

if __name__ == '__main__':
    app.run(debug=True)
