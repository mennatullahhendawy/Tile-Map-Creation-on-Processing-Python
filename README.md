# Tile Map Creation on Processing Python
 
Tile Map Creation Tool
This repository contains a Tile Map Creation Tool developed as part of the Game Development 1 course at the University of California, Santa Cruz. The tool allows users to create tile maps by selecting different tiles and placing them on a grid.

Acknowledgments
Acknowledgments: This project was developed as an assignment for the Game Development 1 course (GAME 235) at the University of California, Santa Cruz. The code was developed with the help of Mohamed Samy and Mohamed-Ali-77. Additionally, we used ChatGPT to assist in structuring and refining parts of the project.

Overview
The Tile Map Creation Tool lets you click on the screen to create tiles on a grid, select between four different tile colors, and display the currently selected tile. You can also save the created tile map as an image.

Some of the Game Features
•	Clicking on the screen places a tile on the grid.
•	Keyboard keys (1, 2, 3, 4) allow switching between at least four different tile types.
•	The currently selected tile is visible and follows the mouse cursor with transparency.
•	 Pressing a given key on the keyboard will save a screenshot

2. Installation
1.	Download and install Processing.
2.	Enable Python Mode:
o	Open Processing.
o	Go to the Mode drop-down menu at the top right.
o	Select Python mode from the list.
3.	Clone or download this repository to your local machine.
4.	Open the tile_map_creator.pde file in Processing.

Usage
Controls
1.	Press 1, 2, 3, or 4 to select a tile color:
o	1: Red Tile
o	2: Green Tile
o	3: Blue Tile
o	4: Yellow Tile
2.	Click on the screen to place the selected tile on the grid.
3.	Press 's' to save the tile map as a screenshot (saves as tilemap.png).

Running the Program
1.	Launch Processing.
2.	Open the tile_map_creator.pde file from this repository.
3.	Click the Run button in Processing to start the tile map creation tool.
4.	Select a tile color using the keyboard and place tiles by clicking on the grid.

Example Code Snippet
```python
Copy code
# Initial fixed variables
grid_size = 40
tiles = []  # Grid creation list
selected_tile = 0  # First tile starts on the top left corner
tile_images = []  # List to store tile colors

def setup():
    size(600, 600)  # Background size
    noStroke()  # No stroke for the grid
    load_tiles()  # Load the tile colors

def load_tiles():
    global tile_images
    # Load 4 different tiles (colored squares for simplicity)
    tile_images = [
        color(255, 0, 0),  # Red Tile
        color(0, 255, 0),  # Green Tile
        color(0, 0, 255),  # Blue Tile
        color(255, 255, 0)  # Yellow Tile
    ]

def draw():
    draw_grid()  # Draw the grid
    draw_tiles()  # Draw placed tiles
    draw_selected_tile()  # Show selected tile following the mouse cursor

def draw_grid():
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            fill(0)  # No color for grid background
            rect(x, y, grid_size, grid_size)  # Draw grid rectangles

def draw_tiles():
    for t in tiles:
        fill(t[2])  # Fill the placed tile with selected color
        rect(t[0] * grid_size, t[1] * grid_size, grid_size, grid_size)  # Draw tile at the grid location

def draw_selected_tile():
    # Draw the selected tile following the mouse cursor with transparency
    fill(tile_images[selected_tile], 128)  # Transparency applied
    rect(mouseX // grid_size * grid_size, mouseY // grid_size * grid_size, grid_size, grid_size)

def mousePressed():
    # Add a tile to the grid based on mouse position
    x = mouseX // grid_size
    y = mouseY // grid_size
    tiles.append((x, y, tile_images[selected_tile]))

def keyPressed():
    global selected_tile
    # Change tile color based on key pressed (1, 2, 3, 4 for tiles)
    if key == '1':
        selected_tile = 0
    elif key == '2':
        selected_tile = 1
    elif key == '3':
        selected_tile = 2
    elif key == '4':
        selected_tile = 3
    elif key == 's':
        save_frame("tilemap.png")  # Save screenshot


