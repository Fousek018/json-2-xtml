import csv
import requests
import os
import random
import json
import urllib2
import dicttoxml
from flask import Flask,jsonify,render_template,make_response
'''https://github.com/newnewcoder/flask-chartjs-demo'''
os.environ['no_proxy']='*'

app = Flask(__name__)

def wpjson():
    r= urllib2.urlopen('https://blog.iservery.com/wp-json/wp/v2/posts')
    data=json.load(r)
    pole=[]
    for radek in data:
        inradek=dict(nadpis=radek['title']['rendered']+'Petr',text=radek['content']['rendered'])
        #inradek={'nadpis':'data','text':'data'}
        pole.append(inradek)
    return pole

@app.route('/json')
def jsex():
    return jsonify(list=wpjson())
@app.route('/xml')
def xmlex():
    list = wpjson()
    xml = dicttoxml.dicttoxml(list)
    response = make_response(xml, 200)
    response.headers['Content-Type'] = 'application/xml'
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)