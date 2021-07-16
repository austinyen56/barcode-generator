import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageFont, ImageDraw
# Generates 2000 barcodes from 14835 to 16835 in png format
# Stored in directory shown below
def barcodegen():
    snum = 14835
    for i in range(2001):
        sn = "000"+ str(snum)
        code = barcode.get("gs1_128", str(sn), writer=ImageWriter())
        code.save("D:\Python Projects\qrresults\\"+sn)
        snum+=1
        print("Done with "+ sn)
barcodegen()

# x = 148 - 1 center
# 4px a char
def centerize(s):
    s = len(s)
    s = 147 - s * 7
    return int(s)

# Adding text to a picture generated from barcodegen()
def addtxt():
    title = "哈哈哈哈哈"
    img = Image.open("D:\Python Projects\qrresults\\"+'00014835.png')
    tf = ImageFont.truetype('simsun.ttc', 15)
    ImageDraw.Draw(img).text((90,200),"彰化縣縣立大西國小",(0,0,0),font= tf)
    ImageDraw.Draw(img).text((centerize(title),225),title,(0,0,0),font= tf)
    img.save("D:\Python Projects\qrresults\meme.png")
addtxt()
