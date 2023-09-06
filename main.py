from PIL import Image
import os

def split_spritesheet(filename, sprite_width, sprite_height, output_folder):
    """
    Splits a sprite sheet into individual sprites.

    :param filename: The sprite sheet filename.
    :param sprite_width: Width of a single sprite.
    :param sprite_height: Height of a single sprite.
    :param output_folder: Folder to save individual sprite images.
    """
    # Open the sprite sheet
    sprite_sheet = Image.open(filename)
    
    # Calculate the number of sprites in x and y direction
    sheet_width, sheet_height = sprite_sheet.size
    x_sprites = sheet_width // sprite_width
    y_sprites = sheet_height // sprite_height

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each sprite in the sprite sheet
    for x in range(x_sprites):
        for y in range(y_sprites):
            # Define box coordinates for cropping
            left = x * sprite_width
            upper = y * sprite_height
            right = left + sprite_width
            lower = upper + sprite_height
            
            # Crop and save each sprite
            sprite = sprite_sheet.crop((left, upper, right, lower))
            sprite_filename = os.path.join(output_folder, f'sprite_{x}_{y}.png')
            sprite.save(sprite_filename)
            print(f"Saved: {sprite_filename}")

if __name__ == '__main__':
    # Replace with the path to your sprite sheet and the sprite dimensions
    sprite_sheet_filename = 'spritesheets/magicCircle 160x160.png'
    sprite_w = 160  # replace with the width of a single sprite
    sprite_h = 160  # replace with the height of a single sprite 
    output_dir = 'sprites'

    split_spritesheet(sprite_sheet_filename, sprite_w, sprite_h, output_dir)
