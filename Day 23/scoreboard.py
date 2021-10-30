from turtle import Turtle


class Score(Turtle):
    """Creates the scoreboard"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        """Updates the scoreboard"""
        self.write(f"Score: {self.score}", False, "center", ("Arial", 24, "normal"))

    def increase_score(self):
        """Increases the score"""
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        """Triggers a game over event"""
        self.goto(0, 0)
        self.write("Game over", False, "center", ("Arial", 24, "normal"))
