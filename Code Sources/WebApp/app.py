from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'SecretKey123'  # Replace with a strong secret key

# Variable to store ESP32 IP address and current user
ESP32_IP = None
LOGGED_IN_USER = None

# Hardcoded credentials (change these as needed)
USERNAME = 'admin'
PASSWORD = 'Team34ECE445'

@app.route('/login', methods=['GET', 'POST'])
def login():
    global LOGGED_IN_USER
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            # Check if someone else is already logged in
            if LOGGED_IN_USER and LOGGED_IN_USER != username:
                return "Another user is currently logged in. Try again later.", 403
            # Authenticate the user
            session['logged_in'] = True
            session['username'] = username
            LOGGED_IN_USER = username
            return redirect(url_for('index'))
        else:
            return "Invalid credentials. Please try again.", 401
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    global LOGGED_IN_USER
    if 'logged_in' in session and session['logged_in']:
        LOGGED_IN_USER = None
        session.clear()
        return jsonify({'message': 'Logged out successfully'}), 200
    return jsonify({'error': 'No user logged in'}), 400

@app.route('/')
def index():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    global ESP32_IP
    data = request.get_json()
    esp32_ip = data.get('ip')

    if esp32_ip:
        ESP32_IP = esp32_ip
        print(f"Received ESP32 IP address: {ESP32_IP}")
        return jsonify({'message': 'ESP32 IP registered successfully'}), 200
    else:
        return jsonify({'error': 'No IP address provided'}), 400

@app.route('/draw', methods=['POST'])
def draw():
    global ESP32_IP
    if 'logged_in' not in session or not session['logged_in']:
        return jsonify({'error': 'Unauthorized access'}), 403

    if not ESP32_IP:
        return jsonify({'error': 'ESP32 IP address not registered'}), 400

    data = request.get_json()
    shape = data.get('shape')

    if shape not in ['circle', 'square', 'rectangle', 'triangle']:
        return jsonify({'error': 'Invalid shape'}), 400

    try:
        response = requests.post(f'http://{ESP32_IP}/draw', json={'shape': shape})
        response.raise_for_status()
        return jsonify({"message": "Drawing command sent to ESP32"}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'Error with ESP32 comms': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
