from os import path
import pandas as pd
import json

class manage:
    train1Folder = 'static/train1Imgs'
    workingdir = '/usr/local/hadoop/project/sfddd/app'
    train1patchdata = 'patchdata.json'
    train1patchcsv = 'trainlabels.json'
    train1Labels = ['TipNose','RightEar','RightEye','RightElbow','RightWrist','CenterSteering','LeftWrist']
    def __init__ (self):
        self.train1Labels.sort()
    
    def getTrain1List(self):
        lines =[]
        wd = path.join(self.workingdir,self.train1Folder)
        with open(path.join(wd,'lst.txt')) as f:
            lines=f.read().split()
        return lines

    def loadPatchData(self):
        p = path.join(path.join(self.workingdir,self.train1Folder),self.train1patchdata)
        df = None
        if not path.exists(p):
            header = self.createHeader()
            df = pd.DataFrame(columns=header)
        else :
           df  = pd.read_json(p) 
        return df
    
    def savePatchData(self,row):
        p = path.join(path.join(self.workingdir,self.train1Folder),self.train1patchdata)
       
        if path.exists(p):
            df =  pd.read_json(p)
            rdf = pd.DataFrame(row)
            rdf.index = [row[0]['Image']]
            #df = df.set_index('Image')
            #row = row.set_index('Image')
            df = df.append(rdf)
        else:
            header = self.createHeader()
            df = pd.DataFrame(row,columns=header)
            df = df.set_index('Image')
        
        df.to_json(p)
        print "Saved to :" + p
    
    def getBasename(self,lst):
        l = [path.basename(x) for x in lst]
        return l

    def createHeader(self):
        header = ['Image']
        for r in self.train1Labels:
            header.append('{}_X'.format(r))
            header.append('{}_Y'.format(r))
        return tuple(header)

    def createHeadeFromJson(self,rows):
        header=['Image']
        for r in rows:
            header.append('{}_X'.format(r['Label']))
            header.append('{}_Y'.format(r['Label']))
        return tuple(header)
    
    def transformData(self,rows):
        l = []
        obj = {'Image': rows[0]['Image']}
        for r in rows:
            obj['{}_X'.format(r['Label'])] = '{}'.format(r['X'])
            obj['{}_Y'.format(r['Label'])] = '{}'.format(r['Y'])
        l.append(obj)
        return l

