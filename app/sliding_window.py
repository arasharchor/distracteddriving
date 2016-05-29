import os
class slidingw:
    psize=None
    lastrow=0
    lastcol=0
    lstFilename ='lst.txt'
    allFeatures = ['rEar','topHead','tipNose','rEye','lEye','tipChin','rElbow','rShoulderSocket','rWrist','lElbow','lShoulderSocket','centerSteering','leftBottomWindow']
    def __init__(self,pwidth,pheight):
        self.psize = (pwidth,pheight)
        
    def getpatch(self,img, row,col):
        # retrieve the specific patch from the image specified
        print 'getpatch not implemented'
    
    def locateNextImg(self, setFolder,df,lf):
        names = [self.getFilename(x) for x in lf]
        print names[0]
        # find the next image which needs to be annotated
        # load list of imagesi
        # if lf is empty return None
        if len(lf) == 0:
            return None
        # if df is empty, return first item
        if df.shape[0] < 1:
            return self.getFilename(lf[0])
        # if df is not empty find the first item not in dataframe
        imagesdone = df.image.tolist()
        filtered = [i for i in names if not i in imagesdone]
        if len(filtered) > 0 :
            nextitem = filtered[0]
            idx = idxname.index(nextitem)
            return self.getFilename(lf[idx])
        else :
            return None
        # if item is in df but does not have all features set, return it
        #df[~df.image.isin(lf)]
        print ''

    def getFilename(self,item):
        return os.path.basename(item)
