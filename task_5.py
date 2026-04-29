class Game:
    """
    Class modeling a basketball game between two teams.

    Attributes:
        teams (dict): dictionary with team names under keys 'command1' and 'command2'.
        scores (dict): dictionary holding current scores of teams with keys 1 and 2.
    """

    def __init__(self, commands):
        """
        Initialize the game with team names and zero scores.

        Args:
            commands (dict): dictionary with keys 'command1' and 'command2' mapping to team names.
        """
        self.teams = {
            1: commands.get('command1', 'Team 1'),
            2: commands.get('command2', 'Team 2')
        }
        self.scores = {1: 0, 2: 0}

    def ball_thrown(self, command, points):
        """
        Add points to the specified team.

        Args:
            command (int): team number (1 or 2).
            points (int): number of points scored.

        Raises:
            ValueError: if command is not 1 or 2, or points is negative.
        """
        if command not in (1, 2):
            raise ValueError("Team number must be 1 or 2.")
        if points < 0:
            raise ValueError("Points is natural.")
        self.scores[command] += points

    def get_score(self):
        """
        Get the current score of the game.

        Returns:
            tuple: current scores of team 1 and team 2 as (score1, score2).
        """
        return (self.scores[1], self.scores[2])

    def get_winner(self):
        """
        Determine the winner of the game.

        Returns:
            str: name of the winning team, or 'Draw' if scores are equal.
        """
        if self.scores[1] > self.scores[2]:
            return self.teams[1]
        elif self.scores[2] > self.scores[1]:
            return self.teams[2]
        else:
            return 'Draw'



game_one = Game({'command1': 'Utah Jazz', 'command2': 'Miami Heat'})

game_one.ball_thrown(1, 2)
game_one.ball_thrown(1, 3)
game_one.ball_thrown(2, 2)
game_one.ball_thrown(1, 1)

print(game_one.get_score())

game_one.ball_thrown(2, 3)
game_one.ball_thrown(2, 2)
game_one.ball_thrown(1, 2)

print(game_one.get_score())

print(game_one.get_winner())
