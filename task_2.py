class NotSleeping:
    """
    Represents a person who is trying to fall asleep and counting sheep.

    Attributes:
        name (str): The name of the person.
        count_sheeps (int): Number of sheep counted.

    Methods:
        add_sheep(): Increments the count of sheep by one.
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



human_1 = NotSleeping("Jhon")
human_1.add_sheep()
human_1.add_sheep()
human_1.add_sheep()
human_1.add_sheep()
human_1.add_sheep()

human_2 = NotSleeping("Alex", 5)
human_2.add_sheep()
human_2.add_sheep()
human_2.add_sheep()

print(human_1.name, "counted", human_1.count_sheeps, "sheep")
print(human_2.name, "counted", human_2.count_sheeps, "sheep")
