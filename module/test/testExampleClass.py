import unittest
from module.square import Square
from module.triangle import Triangle
from module.exampleClass import Rectangle

class TestSquare(unittest.TestCase):
    
  
    def setUp(self):
        unittest.TestCase.setUp(self)
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testTestFunc(self):
        self.assertEqual(25, Square(5).getArea(), 'Outputs do NOT match')
        self.assertEqual(36, Square(6).getArea(), 'Outputs do NOT match')    
    
class TestRectangle(unittest.TestCase):
    
  
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testTestFunc(self):
        self.assertEqual(24, Rectangle(6,4).getArea(), 'Outputs do NOT match')
        self.assertEqual(32, Rectangle(8,4).getArea(), 'Outputs do NOT match')
        
class TestTriangle(unittest.TestCase):
    
  
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testTestFunc(self):
        self.assertEqual(12, Triangle(6,4).getArea(), 'Outputs do NOT match')
        self.assertEqual(16, Triangle(8,4).getArea(), 'Outputs do NOT match')
        

if __name__ == '__main__':
    unittest.main()