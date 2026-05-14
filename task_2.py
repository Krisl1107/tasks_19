class NavalBattle:
    """
    The NavalBattle class implements the logic for a simple sea battle game
    on a 10x10 playing field.

    Class Attributes:
        playing_field (list[list[int | str]]): A 10x10 grid for the game.
    """
    playing_field: list[list[int | str]] = [[0 for _ in range(10)] for _ in range(10)]

    def __init__(self, player: str) -> None:
        """
        Initializes a NavalBattle player.

        Args:
            player (str): The symbol representing the player ("X", "Y", etc.).
        """
        self.player = player

    @staticmethod
    def show() -> None:
        """
        Displays the current state of the playing field.
        Ships and hidden cells are represented with '~',
        hits with a player symbol, and misses with 'o'.
        """
        print("   " + " ".join(str(num) for num in range(1, 11)))
        for coord_y in range(10):
            rows = []
            for coord_x in range(10):
                cell = NavalBattle.playing_field[coord_y][coord_x]
                if isinstance(cell, str):
                    rows.append(cell)
                elif cell == 1 or cell == 0:
                    rows.append("~")
                else:
                    rows.append("~")
            print(f"{coord_y + 1:2} " + " ".join(rows))

    def shot(self, x: int, y: int) -> None:
        """
        Shoots at the given coordinates on the playing field.

        Args:
            x (int): The column (1-10).
            y (int): The row (1-10).

        Raises:
            ValueError: If the coordinates are out of bounds
                        or cell is defined incorrectly.
        """
        if not (1 <= x <= 10 and 1 <= y <= 10):
            raise ValueError("Coordinates must be from 1 to 10.")

        coord_y, coord_x = y - 1, x - 1

        cell = NavalBattle.playing_field[coord_y][coord_x]

        if isinstance(cell, str):
            print("This cell has already been shot at!")
            return
        if cell == 1:
            NavalBattle.playing_field[coord_y][coord_x] = self.player
            print("hit")
        elif cell == 0:
            NavalBattle.playing_field[coord_y][coord_x] = "o"
            print("miss")
        else:
            raise ValueError("Cell defined incorrectly.")


NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1 = NavalBattle('#')
player2 = NavalBattle('*')
NavalBattle.show()
player1.shot(6, 2)
player1.shot(6, 1)
player2.shot(6, 3)
player2.shot(6, 4)
player2.shot(6, 5)
player2.shot(3, 3)
player2.show()
player1.shot(1, 1)
NavalBattle.show()
