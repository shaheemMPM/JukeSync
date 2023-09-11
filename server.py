from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def dashboard():
  return render_template('index.html')

@app.route('/next-song', methods=['GET'])
def next_song():
  return '1'

if __name__ == '__main__':
  app.run(debug=True)
