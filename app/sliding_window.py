import os
class slidingw:
    psize=None
    lastrow=0
    lastcol=0
    lstFilename ='lst.txt'
    def __init__(self,pwidth,pheight):
        self.psize = (pwidth,pheight)
        
    def getpatch(self,img, row,col):
        # retrieve the specific patch from the image specified
        print 'getpatch not implemented'
    def locateNextImgSet(self, setFolder):
        # find the next image which needs to be annotated
        # load list of images
        p = os.path.join(setFolder,self.lstFilename)

        print p
