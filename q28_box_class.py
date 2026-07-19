

class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def surface_area(self):
        return 2 * (self.width * self.height +
                    self.width * self.depth +
                    self.height * self.depth)

box1 = Box(2, 3, 4)
box2 = Box(5, 5, 5)

print(f"Box 1 -> Volume: {box1.volume()}, Surface Area: {box1.surface_area()}")
print(f"Box 2 -> Volume: {box2.volume()}, Surface Area: {box2.surface_area()}")
