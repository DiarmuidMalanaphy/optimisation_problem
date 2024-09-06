import pygame
import json

def load_maze_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def draw_maze(maze):
    # Initialize pygame
    pygame.init()
    
    # Define constants
    cell_size = 10  # Size of each cell in pixels
    width, height = len(maze[0]), len(maze)
    screen_width, screen_height = width * cell_size, height * cell_size
    
    # Set up the display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Visualization")
    
    # Define colors
    colors = {
        0: (255, 255, 255),  # White for empty space
        1: (0, 0, 0),        # Black for walls
        2: (0, 255, 0)       # Green for the end goal
    }
    
    # Draw the maze
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, colors[cell], (x * cell_size, y * cell_size, cell_size, cell_size))
    
    # Update the display
    pygame.display.flip()
    
    # Event loop to keep window open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

# Load the maze from a file
maze = load_maze_from_file('maze.json')

# Visualize the maze
draw_maze(maze)
