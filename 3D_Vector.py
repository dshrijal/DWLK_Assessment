import math


class InvalidCoordinateValidator:
    def __init__(self, value):
        self.value = value
        self.message = None

        if not isinstance(value, tuple):
            self.message = "Coordinates should be a tuple."

        elif len(value) > 3:
            self.message = "Coordinates should not exceed length 3."

    def __str__(self):
        return f"Error: {self.message} | Value: {self.value}"


class Vector3D:
    def __init__(self, x_comp, y_comp, z_comp):
        self.__x_comp = x_comp
        self.__y_comp = y_comp
        self.__z_comp = z_comp

    @property
    def coordinates(self):
        return self.__x_comp, self.__y_comp, self.__z_comp

    @coordinates.setter
    def coordinates(self, value):
        validator = InvalidCoordinateValidator(value)

        if validator.message is not None:
            raise ValueError(validator.message)

        if len(value) == 0:
            self.__x_comp, self.__y_comp, self.__z_comp = 0, 0, 0

        elif len(value) == 1:
            self.__x_comp, self.__y_comp, self.__z_comp = value[0], 0, 0

        elif len(value) == 2:
            self.__x_comp, self.__y_comp, self.__z_comp = value[0], value[1], 0

        else:
            self.__x_comp, self.__y_comp, self.__z_comp = value

    @property
    def magnitude(self):
        return math.sqrt(
            self.__x_comp ** 2 +
            self.__y_comp ** 2 +
            self.__z_comp ** 2
        )

    def __str__(self):
        return f"({self.__x_comp}i + {self.__y_comp}j + {self.__z_comp}k)"


# -------------------------
# Testing
# -------------------------

vector = Vector3D(1, 2, 3)

print(vector)
print("Coordinates:", vector.coordinates)
print("Magnitude:", vector.magnitude)

print()

vector.coordinates = ()
print(vector)

vector.coordinates = (7,)
print(vector)

vector.coordinates = (7, 8)
print(vector)

vector.coordinates = (7, 8, 9)
print(vector)

print("Coordinates:", vector.coordinates)
print("Magnitude:", vector.magnitude)