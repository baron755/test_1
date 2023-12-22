from PIL import Image, ImageFile

class ImageEditor():
    def __init_(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()
        
    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("File not found")
        self.original.show()
        
    def do_left(self):
        rotated = self.original.transpose(Image.ROTATE_90)
        self.changed.append(rotated)

#открой файл с оригиналом картинки
#python -m pip install pillow
#сделай оригинал изображения чёрно-белым

#сделай оригинал изображения размытым

#поверни оригинал изображения на 180 градусов