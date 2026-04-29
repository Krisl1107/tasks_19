class User:
    """
    Represents a website user.

    Attributes:
        id (int): Unique user ID.
        nick_name (str): User's nickname.
        first_name (str): User's first name.
        last_name (str, optional): User's last name.
        middle_name (str, optional): User's middle name.
        gender (str, optional): User's gender.
    """

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        """
        Initialize a User instance.

        Args:
            id (int): Unique user ID.
            nick_name (str): User's nickname.
            first_name (str): User's first name.
            last_name (str, optional): User's last name. Defaults to None.
            middle_name (str, optional): User's middle name. Defaults to None.
            gender (str, optional): User's gender. Defaults to None.
        """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender


    def update(self, id='', nick_name='', first_name='', last_name='', middle_name='', gender=''):
        """
        Update user attributes with provided values.

        Only attributes with non-None arguments will be updated.

        Args:
            id (int, optional): New user ID.
            nick_name (str, optional): New nickname.
            first_name (str, optional): New first name.
            last_name (str, optional): New last name.
            middle_name (str, optional): New middle name.
            gender (str, optional): New gender.
        """
        if id != '':
            self.id = id
        if nick_name != '':
            self.nick_name = nick_name
        if first_name != '':
            self.first_name = first_name
        if last_name != '':
            self.last_name = last_name
        if middle_name != '':
            self.middle_name = middle_name
        if gender != '':
            self.gender = gender


    def full_name(self):
        """
        Construct and return full name by concatenating last name, first name, and middle name.

        Returns:
            str: Full name with parts separated by spaces. Missing parts are skipped.
        """
        parts = [self.last_name, self.first_name, self.middle_name]
        return " ".join(part for part in parts if part)


    def __str__(self):
        """
        Return string representation of the user.

        Format:
        ID: {id} LOGIN: {nick_name} NAME: {full_name} [GENDER: {gender}]

        The "GENDER: ..." part is included only if gender is present.

        Returns:
            str: User info string.
        """
        gender_part = f" GENDER: {self.gender}" if self.gender else ""
        return (f"ID: {self.id} "
                f"LOGIN: {self.nick_name} "
                f"NAME: {self.full_name()}"
                f"{gender_part}")




user_1 = User(12, 'alex', 'Алексей')
print(user_1)

user_2 = User(44, 'andru', 'Андрей', 'Петров')
print(user_2)

user_3 = User(25, 'nik', 'Николай', 'Иванов', 'Федорович')
print(user_3)

user_4 = User(61, 'ivan', 'Денис', 'Сидоров', 'Алексеевич', 'M')
print(user_4)

user_5 = User(47, 'ann', 'Анна', gender='F')
print(user_5)

user_4.update(0, '', 'Ваня')
print(user_4)

user_3.update(15, '', 'Никита', '', 'Петрович')
print(user_3)

users = []
users.append(user_2.nick_name)
users.append(user_4.nick_name)
users.append(user_5.nick_name)
users.append(user_1.nick_name)
users.append(user_3.nick_name)
print(users)
