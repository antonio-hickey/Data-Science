from flask import Flask
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

data = pd.read_csv("../back end/Projections.csv")
print(data.columns[0])

@app.route('/hello')
def say_hello_world():
    return {'result': "Fuck off"}
    
@app.route('/heading1')
def heading1():
    return {'heading': data.columns[0]}

@app.route('/heading2')
def heading2():
    return {'heading2': data.columns[1]}

@app.route('/heading3')
def heading3():
    return {'heading3': data.columns[2]}

@app.route('/f1c1')
def f1_c1():
    return {'f1c1': str(data['Fight #'].loc[0])}

@app.route('/f1c2')
def f1_c2():
    return {'f1c2': data['Projected Winner'].loc[0]}

@app.route('/f1c3')
def f1_c3():
    return {'f1c3': data['Odds'].loc[0]}

@app.route('/f2c1')
def f2_c1():
    return {'f2c1': str(data['Fight #'].loc[1])}

@app.route('/f2c2')
def f2_c2():
    return {'f2c2': data['Projected Winner'].loc[1]}

@app.route('/f2c3')
def f2_c3():
    return {'f2c3': data['Odds'].loc[1]}

@app.route('/f3c1')
def f3_c1():
    return {'f3c1': str(data['Fight #'].loc[2])}

@app.route('/f3c2')
def f3_c2():
    return {'f3c2': data['Projected Winner'].loc[2]}

@app.route('/f3c3')
def f3_c3():
    return {'f3c3': data['Odds'].loc[2]}

@app.route('/f4c1')
def f4_c1():
    return {'f4c1': str(data['Fight #'].loc[3])}

@app.route('/f4c2')
def f4_c2():
    return {'f4c2': data['Projected Winner'].loc[3]}

@app.route('/f4c3')
def f4_c3():
    return {'f4c3': data['Odds'].loc[3]}

@app.route('/f5c1')
def f5_c1():
    return {'f5c1': str(data['Fight #'].loc[4])}

@app.route('/f5c2')
def f5_c2():
    return {'f5c2': data['Projected Winner'].loc[4]}

@app.route('/f5c3')
def f5_c3():
    return {'f5c3': data['Odds'].loc[4]}