from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')