from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
img=Image.new('RGB', (200, 100), (255,255,255))
d = ImageDraw.Draw(img)
d.text((10,10), "Hello World", fill=(255,255,0))
img.show()