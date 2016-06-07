import os
from PIL import Image
import numpy as np
from random import randint

class slidingw:
	psize=None
	patchsize=None
	lastrow=0
	lastcol=0
	lstFilename ='lst.txt'
	
	def __init__(self,pwidth,pheight):
		self.psize = (pwidth,pheight)
		self.patchsize = (self.psize[0]/10, self.psize[1]/10)
		 
	def getpatch(self,img, row,col):
		a = self.loadimage(img)
		startpos = self.getpatchlocation(row, col)
		return a[startpos[1]:startpos[1] + self.patchsize[1], startpos[0]:startpos[0] + self.patchsize[0]]
	
	def getpatchlocation(self,row,col):
		startr = min(self.patchsize[1] * row/10,90)
		startc = min(self.patchsize[0] * col/10,90)
		return(startc,startr)
		#print 'getpatch not implemented'
	
	def featurePosition(feature, imageName, row,col):
		# for image patches which contain the feature return the following training features
		#	return Y as the specified feature's patch relative x and y 
		#	return X as the image relative x and y positions of the top left corner of the patch
		#	both of these will be scaled
		#	Y is scaled so that 0 is the center of the patch 
		#	-x values are left of center +x values are right of center 
		#	-y values are above center +y values are below center 
		#	h indicates wheter the feature exists in the patch 
		#		-1 indicates it's not found
		#		+1 indicates it is found
		# for image patches which do not contain the feature 
		#	X still contains the image relative x and y positions
		#	Y has -1 for both x and y and -1 for h
		print feature

	def loadimage(self,filename):
		img = Image.open(filename)
		img.load()	  
		data = np.asarray(img, dtype="int32")
		return data

	def locateNextImg(self, setFolder,df,lf):
		names = [self.getFilename(x) for x in lf]
		# find the next image which needs to be annotated
		# load list of imagesi
		# if lf is empty return None
		if len(lf) == 0:
			return None
		# if df is empty, return first item
		if df.shape[0] < 1:
			return self.getFilename(lf[0])
		# if df is not empty find the first item not in dataframe
		imagesdone = df.index.tolist()
		filtered = [i for i in names if not i in imagesdone]
		if len(filtered) > 0 :
			nextitem = filtered[0]
			return nextitem 
		else :
			return None

	def getFilename(self,item):
		return os.path.basename(item)

	def generateIntersectingPatches(self,centerX,centerY,count):
		# create a list of rectangles of a given size(width & height) including the center X and Y
		imgOffsets = []
		patchPositions = []
		for i in range(count):
			# offset is the number of pixels to move the patch or how far the center has moved
			# negative is left/up + is right/down
			offset = (randint(-(self.patchsize[0]/2 -10), self.patchsize[0]/2 -10) ,randint(-(self.patchsize[1]/2) -10, self.patchsize[1]/2 - 10))
			imgPosition = (centerX + offset[0], centerY + offset[1])
			imgOffsets.append(imgPosition)
			patchPositions.append(((imgPosition[0] - self.patchsize[0]/2)/640.0 * 100, (imgPosition[1] - self.patchsize[0]/2)/480.0 * 100, offset[0], offset[1]))
		return patchPositions


		
		
