class NotSleeping:
    """
    Represents a person who is trying to fall asleep by counting sheep.

    Attributes:
        name (str): The name of the person.
        count_sheeps (int): Number of sheep counted.

    Methods:
        add_sheep(): Increment the count of sheep by one.
        lost(): Reset the sheep count to zero.
        get_count_sheeps(): Return the current count of sheep.
    """

    def __init__(self, name, number=0):
        """
        Initialize a NotSleeping instance.

        Args:
            name (str): Name of the person.
            number (int, optional): Initial sheep count. Defaults to 0.
        """
        self.name = name
        self.count_sheeps = number

    def add_sheep(self):
        """
        Increase the number of counted sheep by one.
        """
        self.count_sheeps += 1

    def lost(self):
        """
        Reset the counted sheep to zero.
        """
        self.count_sheeps = 0

    def get_count_sheeps(self):
        """
        Return the current number of counted sheep.

        Returns:
            int: number of sheep counted
        """
        return self.count_sheeps



human = NotSleeping("Alex")
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()

print(human.name, "counted", human.count_sheeps, "sheep")

human.add_sheep()
human.lost()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()

print(human.name, "counted", human.get_count_sheeps(), "sheep")
