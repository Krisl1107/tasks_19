class Point:
    """
    Represents a point on a 2D plane.

    Attributes:
        x (float): The x-coordinate.
        y (float): The y-coordinate.
    """

    def __init__(self, coordinates=None):
        """
        Initializes a Point instance.

        Args:
            coordinates (tuple or None): A tuple (x, y). If None, defaults to (0,0).
        """
        if coordinates is None:
            self.x = 0
            self.y = 0
        else:
            self.x, self.y = coordinates

    def __str__(self):
        """
        Returns a string representation of the point in the format '(x; y)'.

        Returns:
            str: The formatted string.
        """
        return f"({self.x}; {self.y})"


class Segment:
    """
    Represents a line segment defined by two points on the plane.

    Attributes:
        start_point (Point): The starting point of the segment.
        end_point (Point): The ending point of the segment.
        one_intersection (bool): True if the segment intersects exactly one axis, False otherwise.
    """

    def __init__(self, point1, point2):
        """
        Initializes a Segment instance with two Point objects.

        Args:
            point1 (Point): The first endpoint of the segment.
            point2 (Point): The second endpoint of the segment.
        """
        self.start_point = point1
        self.end_point = point2
        self.one_intersection = self.one_axis_intersection()

    def one_axis_intersection(self):
        """
        Determines if the segment intersects exactly one axis (X or Y).

        Returns:
            bool: True if it intersects exactly one axis, False otherwise.
        """
        x_1, y_1 = self.start_point.x, self.start_point.y
        x_2, y_2 = self.end_point.x, self.end_point.y


        intersects_x = (x_1 * x_2 < 0) or (x_1 == 0 and x_2 != 0) or (x_1 != 0 and x_2 == 0)
        intersects_y = (y_1 * y_2 < 0) or (y_1 == 0 and y_2 != 0) or (y_1 != 0 and y_2 == 0)

        return intersects_x != intersects_y

    def __str__(self):
        """
        Returns a string representation of the segment in the format '((x1; y1), (x2; y2))'.

        Returns:
            str: The formatted string.
        """
        return f"({self.start_point}, {self.end_point})"


class CoordinateSystem:
    """
    Represents a coordinate system containing multiple line segments.

    Attributes:
        segments (list): List of Segment objects on the plane.
    """

    def __init__(self):
        """
        Initializes an empty CoordinateSystem.
        """
        self.segments = []

    def add_segment(self, segment):
        """
        Adds a segment to the coordinate system.

        Args:
            segment (Segment): The segment to add.
        """
        self.segments.append(segment)

    def axis_intersection(self):
        """
        Counts how many segments intersect exactly one axis.

        Returns:
            int: The number of segments intersecting only one axis.
        """
        return sum(1 for segment in self.segments if segment.one_intersection)

    def __str__(self):
        """
        Returns a string listing all segments contained in the coordinate system.

        Returns:
            str: The string representation of the segments list.
        """
        return f"[{', '.join(str(segment) for segment in self.segments)}]"



p1 = Point((-2, 7))
print(p1)
p2 = Point((3, 4))
s1 = Segment(p1, p2)
print(s1)
print(s1.one_intersection)
xy = CoordinateSystem()
xy.add_segment(s1)
p3 = Point((2, -8))
p4 = Point((4, 16))
s2 = Segment(p3, p4)
xy.add_segment(s2)
xy.add_segment(Segment(p4, p2))
xy.add_segment(Segment(Point((-5, 3)), Point((-13, -6))))
print(xy)
print(xy.axis_intersection())
