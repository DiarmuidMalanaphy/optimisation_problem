import random
import json

def generate_maze(width, height):
    # Initialize maze with walls
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    # Define the start point and end point
    start = (1, 1)
    end = (height - 2, width - 2)
    
    # Initialize the stack with the start point
    stack = [start]
    maze[start[0]][start[1]] = 0  # Mark start as path

    while stack:
        current = stack[-1]
        x, y = current

        # Possible directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)  # Randomize direction order
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < height - 1 and 0 < ny < width - 1 and maze[nx][ny] == 1:
                maze[nx][ny] = 0  # Mark as path
                stack.append((nx, ny))
                break
        else:
            # If no valid move, backtrack
            stack.pop()
        # Optional: Break if we've reached the end
        if current == end:
            break
    # Ensure the end point is marked
    maze[end[0]][end[1]] = 2
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

