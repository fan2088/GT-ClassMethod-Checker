from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
import json
from backend.get_csv import get_data_csv
from backend.csv_to_json import CSV_TO_JSON
from backend.finder import find_valid_result

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CSV_File_Path = './result.csv'
Json_File_Path = './result.json'
DEFAULT_MAJOR = 'Accounting'

@app.route('/', methods=['GET'])
def index():
    get_data_csv(DEFAULT_MAJOR, "Fall 2020")
    CSV_TO_JSON(CSV_File_Path, Json_File_Path)
    with open(Json_File_Path) as json_file:
        data = json.load(json_file)
    return render_template('index.html', content = data, subject = DEFAULT_MAJOR)

@app.route('/', methods=['POST'])
def search():
    req = request.form
    subject = req['subjectName']
    className = req['className']
    sectionName = req['sectionName']
    global DEFAULT_MAJOR
    if (subject != DEFAULT_MAJOR):
        get_data_csv(subject, "Fall 2020")
        CSV_TO_JSON(CSV_File_Path, Json_File_Path)
    with open(Json_File_Path) as json_file:
        data = json.load(json_file)
    if className == '' and sectionName == '':
        result = data
    else:
        result = find_valid_result(data, className, sectionName)
    DEFAULT_MAJOR = subject
    return render_template('index.html', content = result, subject=DEFAULT_MAJOR)

if __name__=="__main__":
    app.run(debug=True)
