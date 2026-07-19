#polymorphism -> getter/setter /data mangling / 
#vectors -> basic operations!
#class works as a blueprint for creating objects
"""import math


class Vector2D:
    def __init__(self, x_comp, y_comp):
        self.__x_comp = x_comp
        self.__y_comp = y_comp

    @property
    def coordinates(self):
        return self.__x_comp, self.__y_comp

    @coordinates.setter
    def coordinates(self, value):
        self.__x_comp = value[0]
        self.__y_comp = value[1]

    @property
    def magnitude(self):
        return math.sqrt(self.__x_comp**2 + self.__y_comp**2)

    def __str__(self):
        return f'({self.__x_comp}i + {self.__y_comp}j)'


vector = Vector2D(1, 3)
print(vector.coordinates, vector.magnitude)
vector.coordinates = (1, 7)
print(vector.coordinates, vector.magnitude)
"""






#Better way to validate the coordinates

import math


class InvalidCoordinateValidator:
    def __init__(self, value):
        self.value = value
        self.message = None
        if not isinstance(value, tuple):
            self.message = "Coordinates should be a tuple in Nature."
        if len(value) > 2:
            self.message = "Coordinates should be a tuple not Exceeding length 2."

    def __str__(self):
        return f'Error: {self.message} | value: {self.value}'


class Vector2D:
    def __init__(self, x_comp, y_comp):
        self.__x_comp = x_comp
        self.__y_comp = y_comp

    @property
    def coordinates(self):
        return self.__x_comp, self.__y_comp

    @coordinates.setter
    def coordinates(self, value):
        ice = InvalidCoordinateValidator(value)
        if ice.message is not None:
            raise ValueError(ice.message)

        if len(value) == 0:
            self.__x_comp, self.__y_comp = 0, 0
        elif len(value) == 1:
            self.__x_comp, self.__y_comp = value[0], 0
        else:
            self.__x_comp, self.__y_comp = value[0], value[1]

    @property
    def magnitude(self):
        return math.sqrt(self.__x_comp**2 + self.__y_comp**2)

    def __str__(self):
        return f'({self.__x_comp}i + {self.__y_comp}j)'


vector = Vector2D(1, 3)
print(vector.coordinates, vector.magnitude)
vector.coordinates = (7, 5)
print(vector.coordinates, vector.magnitude)

