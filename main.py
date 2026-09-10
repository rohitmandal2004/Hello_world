from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
  return 'Hello World from the gangster of Basirhat Goat Rohit Mandal, My english is englishing , to dont dare to toucg  😎'
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
