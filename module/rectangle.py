from module.exampleClass import Shape

class Rectangle(Shape):
    
    def __init__(self, _height, _width):
        self.height=_height
        self.width=_width
        self.setArea()
        
    def setArea(self):
        self.area=(self.height*self.width)