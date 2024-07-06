from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'supersecretkey'

UPLOAD_FOLDER = 'static/input'
OUTPUT_FOLDER = 'static/output'

# Ensure the input and output directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def convert_mov_to_webm(input_folder, output_folder):
    ffmpeg_path = 'ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.mov'):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.webm')
            command = [
                ffmpeg_path,
                '-i', input_file,
                '-c:v', 'libvpx-vp9',  
                '-b:v', '1M',
                '-c:a', 'libvorbis',
                output_file
            ]
            subprocess.run(command)

@app.route('/')
def index():
    input_files = os.listdir(UPLOAD_FOLDER)
    output_files = os.listdir(OUTPUT_FOLDER)
    return render_template('index.html', input_files=input_files, output_files=output_files)

@app.route('/upload_files', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        flash('No files part')
        return redirect(request.url)
    files = request.files.getlist('files')
    for file in files:
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file.filename.endswith('.mov'):
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    flash('Files successfully uploaded')
    return redirect(url_for('index'))

@app.route('/convert_files', methods=['POST'])
def convert_files():
    convert_mov_to_webm(UPLOAD_FOLDER, OUTPUT_FOLDER)
    return jsonify(status="success")

@app.route('/get_files', methods=['GET'])
def get_files():
    input_files = os.listdir(UPLOAD_FOLDER)
    output_files = os.listdir(OUTPUT_FOLDER)
    return jsonify(input_files=input_files, output_files=output_files)

if __name__ == '__main__':
    app.run(debug=True)