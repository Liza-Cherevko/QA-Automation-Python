class Rhombus:
    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a
        self.corner_b = 180 - corner_a

    def __setattr__(self, name, value):

        if name == "side_a":
            if value <= 0:
                raise ValueError("Side must be greater than 0")

        if name == "corner_a":
            if value <= 0 or value >= 180:
                raise ValueError("Angle must be between 0 and 180")

        if name == "corner_b":
            if value <= 0 or value >= 180:
                raise ValueError("Angle must be between 0 and 180")

        object.__setattr__(self, name, value)

        if name == "corner_a":
            object.__setattr__(self, "corner_b", 180 - value)

    def get_data(self):
        print(self.side_a, self.corner_a, self.corner_b)


test = Rhombus(5, 60)
test.get_data()