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
    
    # Define the probability of a cell being an open space
    probability_of_open_space = 0.5  # 50% chance to be an open space
    
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            if (x, y) != start and (x, y) != end:
                if random.random() < probability_of_open_space:
                    maze[x][y] = 0

    # Ensure the end goal is fully accessible
    def make_end_accessible(maze, end):
        ex, ey = end
        # Ensure that the end goal is surrounded by open cells
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = ex + dx, ey + dy
            if 0 < nx < height - 1 and 0 < ny < width - 1:
                maze[nx][ny] = 0
    
    make_end_accessible(maze, end)
    
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

