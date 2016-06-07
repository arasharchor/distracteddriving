import unittest
import views

class ViewsTest(unittest.TestCase):
    def trainset1Rows(self):
        x = trainset1()
        self.assertEqual("Rows" in x,True)

if __name == '__main__':
    unittest.main()
