from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Courier", 24, "normal")
FONT2 = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0,265)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT1)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")

        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT1)

        self.goto(0,-40)
        self.write("Press 'R' to Restart", align = ALIGNMENT, font = FONT2)

        self.goto(0,-65)
        self.write("Press 'Q' to Quit", align = ALIGNMENT, font = ("Courier", 14, "normal"))

    def restart(self):
        self.score = 0
        self.update_scoreboard()

    def welcome_screen(self):
        self.clear()
        self.goto(0,40)
        self.write("SNAKE TAIL", align=ALIGNMENT, font= ("Courier", 30, "bold"))

        self.goto(0,-10)
        self.write("Use Arrow Keys to Move", align = ALIGNMENT, font = FONT2)

        self.goto(0,-50)
        self.write("Press SPACE to Start", align = ALIGNMENT, font = FONT2)