from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def que():
    return render_template('form.html')

@app.route('/statistics')
def stat():
    return render_template('statistics.html')




if __name__ == '__main__':
    app.run(debug=False)
    
