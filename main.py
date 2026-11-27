from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
food.refresh(snake)
scoreboard = Scoreboard()

snake.head.hideturtle()
for segment in snake.snakes[1:]:
    segment.hideturtle()

food.hideturtle()

game_is_on = False
def game_loop():
    global game_is_on
    screen.update()
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh(snake)
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 240 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail
    for seg in snake.snakes[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_is_on = False

    screen.update()

    if game_is_on:
        screen.ontimer(game_loop, 100)

def restart_game():
    global game_is_on

    if not game_is_on:
        snake.reset()
        food.refresh(snake)
        scoreboard.restart()
        game_is_on = True
        game_loop()

def start_game():
    global game_is_on

    if not game_is_on:
        scoreboard.clear()
        scoreboard.update_scoreboard()
        game_is_on = True
        snake.head.showturtle()
        for segments in snake.snakes[1:]:
            segments.showturtle()
        food.showturtle()
        game_loop()

screen.listen()
screen.onkey(start_game, "space")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(restart_game,"R")
screen.onkey(screen.bye, "Q")

scoreboard.welcome_screen()
screen.update()
screen.exitonclick()