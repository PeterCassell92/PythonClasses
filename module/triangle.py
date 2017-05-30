from module.exampleClass import Shape
class Triangle(Shape):
    
    def __init__(self, _height, _base):
        self.height=_height
        self.base=_base
        self.setArea()
    
    def setArea(self):
        self.area=(self.height*self.base)/2