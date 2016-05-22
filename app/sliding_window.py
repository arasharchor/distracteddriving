class slidingw:
    psize=None
    lastrow=0
    lastcol=0
    def __init__(self,pwidth,pheight):
        self.psize = (pwidth,pheight)
        
    def getpatch(self,img, row,col):
        
