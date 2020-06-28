from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
import PIL
import textwrap


f=open("solution.txt","r") #opens text file
st=f.read()  #reads text file to a string


img = Image.new('RGB', (1366   , 768), (255,255,255)) #Creates white background image
draw = ImageDraw.Draw(img) #creates object which can make edits to image img
font=ImageFont.truetype("MyFont.ttf",size=30) #sets font and fontsize

a=30  #start making line from y coordinate=30
while(a<768):  #make lines upto y coodinate 768

    draw.line((0,a,1366,a), fill=(0,0,0)) #make line from (0,a) to (1366,a).Note general res is 1466*768
    a+=30  # increase a by value of height found in line 40


lines=textwrap.wrap(st,width=90) #convert the string to lines based on widtg(no of characters)
y_text=0 #initial height
for line in lines:  
    width, height = font.getsize(line) #get height of line used for creating lines
    lst=line.split()
    nline="  ".join(lst) #above two lines is to create more spacing betwween words due to the issue being faced
    if("?" in line):#if line contains ?
        draw.text((0, y_text), nline, font=font, fill=(0,0,255),spacing=10)#print line in blue


    else:

        draw.text((0, y_text), nline+" ", font=font, fill=(0,0,0),spacing=10)#print line in blakc

        
    y_text += height#next line to start at current height + height
    print(height)


pagenum=1    #trick to create multiple photos
img.save("image{}.jpg".format(pagenum))    #save image in folder as dynamic name



img.show() #display image
