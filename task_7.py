class TrafficLight:
    """
    Class representing a traffic light with cyclic signals.

    Attributes:
        permissible_values (list): class attribute listing possible signals in order.
        current_signal (str): current signal of the traffic light instance.
    """

    permissible_values = ['green', 'yellow', 'red', 'yellow']

    def __init__(self):
        """
        Initialize the traffic light with the green signal.
        """
        self.current_index = 0
        self.current_signal = self.permissible_values[self.current_index]

    def next_signal(self):
        """
        Change the current signal to the next in order.
        """
        self.current_index = (self.current_index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[self.current_index]


seven_roads = TrafficLight()
print(seven_roads.current_signal)

for _ in range(5):
    seven_roads.next_signal()
    print(seven_roads.current_signal)
