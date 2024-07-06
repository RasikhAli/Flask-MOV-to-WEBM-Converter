# Flask MOV to WEBM Converter

This Flask application allows users to upload MOV files, convert them to WEBM format using ffmpeg, and view the converted files.

## Prerequisites
- Python 3.x installed
- Flask framework
- ffmpeg installed and added to system PATH
 
**ffmpeg Download:**
You can download the latest version of ffmpeg for Windows from [ffmpeg.org](https://ffmpeg.org/download.html).

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Flask-MOV-to-WEBM-Converter
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Run the application:
   ```bash
   python app.py
   ```
   The application will run on http://localhost:5000 by default.

## Usage
1. Upload MOV Files:
     - Click on the "Choose MOV files" button to select one or more MOV files.
     - Click on the "Upload" button to upload the selected files.

3. Convert Files:
     - After uploading MOV files, click on "Convert All" to convert all uploaded files to WEBM format.
     - Converted files will appear in the "Files in Output Directory" section.

4. Play Video:
     - Click on the "Play" button next to any file in the "Files in Input Directory" or "Files in Output Directory" sections to preview the video.

## Folder Structure
  ```
      ffmpeg-master-latest-win64-gpl/      # Files of ffmpeg
      static/
           input/: Directory to store uploaded MOV files.
           output/: Directory to store converted WEBM files.
  ```

## Technologies Used
    Flask: Python web framework
    ffmpeg: Multimedia framework for handling video conversion
