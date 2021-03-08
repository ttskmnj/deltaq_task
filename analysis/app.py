from flask import Flask, request
import pandas as pd
import json


app = Flask(__name__)

@app.route('/analyse', methods=['POST'])
def get_analyse():
    # get uploaded csv file
    f = request.files['upload_file']

    # read csv to dataframe
    df = pd.read_csv(f)

    # convert dataframe index to json
    result = json.dumps(df.index.to_list())
    
    return result
