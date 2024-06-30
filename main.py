from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/aboutus.html')
def aboutme():
    return render_template('aboutus.html')

@app.route('/otherthought.html')
def otherthought():
    with open('saved_thought.txt', 'r') as file:
        data = file.readlines()
    return render_template('otherthought.html', data=data)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_text():
    data = request.form['data']
    with open('saved_thought.txt', 'a') as file:
        file.write(data + '\n')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=4040)