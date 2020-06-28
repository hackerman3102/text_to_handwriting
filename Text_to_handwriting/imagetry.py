from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
import PIL
import textwrap

st=("""Lorem Ipsum is simply dummy text of the printing and typesetting
Lorem Ipsum is simply dummy text of the printing and typesetting?
Lorem Ipsum is simply dummy text of the printing and typesetting 
Lorem Ipsum is simply dummy text of the printing and typesetting
Lorem Ipsum is simply dummy text of the printing and typesetting 
Lorem Ipsum is simply dummy texts of the printing and typesettings""")

f=open("solution.txt","r")
st=f.read()


img = Image.new('RGB', (1366   , 768), (255,255,255))
draw = ImageDraw.Draw(img)
font=ImageFont.truetype("Myfont.ttf",size=30)

a=36
while(a<768):

    draw.line((0,a,1366,a), fill=(0,0,0,0))
    a+=34





lines=textwrap.wrap(st,width=90)
y_text=0
for line in lines:
    width, height = font.getsize(line)
    
    if("?" in line):
        draw.text((0, y_text), line, font=font, fill=(0,0,255),spacing=2)


    else:

        draw.text((0, y_text), line, font=font, fill=(0,0,0),spacing=2)

        
    y_text += height
    print(height)


pagenum=1    
img.save("image{}.jpg".format(pagenum))    



draw.line((40,40),fill=(0,200,0),width=0)



img.show()
text_width, text_height = draw.textsize("typesetting")
print(text_width,text_height)



