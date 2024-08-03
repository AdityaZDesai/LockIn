import os
from flask import Flask
from flask import render_template, request, redirect, url_for
import json


app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.static_folder, 'videos')
@app.route("/main")
def main():
    return "<h1> HELLLOOO </h1>"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        uploaded_file = request.files['filename']
        if uploaded_file.filename != '':
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)
    return render_template('upload.html')

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    return redirect(url_for('main'))

@app.route("/watch", methods=['GET'])
def watch():
    videos_folder = os.path.join(app.static_folder, 'videos')
    videos = [f for f in os.listdir(videos_folder) if f.endswith('.mp4')]
    return render_template('watch.html', videos=videos, len= len(videos))




if __name__ == "__main__":
    app.run(debug=True)
