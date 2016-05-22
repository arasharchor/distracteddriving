from app import app
from flask import render_template
from flask import request
from train_manage import manage

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
    
