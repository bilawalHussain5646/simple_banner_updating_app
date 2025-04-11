from flask import Flask,request, jsonify,render_template,redirect,url_for,request
from database import app, db
from models import *
from flask_cors import cross_origin
import os
import shutil
# sys.path.insert(0, os.path.dirname(__file__))

app.config['SQLALCHEMY_POOL_SIZE'] = 10  # Adjust as needed
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 1800  # Adjust as needed
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600  # Adjust as needed
app.config['SQLALCHEMY_POOL_PRE_PING'] = True  # Adjust as needed

# Folder to store uploaded files
UPLOAD_FOLDER = 'banners'
BACKUP_FOLDER = 'backup_banners'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['BACKUP_FOLDER'] = BACKUP_FOLDER

# Allowed file extensions (optional)
ALLOWED_EXTENSIONS = {'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file and allowed_file(file.filename):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f"File uploaded successfully: {file.filename}"

    return "File type not allowed"



def backup_time(country_id,filename,filepath):
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"{timestamp}_{filename}"
    backup_path = os.path.join(app.config['BACKUP_FOLDER'],country_id, backup_filename)
    shutil.copy(filepath, backup_path)

# # Functionality: signup
@app.route('/', methods=['GET','POST'])
def index():
  
    if request.method == "POST":
            

            country_id = request.form["country"]

            desktop_en = request.files['desktop_en']
            mobile_en = request.files['mobile_en']
            desktop_ar = request.files['desktop_ar']
            mobile_ar = request.files['mobile_ar']





            if desktop_en and allowed_file(desktop_en.filename) and (mobile_en and allowed_file(mobile_en.filename)) and (desktop_ar and allowed_file(desktop_ar.filename)) and (mobile_ar and allowed_file(mobile_ar.filename)): 
                
                
                filepath = os.path.join(app.config['UPLOAD_FOLDER'],country_id, "desktop_en.jpeg")
                desktop_en.save(filepath)
                backup_time(country_id=country_id,filepath=filepath,filename="desktop_en.jpeg")
                
                filepath = os.path.join(app.config['UPLOAD_FOLDER'],country_id, "mobile_en.jpeg")
                mobile_en.save(filepath)
                backup_time(country_id=country_id,filepath=filepath,filename="mobile_en.jpeg")
                
                if country_id != "az":
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'],country_id, "desktop_ar.jpeg")
                    desktop_ar.save(filepath)
                    backup_time(country_id=country_id,filepath=filepath,filename="desktop_ar.jpeg")
                    
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'],country_id, "mobile_ar.jpeg")
                    mobile_ar.save(filepath)
                    backup_time(country_id=country_id,filepath=filepath,filename="mobile_ar.jpeg")
                
                return redirect(url_for("thanks"))
            
            else:
                return redirect(url_for("index"))

    else:
      
        countries_list = [{"id": "ae", "name": "UAE"},{"id": "qatar", "name": "Qatar"},{"id": "az", "name": "Azerbaijan"},{"id": "oman", "name": "Oman"},{"id": "bahrain", "name": "Bahrain"}]

        return render_template("index.html",countries_list=countries_list)
            
     
# # Functionality: signup
@app.route('/thanks', methods=['GET'])
def thanks():
  
    
        return render_template("thanks.html")
            
     

if __name__ == '__main__':
    # app.run(host="0.0.0.0")
    
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(BACKUP_FOLDER, exist_ok=True)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],"ae")
    os.makedirs(filepath, exist_ok=True)
    filepath = os.path.join(app.config['BACKUP_FOLDER'],"ae")
    os.makedirs(filepath, exist_ok=True)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],"qatar")
    os.makedirs(filepath, exist_ok=True)
    filepath = os.path.join(app.config['BACKUP_FOLDER'],"qatar")
    os.makedirs(filepath, exist_ok=True)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],"az")
    os.makedirs(filepath, exist_ok=True)
    filepath = os.path.join(app.config['BACKUP_FOLDER'],"az")
    os.makedirs(filepath, exist_ok=True)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],"bahrain")
    os.makedirs(filepath, exist_ok=True)
    filepath = os.path.join(app.config['BACKUP_FOLDER'],"bahrain")
    os.makedirs(filepath, exist_ok=True)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],"oman")
    os.makedirs(filepath, exist_ok=True)
    filepath = os.path.join(app.config['BACKUP_FOLDER'],"oman")
    os.makedirs(filepath, exist_ok=True)
    app.run(debug=True)
