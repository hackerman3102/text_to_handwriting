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
    while(a<768):  #make lines upto y coodinate 768
        draw.line((0,a+100,1366,a+100), fill=(0,0,0)) #make line from (0,a) to (1366,a).Note general res is 1466*768
        a+=30  # increase a by value of height found in line 40
    
    return img
def ImageToPdf():
    imageto=Image.open(r'C:\Users\Sushmita Agrawal\Downloads\TextToHandwriting\text_to_handwriting\Text_to_handwriting\image1.jpg')
    im1 = imageto.convert('RGB')
    im1.save(r'C:\Users\Sushmita Agrawal\Downloads\TextToHandwriting\text_to_handwriting\Text_to_handwriting\im1.pdf')

f=open("solution.txt","r") #opens text file
st=f.read()  #reads text file to a string


img=newImg() #func call

font=ImageFont.truetype("MyFont.ttf",size=30)
draw = ImageDraw.Draw(img)
lines=textwrap.wrap(st,width=65)
y_text=100
for line in lines:  
    width, height = font.getsize(line) #get height of line used for creating lines
    lst=line.split()
    nline="   ".join(lst) #above two lines is to create more spacing betwween words due to the issue being faced
    if("?" in line):#if line contains ?
        draw.text((100, y_text), nline, font=font, fill=(0,0,255),spacing=10)#print line in blue
    else:
        draw.text((100, y_text), nline+" ", font=font, fill=(0,0,0),spacing=10)#print line in blakc    
    y_text += height#next line to start at current height + height

img.show() 
pagenum=1    #trick to create multiple photos
img.save("image{}.jpg".format(pagenum))    #save image in folder as dynamic name

ImageToPdf()
