import tkinter as tk
import random

root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 20  
SPEED = 200  
score = 0  

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = [(100, 100), (80, 100), (60, 100)]  
snake_direction = "Right"  
food = None  
obstacles = []  

def create_food():
    global food
    x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    food = (x, y)
    if food in snake or food in obstacles:
        create_food()
    else:
        canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="red", tag="food")

def create_obstacles():
    global obstacles
    obstacles.clear()
    for _ in range(20):  
        x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        if (x, y) not in snake and (x, y) != food:
            obstacles.append((x, y))
            canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="gray", tag="obstacle")

def move_snake():
    global snake, food, score, SPEED
    head_x, head_y = snake[0]

    if snake_direction == "Right":
        head_x += SNAKE_SIZE
    elif snake_direction == "Left":
        head_x -= SNAKE_SIZE
    elif snake_direction == "Up":
        head_y -= SNAKE_SIZE
    elif snake_direction == "Down":
        head_y += SNAKE_SIZE

    if (head_x, head_y) in snake or head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or (head_x, head_y) in obstacles:
        game_over()
        return
    
    snake = [(head_x, head_y)] + snake[:-1]
    
    if (head_x, head_y) == food:
        snake.append(snake[-1])  
        canvas.delete("food")
        score += 1
        SPEED = max(50, SPEED - 5)  
        create_food()
        update_score()

    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="green", tag="snake")

    root.after(SPEED, move_snake)

def change_direction(new_direction):
    global snake_direction
    opposite_directions = {"Right": "Left", "Left": "Right", "Up": "Down", "Down": "Up"}
    if new_direction != opposite_directions.get(snake_direction):
        snake_direction = new_direction

def update_score():
    canvas.delete("score")
    canvas.create_text(50, 10, text=f"Score: {score}", fill="white", font=("Arial", 12, "bold"), tag="score")

def reset_game():
    global snake, snake_direction, score, SPEED, obstacles
    canvas.delete("all")
    snake = [(100, 100), (80, 100), (60, 100)]
    snake_direction = "Right"
    score = 0
    SPEED = 100
    create_food()
    create_obstacles()
    update_score()
    move_snake()

def game_over():
    canvas.delete("all")
    canvas.create_text(WIDTH // 2, HEIGHT // 2 - 20, text="Game Over", fill="red", font=("Arial", 24, "bold"))
    canvas.create_text(WIDTH // 2, HEIGHT // 2 + 20, text=f"Final Score: {score}", fill="white", font=("Arial", 16))
    
    play_again_button = tk.Button(root, text="Play Again", command=reset_game, font=("Arial", 12), width=10)
    canvas.create_window(WIDTH // 2 - 50, HEIGHT // 2 + 60, window=play_again_button)
    
    quit_button = tk.Button(root, text="Quit", command=root.destroy, font=("Arial", 12), width=10)
    canvas.create_window(WIDTH // 2 + 50, HEIGHT // 2 + 60, window=quit_button)

root.bind("w", lambda e: change_direction("Up"))
root.bind("s", lambda e: change_direction("Down"))
root.bind("a", lambda e: change_direction("Left"))
root.bind("d", lambda e: change_direction("Right"))
root.bind("<Up>", lambda e: change_direction("Up"))
root.bind("<Down>", lambda e: change_direction("Down"))
root.bind("<Left>", lambda e: change_direction("Left"))
root.bind("<Right>", lambda e: change_direction("Right"))
root.bind("p", lambda e: reset_game())  
root.bind("q", lambda e: root.destroy())  

create_food()
create_obstacles()
move_snake()
update_score()

root.mainloop()