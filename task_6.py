import math

class Point:
    """
    Class representing a point on a 2D plane.

    Attributes:
        x (float): x-coordinate.
        y (float): y-coordinate.
    """

    def __init__(self, coordinates=None):
        """
        Initialize a Point instance.

        Args:
            coordinates (tuple or None): tuple (x, y). If None, initializes at origin (0, 0).
        """
        if coordinates is None:
            self.x = 0
            self.y = 0
        else:
            self.x, self.y = coordinates

    def get_x(self):
        """
        Get the x-coordinate.

        Returns:
            float: x-coordinate.
        """
        return self.x

    def get_y(self):
        """
        Get the y-coordinate.

        Returns:
            float: y-coordinate.
        """
        return self.y

    def distance(self, other):
        """
        Calculate the Euclidean distance between self and another point.

        Args:
            other (Point): another Point instance.

        Returns:
            float: distance between the points.
        """
        d_x = self.x - other.x
        d_y = self.y - other.y
        return math.sqrt(d_x ** 2 + d_y ** 2)

    def sum(self, other):
        """
        Return a new Point which coordinates are the sum of self's and other's coordinates.

        Args:
            other (Point): another Point instance.

        Returns:
            Point: new Point instance with summed coordinates.
        """
        return Point((self.x + other.x, self.y + other.y))

    def __str__(self):
        """
        String representation of the Point.

        Returns:
            str: formatted string "(x, y)".
        """
        return f"point({self.x}, {self.y})"

    def __repr__(self):
        """
        Official string representation of the Point.

        Returns:
            str: representation string.
        """
        return f"Point(({self.x}, {self.y}))"


point_1 = Point((3, -10))
print(point_1)

point_2 = Point()
print(point_2)
print(point_2.get_x())
print(point_2.get_y())

point_3 = Point((-2, 4))
print(point_1.distance(point_3 ))

point_4= point_3.sum(point_1)
print(point_4)
