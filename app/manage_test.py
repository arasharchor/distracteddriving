import unittest
import os
from  train_manage import manage
import pandas as pd

class ManageTest(unittest.TestCase):
    m = None
    testResults = ''

    def setUp(self):
        self.m = manage()
        wd = os.getcwd()
        self.m.workingdir = wd
        self.m.train1Folder = 'testResults'
        self.testResults = os.path.join(self.m.workingdir, self.m.train1Folder)
        if not os.path.exists(self.testResults):
            os.mkdir(self.testResults)
        l = ['a','b','c']
        with open(os.path.join(self.testResults,'lst.txt'),'w+') as f:
            for x in l:
                f.write("%s\n" % x)
        pass
    def tearDown(self):
        if os.path.exists(self.testResults):
            os.remove(os.path.join(self.testResults,'lst.txt'))

    def test_trainset1Rows(self):
        l = self.m.getTrain1List()
        print l[0:3]
        self.assertEqual(len(l) > 0,True)

    def test_savePatchData(self):
        # savePatchData should save a file 
        item = {'image':['img_10420.jpg'],'patchr':[1],'patchc':[1],'feature':['none']}
        fileTest = os.path.join(self.testResults,self.m.train1patchdata)
        d = pd.DataFrame(item)
        self.m.savePatchData(d)
        self.assertEqual(os.path.exists(fileTest),True)
        print fileTest
    def test_basename(self):
        l = ['/mnt/tmp/some.bn','/mnt/x.y']
        tmp = self.m.getBasename(l)
        self.assertEqual(tmp[0] == 'some.bn',True)
        self.assertEqual(tmp[1] == 'x.y',True)        
if __name__ == '__main__':
    unittest.main()
