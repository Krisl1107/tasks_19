import random


class NavalBattle:
    """
    A class that implements a simplified version of a Battleship game.
    """
    playing_field = None
    field_initialized = False

    def __init__(self, player_symbol):
        """
        Initialize a player.

        :param player_symbol: Symbol to mark hits by this player
        """
        self.player_symbol = player_symbol

    @staticmethod
    def show():
        """
        Static method to display the playing field.

        "~" - Hidden cells (not fired)
        "o" - Missed shots
        player symbol - hits by this player
        """
        if NavalBattle.playing_field is None:
            print("игровое поле не заполнено")
            return

        print("   " + " ".join(str(i) for i in range(1, 11)))
        print("  " + "-" * 20)

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
            print(f"{coord_y + 1:2} |" + " ".join(rows))
        print()

    @classmethod
    def new_game(cls):
        """
        Class method that creates a new playing field with randomly placed ships.
        """
        cls.playing_field = [[0 for _ in range(10)] for _ in range(10)]

        ships = {
            4: 1,
            3: 2,
            2: 3,
            1: 4
        }

        for size, count in ships.items():
            for _ in range(count):
                placed = False
                attempts = 0
                while not placed and attempts < 1000:
                    placed = cls._place_ship(size)
                    attempts += 1
                if not placed:
                    print(f"Warning: Could not place ship of size {size}")

        cls.field_initialized = True

    @classmethod
    def _place_ship(cls, size):
        """
        Helper method for placing a single ship.

        :param size: Size of the ship
        :return: True if the ship is placed, False otherwise
        """
        for _ in range(1000):
            direction = random.choice(["hor", "vert"])
            if direction == "hor":
                x = random.randint(0, 9 - size + 1)
                y = random.randint(0, 9)
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 9 - size + 1)

            if cls._check_place_ship(x, y, size, direction):
                for num in range(size):
                    if direction == "hor":
                        cls.playing_field[y][x + num] = 1
                    else:
                        cls.playing_field[y + num][x] = 1
                return True
        return False

    @classmethod
    def _check_place_ship(cls, x, y, size, direction):
        """
        Checks if a ship can be placed at the given coordinates.

        :param x: Starting X coordinate (0-9)
        :param y: Starting Y coordinate (0-9)
        :param size: Size of the ship
        :param direction: Direction ('hor' or 'vert')
        :return: True if the ship can be placed, False otherwise
        """
        for num in range(size):
            if direction == "hor":
                if x + num >= 10 or y >= 10:
                    return False
                if cls.playing_field[y][x + num] != 0:
                    return False
            else:
                if x >= 10 or y + num >= 10:
                    return False
                if cls.playing_field[y + num][x] != 0:
                    return False

        start_x = max(0, x - 1)
        end_x = min(10, x + size + 1 if direction == "hor" else x + 2)
        start_y = max(0, y - 1)
        end_y = min(10, y + size + 1 if direction == "vert" else y + 2)

        for check_y in range(start_y, end_y):
            for check_x in range(start_x, end_x):
                is_ship_cell = False
                for num in range(size):
                    if direction == "hor":
                        if check_x == x + num and check_y == y:
                            is_ship_cell = True
                            break
                    else:
                        if check_x == x and check_y == y + num:
                            is_ship_cell = True
                            break

                if not is_ship_cell and cls.playing_field[check_y][check_x] != 0:
                    return False

        return True

    def shot(self, x, y):
        """
        Method for making a shot.

        :param x: Horizontal coordinate (1 to 10)
        :param y: Vertical coordinate (1 to 10)
        """
        if not NavalBattle.field_initialized or NavalBattle.playing_field is None:
            print("игровое поле не заполнено")
            return

        if not (1 <= x <= 10 and 1 <= y <= 10):
            print("ошибка")
            return

        i, j = y - 1, x - 1

        cell = NavalBattle.playing_field[i][j]

        if isinstance(cell, str):
            print("ошибка")
            return

        if cell == 1:
            NavalBattle.playing_field[i][j] = self.player_symbol
            print("попал")

            if self._is_whole_ship_sunk(i, j):
                print("уничтожен")
        elif cell == 0:
            NavalBattle.playing_field[i][j] = "o"
            print("мимо")

    def _is_whole_ship_sunk(self, row, col):
        """
        Checks if the entire ship is destroyed after a hit.

        :param row: Row index of the hit (0-9)
        :param col: Column index of the hit (0-9)
        :return: True if the ship is completely destroyed, False otherwise
        """
        ship_parts = [(row, col)]

        current_row = row - 1
        while current_row >= 0 and NavalBattle.playing_field[current_row][col] == 1:
            ship_parts.append((current_row, col))
            current_row -= 1

        current_row = row + 1
        while current_row < 10 and NavalBattle.playing_field[current_row][col] == 1:
            ship_parts.append((current_row, col))
            current_row += 1

        current_col = col - 1
        while current_col >= 0 and NavalBattle.playing_field[row][current_col] == 1:
            ship_parts.append((row, current_col))
            current_col -= 1

        current_col = col + 1
        while current_col < 10 and NavalBattle.playing_field[row][current_col] == 1:
            ship_parts.append((row, current_col))
            current_col += 1

        for part_row, part_col in ship_parts:
            cell_value = NavalBattle.playing_field[part_row][part_col]
            if cell_value == 1:
                return False
        return True




player1 = NavalBattle('#')
player1.shot(6, 2)
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
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1,1)
player1.shot(1,1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)
