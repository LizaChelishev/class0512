# Exactly the same program besides the 'radius' our static variablle is not in a function

class Circle:
    pie = 3.14

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def get_area(self):
        area = self.radius ** 2 * Circle.pie
        print(f'The area is {area}')
