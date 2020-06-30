from flask import Flask, render_template

# Configure application
app = Flask(__name__)

@app.route('/index1', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    greeting = 'Welcome to My Data Science Portfolio Website'

    return render_template('/index1.html',
                            greeting=greeting)