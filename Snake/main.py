from snake import Snake
from screen import SnakeScreen
from food import Food
from score import Score

snake = Snake()
screen = SnakeScreen(snake)
food = Food()
score = Score()

game_is_on = True
while game_is_on:
    screen.refresh()
    snake.move()
    screen.listen_key()

    # Detect collision with food
    if snake.head.distance(food) < 25:
        food.refresh_location()
        snake.extend()
        score.increment_score()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()

screen.exit()
