from flask import Flask, render_template, send_from_directory, Response
import cv2
import subprocess

app = Flask(__name__)

process = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    global process
    process = subprocess.Popen(['python', 'main.py'])
    return "output"

@app.route('/shutdown-script', methods=['POST'])
def shutdown_script():
    global process
    if process:
        process.terminate()
        process = None
    return "Script shutdown"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)