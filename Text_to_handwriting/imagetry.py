from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
import PIL
import textwrap
import new
import os
import random

f=open("solution.txt","r") #opens text file
st_list=f.readlines()  #reads text file to a list of string



font=ImageFont.truetype("MyFont.ttf",size=30)
pagenum=1
img,draw=new.newImg()
y_text=100
newpage=False
height=30



for para in st_list:
    


    if("?" in para):
        color=(0,0,255)
    else:
        color=(0,0,0)    

    textlines=textwrap.wrap(para,width=55)
    for line in textlines:
        x=1#random.randint(1,1)
        if(x==1):
            font=ImageFont.truetype("MyFont.ttf",size=30)
        else:
            font=ImageFont.truetype("newFont.ttf",size=30)
        if(y_text>699):
            newpage=True  
        if(newpage):
            img.save(r"images/image{}.jpg".format(pagenum)) 
            pagenum+=1
            img,draw=new.newImg()
            y_text=100
            newpage=False
            
        
        
        lst=line.split()
        nline="   ".join(lst)
        draw.text((100, y_text), nline, font=font, fill=color,spacing=10)
        y_text += height
    y_text+=height    
        
img.save(r"images/image{}.jpg".format(pagenum)) 
img.show()              
imglst=[i for i in os.listdir(r'images/') if i.endswith(".jpg")]
print(imglst)

lst=[]
for i in imglst:
    a=Image.open(r"images/{}".format(i))
    lst.append(a)

lst[0].save("Converted.pdf",resolution=100.0, save_all=True, append_images=lst[1:])








