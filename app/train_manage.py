from os import path
import pandas as pd
import json

class manage:
    train1Folder = 'static/train1Imgs'
    workingdir = '/usr/local/hadoop/project/sfddd/app'
    train1patchdata = 'patchdata.json'
 
    def getTrain1List(self):
        lines =[]
        wd = path.join(self.workingdir,self.train1Folder)
        with open(path.join(wd,'lst.txt')) as f:
            lines=f.read().split()
        return lines

    def loadPatchData(self):
        p = path.join(path.join(self.workingdir,self.train1patchdata),self.train1patchdata)
        df = None
        if not path.exists(p):
            df = pd.DataFrame(columns=[['image','patchr','patchc','feature']])
        else :
           df  = pd.read_json(p) 
        return df
    def savePatchData(self,df):
        p = path.join(path.join(self.workingdir,self.train1Folder),self.train1patchdata)
        df.to_json(p)
        print "saved " + p
    
    def getBasename(self,lst):
        l = [path.basename(x) for x in lst]
        return l
