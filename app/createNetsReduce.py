#!/usr/bin/python

from train_manage import manage
from sliding_window import slidingw
import sys
import numpy as np
import os

class net_reducer:
	d = {}
	folder = 'static/train1Imgs/net'
	m = manage()
	s = slidingw(640.0, 480.0)
	
	def initial_setup(self):
		files = os.listdir(self.folder) 
		for file in files:
			if file.endswith(".net"):
				os.remove(os.path.join(self.folder,file))
	def process_line(self,data):
			if data[1] not in self.d:
				self.d[data[1]] = []
			#print data[0] + data[1] + data[2]
			try:
				p = self.s.getpatch('static/train1Imgs/' + data[0],float(data[2]),float(data[3]))
				pixels = p.shape[0] * p.shape[1]
				if pixels == self.s.patchsize[0] * self.s.patchsize[1]:
					p = np.reshape(p, p.shape[0] * p.shape[1])
					self.d[data[1]].append( ' '.join(map(str,p[1:10])))
				else:
					print 'Invalid pixels size for : ' + data[0] + ' ' + str(float(data[2])) + ',' + str(float(data[3])) + ' size : ' +  str(pixels)
			except:
				e = sys.exc_info()[0]
				print 'error in getpatch ' + data[0] + str(data[2]) + str(data[3])
		
	def write_net_files(self):
		print 'not implemented'
				

def main(argv):
	nr = net_reducer()
	nr.initial_setup()
	for line in sys.stdin:
		try:
			data = line.split(',')
			nr.process_line(data)
		except :
			e = sys.exc_info()[0]
			print 'error ' + str( e)
	for key,value in nr.d.iteritems():
		print key + ' : ' +  str(len(value))
if __name__ == "__main__":
	main(sys.argv)
