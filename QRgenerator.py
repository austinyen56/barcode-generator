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
    s = 147 - s * 3.4   # Chinese chars are * 7
    return int(s)

# Parsing all the book names from txt file
bn = [] # Stores all 50 book names
# For testing bn
#bn = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49']     
with open(r"C:\Users\Austin\Desktop\booknames.txt", "r",encoding="utf-8") as f:
    #print(f.read())
    for i in f.read().split('\n'):
        bn.append(i.title().strip())
#print(bn)

# Adding text to a picture generated from barcodegen()
def addtxt():
    snum = 14835
    bn_index = 0    # Loops through indexes in bn and loops back again 40 times

    for l in range(2001):
        bn_index = bn_index % 50
        title = bn[bn_index]
        img = Image.open("D:\Python Projects\qrresults\\000"+ str(snum) + ".png")
        tf = ImageFont.truetype('C:\WINDOWS\FONTS\MSJH.ttc', 15)
        ImageDraw.Draw(img).text((90,200),"彰化縣縣立大西國小",(0,0,0),font= tf)
        ImageDraw.Draw(img).text((centerize(title),222),title,(0,0,0),font= tf)
        img.save("D:\Python Projects\qrresults\\000"+ str(snum) + ".png")

        bn_index += 1
        snum += 1
        print("Added book names to: " + str(snum))
        
addtxt()
