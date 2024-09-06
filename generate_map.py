import random
import json

def generate_maze(width, height):
    # Initialize maze with walls (1s)
    maze = [[1] * width for _ in range(height)]
    
    # Define start and end points
    start = (0, 0)
    end = (height - 1, width - 1)
    
    # Set start point as path (0)
    x, y = start
    maze[x][y] = 0
    
    while (x, y) != end:
        # Possible moves
        moves = []
        if x < end[0]:  # Can move down
            moves.append((1, 0))
        if y < end[1]:  # Can move right
            moves.append((0, 1))
        
        # Add moves left and up with a 10% chance if they are valid
        if x > 0:  # Can move up
            if random.random() < 0.1:  # 10% chance
                moves.append((-1, 0))
        if y > 0:  # Can move left
            if random.random() < 0.1:  # 10% chance
                moves.append((0, -1))
        
        # If there are no valid moves, we are stuck, so backtrack
        if not moves:
            break
        
        # Randomly choose a move
        dx, dy = random.choice(moves)
        x += dx
        y += dy
        
        # Ensure the new position is within bounds
        if 0 <= x < height and 0 <= y < width:
            # Mark the path
            maze[x][y] = 0
        else:
            # If out of bounds, revert the move
            x -= dx
            y -= dy

    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(str(cell) for cell in row))
def save_maze_to_file(maze, filename):
    with open(filename, 'w') as file:
        json.dump(maze, file)

# Example usage
maze = generate_maze(20, 20)
if maze:
    save_maze_to_file(maze, 'maze.json')
    print("Maze generated and saved successfully.")
else:
    print("Failed to generate maze.")

