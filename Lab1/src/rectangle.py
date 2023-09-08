"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""

class Shape:
    def set_values(self):
        pass
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width=None, height=None):
        self._width = width
        self._height = height
        
    def set_values(self, x, y):
        self.width = x
        self.height = y

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
