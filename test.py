import csv
import requests
import os
from flask import jsonify,Flask
os.environ['no_proxy']='*'
app = Flask(__name__)

@app.route('/')
def jsonout():
    r = requests.get('http://192.168.10.1/data.csv')
    data = r.text
    POLE={'data':[]}
    for line in csv.DictReader(data.splitlines(),skipinitialspace=True):
        POLE['data'].append({'Jmeno':line['Jmeno'],
                         'Age':line['Age']})

    return jsonify(POLE)

@app.route('/chart')
def chart
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)