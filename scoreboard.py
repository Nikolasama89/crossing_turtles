from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.current_level()

    def current_level(self):
        self.clear()
        self.goto(-290, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_update(self):
        self.level += 1
        self.current_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



