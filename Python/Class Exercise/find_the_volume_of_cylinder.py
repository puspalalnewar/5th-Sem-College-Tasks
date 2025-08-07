# Input the height and radius of a cylender to calculate volume

class Cylinder :
    def __init__(self, r, h):
        self.radius = r
        self.height = h
        
    def calculate_volume(self) : 
        return 3.141 * self.radius * self.radius * self.height
    def calc_area(self) :
        return (2 * 3.14 * self.r * self.r) + (2 * 3.14 * self.r * self.h)

c1 = Cylinder(5, 10)
c2 = Cylinder(1, 2)

print(c1.calculate_volume())
print(c2.calc_area())
    