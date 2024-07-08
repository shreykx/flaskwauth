from flask import Flask, render_template, jsonify
from flask_cors import CORS
import jwt
from getenv import GetVariable
from db import CreateUser, CheckUser


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/user/login')
def login():
    return render_template('login.html')

@app.route('/user/signup')
def signup():
    return render_template('signup.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/api/login/<username>/<password>')
def authenticate(username, password):
    if CheckUser(username, password):
        token = jwt.encode({'username': username}, 'secretkey', algorithm='HS256')
        return jsonify({'token': token.decode('utf-8')}), 200
    else :
        return jsonify({'error': 'Invalid credentials'}), 401
    
@app.route('/api/create/<username>/<password>')
def create_user(username, password):
    return 
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=int(GetVariable('PORT')))