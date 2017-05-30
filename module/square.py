from module.exampleClass import Shape

class Square(Shape):

    def __init__(self, _sqLength):
        self.sqLength=_sqLength
        self.setArea()
        
    def setArea(self):
        self.area=self.sqLength*self.sqLength