#app.py
from flask import Flask, json, request, jsonify, send_from_directory, render_template
import os
# import urllib.request
from werkzeug.utils import secure_filename
 
app = Flask(__name__)

 
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/')
def main():
    return render_template('index.html')
 
uploaded_files = []

@app.route('/files', methods=['GET'])
def get_files_info():
    return jsonify(uploaded_files)


@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
 
    files = request.files.getlist('files')
     
    errors = {}
    success = False
     
    for file in files:
        # print("File object:", file)  # Print the file object
        # print("File object type:", type(file))  # Print the type of the file object      
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            # print("File path:", filename) 
            file_info = {
                'filename': file.filename,
                'size': os.path.getsize(filename),
                'url': f'http://localhost:5000/uploads/{file.filename}'  # Change the URL as needed
            }
            uploaded_files.append(file_info)

            success = True
            
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    

    
@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)