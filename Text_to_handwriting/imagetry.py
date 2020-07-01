from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
import PIL
import textwrap
import new


     






f=open("solution.txt","r") #opens text file
st_list=f.readlines()  #reads text file to a list of string



font=ImageFont.truetype("MyFont.ttf",size=30)
pagenum=1
img,draw=new.newImg()
y_text=100
newpage=False
control=0
height=30

print(st_list)

for para in st_list:
    if("?" in para):
        color=(0,0,255)
    else:
        color=(0,0,0)    

    textlines=textwrap.wrap(para,width=55)
    for line in textlines:
        if(y_text>768):
            newpage=True  
        if(newpage):
            img.save("image{}.jpg".format(pagenum)) 
            pagenum+=1
            img,draw=new.newImg()
            y_text=100
            newpage=False
            
        
        
        lst=line.split()
        nline="   ".join(lst)
        draw.text((100, y_text), nline, font=font, fill=color,spacing=10)
        y_text += height
    y_text+=height    
        
img.save("image{}.jpg".format(pagenum)) 
img.show()              




