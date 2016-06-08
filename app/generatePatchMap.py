#!/usr/bin/python
from train_manage import manage
from sliding_window import slidingw
import sys
import json
class mapper:
	m = manage()
	df = m.loadPatchData()
	s = slidingw(640.0,480.0)
	litems = []
	patches = []
	cnt = 5
	def perform_map(self):
		for l in self.m.train1Labels:
			for row in self.df.itertuples():
				if getattr(row,'Image'):
					X = {'Image':getattr(row,'Image'),'x':getattr(row,l + '_X'),'y':getattr(row,l + '_Y')}
					X['PatchPositions'] = self.s.generateIntersectingPatches(X['x'],X['y'],self.cnt)
					X['Label'] = l
					self.litems.append(X)
					
		
def main(args):
	m = mapper()
	m.perform_map()
	for x in m.litems:
		print json.dumps(x)

if __name__ == "__main__":
	main(sys.argv)

