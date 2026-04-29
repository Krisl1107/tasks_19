class StrandsDNA:
    """
    A class to store and manage DNA strands.

    Attributes:
        all_strands (list): A list to store DNA strands.
    """

    def __init__(self):
        """
        Initializes a new instance of the StrandsDNA class.
        """
        self.all_strands = []

    def add_strands(self, strands):
        """
        Adds DNA strands to the collection.

        Args:
            strands (str): A string containing DNA strands separated by spaces.
        """
        new_strands = strands.split()
        self.all_strands.extend(new_strands)

    def get_max_strands(self):
        """
        Retrieves a string of unique, lexicographically sorted DNA strands
        with the maximum length, separated by spaces.

        Returns:
            str: A string containing the maximum length strands, sorted lexicographically and separated by spaces.
        """
        if not self.all_strands:
            return ""

        max_length = max(len(strand) for strand in self.all_strands)

        max_strands = {strand for strand in self.all_strands if len(strand) == max_length}

        return ' '.join(sorted(max_strands))

    def __str__(self):
        """
        Returns a string representation of all DNA strands stored.
        """
        return ' '.join(self.all_strands)

covid_19 = StrandsDNA()
covid_19.add_strands('GAAT ACCGTT TTGAC TGGGAC')
print(covid_19)
covid_19.add_strands('ACCT AGGCT TGGGAC')
covid_19.add_strands('CATTTT TAATTC')
print(covid_19)
print(covid_19.get_max_strands())
