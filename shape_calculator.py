class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * (self.height + self.width))

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    def get_picture(self):
        text = ""
        if self.height < 51 and self.width < 51:
            for i in range(self.height):
                for j in range(self.width):
                    text += "*"
                text += "\n"    
            return text
        else:
            return  "Too big for picture."

    def get_amount_inside(self, shape):
       return (self.get_area() // (shape.height * shape.width))

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __repr__(self):
    return f"Square(side={self.width})"

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.set_side(side)

  def set_height(self, side):
    self.set_side(side)
