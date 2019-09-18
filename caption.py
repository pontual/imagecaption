import os
from PIL import Image, ImageFont, ImageDraw

def caption(origfilename,
            text,
            fontsize=40):
    img = Image.open(origfilename)
    w, h = img.size
    if w > 2000:
        fontsize = 96
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("c:/Users/Heitor/Desktop/code/imagecaption/ubuntu.ttf", fontsize)
    draw.text((10, 10), text, (190, 0, 0), font=font)

    # target_filename = origfilename.split("imagecaption/original/")[-1]
    target_filename = origfilename.split("/")[-1]
    
    img.save("c:/Users/Heitor/Desktop/code/imagecaption/anotado/" + target_filename)
