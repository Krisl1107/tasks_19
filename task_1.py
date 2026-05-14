class Circle:
    """
    Represents a circle with a specified radius.

    Class Attributes:
        pi (float): The mathematical constant Pi, used for calculations.
        all_circles (list): A list to keep track of all instantiated Circle objects.

    Instance Attributes:
        radius (float): The radius of the circle.
    """

    pi = 3.1415
    all_circles = []

    def __init__(self, radius=1):
        """
        Initializes a new Circle instance with a given radius.

        Args:
            radius (float, optional): The radius of the circle. Defaults to 1.
        """
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return Circle.pi * (self.radius ** 2)

    @staticmethod
    def total_area():
        return sum(circle.area() for circle in Circle.all_circles)

    def __str__(self):
        return str(self.radius)

    def __repr__(self):
        return str(self.radius)

c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)
print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))
