class Circle:
    def __init__(self, radius):
        self.pie = 3.14
        self.radius = radius

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def get_area(self, radius, pie):
        area = radius ** 2 * pie
        print(f'The area is {area} ')
