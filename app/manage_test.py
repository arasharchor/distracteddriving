import unittest
from  train_manage import manage

class ManageTest(unittest.TestCase):
    def setup(self):
        pass
    def test_trainset1Rows(self):
        x = manage()
        l = x.getTrain1List()
        print l[0:3]
        self.assertEqual(len(l) > 0,True)

if __name__ == '__main__':
    unittest.main()
