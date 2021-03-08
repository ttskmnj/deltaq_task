import os
import requests
from flask import Flask
import pandas as pd
import json
import os


app = Flask(__name__)
path = "/app/api/datas/"
analysis_path = os.environ.get('ANALYSIS')

@app.route('/csvfiles', methods=['GET'])
def get_csvfiles():
    # get all files uneder datas directory
    dirs = os.listdir( path )
    
    return json.dumps(dirs)


@app.route('/sendcsv/<csvfile>', methods=['GET'])
def send_csv(csvfile):
    url = f"{analysis_path}:5001/analyse"

    # prepare csv file to send
    file = {'upload_file': open(path + csvfile,'rb')}

    # send csv request to Analysis server via post
    r = requests.post(url, files=file)

    return r.content
