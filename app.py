from flask import Flask, render_template, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    subprocess.call(['python', 'main.py'])
    return 'Script executed'

@app.route('/video')
def video():
    return send_from_directory(os.getcwd(), 'output.mp4')

if __name__ == '__main__':
    app.run(debug=True)