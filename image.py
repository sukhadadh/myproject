
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)


class processing():
    def __init__(self,img) :
        self.img = img
        
    def display(self):
        self.img.show()
        self.img.save("sample image.jpg")
    
    def properties(self):
        print("properties of a image:")
        print("size of image:",self.img.size)
        print("format of image:",self.img.format)
        print("mode of a image:",self.img.mode)

    def resize(self):
        p1 = int(input("enter parameter 1:"))
        p2 = int(input("enter parameter 2:"))
        newimg = self.img.resize((p1,p2))
        newimg.show()
        newimg.save("newimg.jpg")

    def rotate(self):
        a = int(input("enter a angle to rotate:"))
        rimg =self.img.rotate(a)
        rimg.show()
        rimg.save("rimg.jpg")

    def gray(self):
        gimg = self.img.convert("L")
        gimg.show()
        gimg.save("gimg.jpg")

    def crop(self):
        box = (200, 300, 700, 600)
        cimg = self.img.crop(box)
        cimg.show()
        cimg.save("cimg.jpg")

    def blur(self):
        bimg = self.img.filter(ImageFilter.BLUR)
        bimg.show()
        bimg.save("bimg.jpg")

    def hflip(self):
        himg = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        himg.show()
        himg.save("himg.jpg")

    def vflip(self):
        vimg = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        vimg.show()
        vimg.save("vimg.jpg")

    def contour(self):
        coimg = self.img.filter(CONTOUR)
        coimg.show()
        coimg.save("coimg.jpg")

pro = Image.open(r"C:\Users\SUKHADA\Downloads\sample.jpg")
image = processing(pro)
#image.rotate()
while(True):
    print("Select the operation you want to perform:")
    print("1. Display image")
    print("2.Properties of image")
    print("3.resize image")
    print("4.rotate image")
    print("5.graing image")
    print("6.croping image")
    print("7.bluring image")
    print("8.horizontally flip image")
    print("9.vertically flip image")
    print("10.countour image")
    print("11.exit")
    print("--------------------------------")
    op = int(input("enter your choice:"))
    if (op == 1):
        
        image.display()

    elif (op == 2):
        image.properties()

    elif (op == 3):
        image.resize()

    elif (op == 4):
        image.rotate()

    elif (op == 5):
        image.gray()

    elif (op == 6):
        image.crop()

    elif (op == 7):
        image.blur()

    elif (op == 8):
        image.hflip()

    elif (op == 9):
        image.vflip()

    elif (op == 10):
        image.contour()

    elif (op == 11):
        print("Thanks for using image processing system")
        print("We hope you enjoyed!!")
        break

