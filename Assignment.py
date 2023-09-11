import random

#  Declare The Constants
EMPTY = '-'
RABBIT = 'r'
RABBIT_HOLDING_CARROT = 'R'
CARROT = 'c'
RABBIT_HOLE = 'O'

# Function to generate a random map
def generate_map(size, num_carrots, num_holes):
    map_size = size * size
    if num_carrots + num_holes + 1 > map_size:
        raise ValueError("Too many carrots and holes for the map size")

    # Initialize an empty map
    game_map = [EMPTY] * map_size

    # Place the rabbit randomly
    rabbit_position = random.randint(0, map_size - 1)
    game_map[rabbit_position] = RABBIT

    # Place carrots randomly
    for _ in range(num_carrots):
        while True:
            pos = random.randint(0, map_size - 1)
            if game_map[pos] == EMPTY:
                game_map[pos] = CARROT
                break

    # Place rabbit holes randomly
    for _ in range(num_holes):
        while True:
            pos = random.randint(0, map_size - 1)
            if game_map[pos] == EMPTY:
                game_map[pos] = RABBIT_HOLE
                break

    return game_map, size

# Function to print the map
def print_map(game_map, size):
    for i in range(size):
        for j in range(size):
            print(game_map[i * size + j], end=' ')
        print()

# Function to move the rabbit
def move_rabbit(game_map, size, direction):
    rabbit_index = game_map.index(RABBIT)
    row, col = divmod(rabbit_index, size)

    if direction == 'w':
        new_row = row - 1
        new_col = col
    elif direction == 's':
        new_row = row + 1
        new_col = col
    elif direction == 'a':
        new_row = row
        new_col = col - 1
    elif direction == 'd':
        new_row = row
        new_col = col + 1
    else:
        raise ValueError("Invalid direction")

    if 0 <= new_row < size and 0 <= new_col < size:
        new_index = new_row * size + new_col
        if game_map[new_index] != CARROT:
            game_map[rabbit_index] = RABBIT_HOLDING_CARROT if game_map[rabbit_index] == RABBIT_HOLDING_CARROT else EMPTY
            game_map[new_index] = RABBIT
        else:
            print("You picked up a carrot! Press 'p' to place it in a hole.")
    else:
        print("Invalid move. Try again.")

# Function to jump the rabbit over the hole
def jump_rabbit(game_map, size):
    rabbit_index = game_map.index(RABBIT)
    rabbit_hole_index = game_map.index(RABBIT_HOLE)

    row, col = divmod(rabbit_index, size)
    hole_row, hole_col = divmod(rabbit_hole_index, size)

    if row == hole_row:
        new_col = col - 1 if col > hole_col else col + 1
        new_index = row * size + new_col

        if game_map[new_index] != CARROT:
            game_map[rabbit_index] = RABBIT_HOLDING_CARROT if game_map[rabbit_index] == RABBIT_HOLDING_CARROT else EMPTY
            game_map[new_index] = RABBIT
        else:
            print("You picked up a carrot! Press 'p' to place it in a hole.")
    elif col == hole_col:
        new_row = row - 1 if row > hole_row else row + 1
        new_index = new_row * size + col

        if game_map[new_index] != CARROT:
            game_map[rabbit_index] = RABBIT_HOLDING_CARROT if game_map[rabbit_index] == RABBIT_HOLDING_CARROT else EMPTY
            game_map[new_index] = RABBIT
        else:
            print("You picked up a carrot! Press 'p' to place it in a hole.")
    else:
        print("Invalid jump. Try again.")

# Function to place a carrot in a rabbit hole
def place_carrot(game_map, size):
    rabbit_index = game_map.index(RABBIT)
    rabbit_hole_index = game_map.index(RABBIT_HOLE)

    row, col = divmod(rabbit_index, size)
    hole_row, hole_col = divmod(rabbit_hole_index, size)

    if (abs(row - hole_row) == 1 and col == hole_col) or (abs(col - hole_col) == 1 and row == hole_row):
        game_map[rabbit_hole_index] = CARROT
        game_map[rabbit_index] = RABBIT_HOLDING_CARROT if game_map[rabbit_index] == RABBIT_HOLDING_CARROT else EMPTY
        print("Carrot placed in the hole! You win!")
        return True

    print("Invalid placement. Try again.")
    return False

# Main game loop
def play_game(size, num_carrots, num_holes):
    game_map, size = generate_map(size, num_carrots, num_holes)
    print_map(game_map, size)

    while True:
        action = input("Enter your move (w/a/s/d/j/p/q):  , a=move left , s=move right , w=move up , s=move down , p=pick carrots , j=jump " ).lower()

        if action == 'q':
            print("Game over. You quit.")
            break
        elif action in ['w', 'a', 's', 'd']:
            move_rabbit(game_map, size, action)
        elif action == 'j':
            jump_rabbit(game_map, size)
        elif action == 'p':
            if place_carrot(game_map, size):
                break
        else:
            print("Invalid input. Please try again.")

# Start the game
if __name__== "__main__":
    size = int(input("Enter the size of the grid: "))
    num_carrots = int(input("Enter the number of carrots: "))
    num_holes = int(input("Enter the number of rabbit holes: "))

    play_game(size, num_carrots, num_holes)