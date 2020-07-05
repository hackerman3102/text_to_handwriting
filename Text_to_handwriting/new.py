from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
import PIL
import textwrap

def newImg():
    img = Image.new('RGB', (1366   , 768), (255,255,255)) #Creates white background image
    draw = ImageDraw.Draw(img) #creates object which can make edits to image img
    #sets font and fontsize

    draw.line((100,0,100,768),fill=(255,0,0))
    draw.line((0,100,1366,100),fill=(255,0,0))
    a=30 #start making line from y coordinate=30
    while(a<630):  #make lines upto y coodinate 768
        draw.line((0,a+100,1366,a+100), fill=(0,0,0)) #make line from (0,a) to (1366,a).Note general res is 1466*768
        a+=30  # increase a by value of height found in line 40
    
    return img,draw


