from turtle import Turtle


class Score(Turtle):
    """Creates the scoreboard"""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()
        # self.load_highscore()

    def update_score(self):
        """Updates the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score}  : High Score: {self.high_score}", False, "center", ("Arial", 24, "normal"))

    def increase_score(self):
        """Increases the score"""
        self.score += 1
        self.update_score()

    def update_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # Save the highscore to data.txt    
    def save_highscore(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

   
        


    # def game_over(self):
    #     """Triggers a game over event"""
    #     self.goto(0, 0)
    #     self.write("Game over", False, "center", ("Arial", 24, "normal"))
