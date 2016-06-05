from app import app
from flask import render_template
from flask import request
from train_manage import manage
from sliding_window import slidingw
import logging
import json


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Miguel'} # fake user
    return render_template('index.html',title='Home',user=user)

@app.route('/train/set1',  methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def trainset1():
    if request.method == 'GET':
        m = manage()
        d = m.loadPatchData()
        return 'Rows done : '  + str(len(d))

@app.route('/train/set1/next',methods=['GET','POST'])
def trainset1Next():
    m = manage()
    if request.method == 'GET':
        d = m.loadPatchData()
        l = m.getTrain1List()
        sw = slidingw(64,48)
        img = sw.locateNextImg('',d,l)   
        #print 'Training : ' + img
        return render_template('trainloc.html',imgname=img,labels = m.train1Labels,c = d.shape[0], ttl=len(l))
    if request.method == 'POST':
        #print request.json
        #print request.mimetype
        
        content = request.get_json()
        #print content
        row = m.transformData(content)
        print row
        with open('content.json', 'w') as outfile:
            json.dump(row,outfile)
        m.savePatchData(row) 
        return '{"result":"saved"}'
