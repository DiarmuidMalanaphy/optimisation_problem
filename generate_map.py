import random
import json

def generate_maze(width, height):
    # Initialize maze with walls
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    # Define the start point and end point
    start = (1, 1)
    end = (height - 2, width - 2)
    
    # Mark start and end points
    maze[start[0]][start[1]] = 0
    maze[end[0]][end[1]] = 2
    
    # Create a list of positions to explore
    stack = [start]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while stack:
        x, y = stack[-1]
        maze[x][y] = 0
        
        # Find all possible directions
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < height - 1 and 0 < ny < width - 1 and maze[nx][ny] == 1:
                if maze[x + dx][y + dy] == 1:
                    maze[x + dx][y + dy] = 0
                    stack.append((nx, ny))
                    break
        else:
            stack.pop()
    
    # Randomly open up more spaces
    for _ in range(width * height // 2):
        x, y = random.randint(1, height - 2), random.randint(1, width - 2)
        if maze[x][y] == 1:
            maze[x][y] = 0
    
    return maze

def save_maze_to_file(maze, filename):
    with open(filename, 'w') as file:
        json.dump(maze, file)

# Define the size of the maze
width, height = 200, 70

# Generate the maze
maze = generate_maze(width, height)

# Save the maze to a file
save_maze_to_file(maze, 'maze.json')

