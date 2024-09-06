import random
import json

def generate_maze(width, height):
    # Initialize maze with walls
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    # Define the start point and end point
    start = (1, 1)
    end = (height - 2, width - 2)
    
    # Create a random path from start to end
    current = start
    maze[start[0]][start[1]] = 0  # Mark start as path

    while current != end:
        x, y = current
        # Possible directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)  # Randomize direction order
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < height - 1 and 0 < ny < width - 1 and maze[nx][ny] == 1:
                maze[nx][ny] = 0  # Mark as path
                current = (nx, ny)
                break
        else:
            # If no valid move, backtrack (this shouldn't happen in a proper implementation)
            print("Error: No valid move found. This shouldn't happen.")
            return None

    # Mark end point
    maze[end[0]][end[1]] = 2

    return maze

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

