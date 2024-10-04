import random

# Constants for the game
GRID_SIZE = 5
NUM_MINES = 3

# Initialize the grid
def create_grid(size):
    return [['-' for _ in range(size)] for _ in range(size)]

# Randomly place mines in the grid
def place_mines(grid, num_mines):
    mines = 0
    while mines < num_mines:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        if grid[row][col] != 'M':  # Ensure no duplicate mines
            grid[row][col] = 'M'
            mines += 1

# Check if the clicked cell contains a mine
def click_cell(grid, row, col):
    if grid[row][col] == 'M':
        print("Boom! You hit a mine!")
        return True  # Game over
    else:
        print("Safe! No mine here.")
        # Optional: Add more logic here to reveal neighboring cells
        return False  # Safe

# Print the grid (for debugging)
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Main game logic
def play_game():
    # Create and set up the grid
    grid = create_grid(GRID_SIZE)
    place_mines(grid, NUM_MINES)

    # Debug: print grid (normally hidden)
    print_grid(grid)

    # Game loop
    while True:
        # Get player input (row and col)
        row = int(input("Enter row (0-4): "))
        col = int(input("Enter col (0-4): "))
        
        # Handle out-of-bounds
        if row < 0 or row >= GRID_SIZE or col < 0 or col >= GRID_SIZE:
            print("Invalid input! Try again.")
            continue
        
        # Click the cell and check for a mine
        if click_cell(grid, row, col):
            break  # Game over
        else:
            print("Keep playing!")
        
        print_grid(grid)  # Optional: For debugging

# Start the game
play_game()
