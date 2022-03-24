from flask import Flask,render_template,request,redirect,url_for,make_response,jsonify
from werkzeug.utils import secure_filename
import os
import cv2
 
from datetime import timedelta
 
ALLOWED_TYPE = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_TYPE
 
app = Flask(__name__)
app.send_file_max_age_default = timedelta(seconds=1)
 
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
 
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "Upload Type，Only:png、PNG、jpg、JPG、bmp"})
 
        user_input = request.form.get("name")
 
        basepath = os.path.dirname(__file__) 
 
        upload_path = os.path.join(basepath, 'static/images',secure_filename(f.filename))
        f.save(upload_path)
 
        image_data = open(upload_path, "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/png'
        return response
 
    return render_template('upload.html')
 
if __name__ == '__main__':
    # app.debug = True
    app.run(host='localhost', port=5001, debug=True)
