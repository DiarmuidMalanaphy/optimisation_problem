import random
import json

def generate_maze(width, height):
    # Initialize maze with walls
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    # Define the start point and end point
    start = (1, 1)
    end = (height - 2, width - 2)
    
    # Create a path from start to end
    current = start
    stack = [current]
    visited = set([current])
    
    while current != end:
        x, y = current
        neighbors = [(x+dx, y+dy) for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]
                     if 0 < x+dx < height-1 and 0 < y+dy < width-1 and (x+dx, y+dy) not in visited]
        
        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(next_cell)
            visited.add(next_cell)
            maze[next_cell[0]][next_cell[1]] = 0
            current = next_cell
        elif stack:
            current = stack.pop()
        else:
            break  # This should not happen if the maze is solvable
    
    # Mark start and end points
    maze[start[0]][start[1]] = 0
    maze[end[0]][end[1]] = 2
    
    # Add some random open spaces
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            if (x, y) not in visited and random.random() < 0.3:  # 30% chance to be an open space
                maze[x][y] = 0
    
    return maze

def save_maze_to_file(maze, filename):
    with open(filename, 'w') as file:
        json.dump(maze, file)

# Example usage
maze = generate_maze(200, 200)
save_maze_to_file(maze, 'maze.json')
