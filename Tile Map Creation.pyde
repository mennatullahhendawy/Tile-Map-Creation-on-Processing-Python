# Tile Map Creation Tool
# Controls:
# 1. Press 1, 2, 3, 4 to select different tile color
# 2. Press 's' to save a screenshot
# 3. Tiles will follow the mouse and can be placed by clicking



# initial fixed Variables
grid_size = 40
tiles = [] #grid creation list
selected_tile = 0 #first tile starts on the top left corner
tile_images = [] #change of colour on click

def setup(): #background
    size(600, 600) #background size
    noStroke() #no stroke for background
    load_tiles() #call function 

def load_tiles(): #identify the function called above
    # Load 4 different tiles (colored squares for simplicity)
    global tile_images #making the variable global
    tile_images = [ #adding the four tiles to the list
        color(255, 0, 0),   # Red Tile
        color(0, 255, 0),   # Green Tile
        color(0, 0, 255),   # Blue Tile
        color(255, 255, 0)  # Yellow Tile
    ]

def draw():
    draw_grid() #functions to be called
    draw_tiles() #functions to be called
    draw_selected_tile() #functions to be called

def draw_grid(): #drawing the reapted grid
    for x in range(0, width, grid_size): #for loop to create the background grid
        for y in range(0, height, grid_size):
            fill(0)#no color fill for the grid/tile 
            rect(x, y, grid_size, grid_size) #drawing the grid as a rectangle

def draw_tiles(): #filling the grid with color
    for t in tiles: #for loop to repeat this function according to tile numbers
        fill(t[2]) #filling the tile that we press with updated colour 
        rect(t[0] * grid_size, t[1] * grid_size, grid_size, grid_size) #drawing rectangle for the tile

def draw_selected_tile(): #drawing the tile that the mouse pressed on
    # Draw the selected tile following the mouse cursor with transparency
    fill(tile_images[selected_tile], 128)  # Transparency
    rect(mouseX // grid_size * grid_size, mouseY // grid_size * grid_size, grid_size, grid_size) #draw rectangle on the location of the mouse

def mousePressed(): #defining mouse click
    # Add a tile to the grid based on mouse position
    x = mouseX // grid_size
    y = mouseY // grid_size
    tiles.append((x, y, tile_images[selected_tile])) #filling tile when i click

def keyPressed(): #defining the change of color
    global selected_tile
    # Change the tile based on key pressed (1, 2, 3, 4 for tiles)
    if key == '1':
        selected_tile = 0
    elif key == '2':
        selected_tile = 1
    elif key == '3':
        selected_tile = 2
    elif key == '4':
        selected_tile = 3
    elif key == 's':
        save_frame("tilemap.png")  # Save screenshot (add your path)
