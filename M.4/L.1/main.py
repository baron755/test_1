from PIL import Image

with Image.open("original.jpg") as pic_original:
    print("Розмір:", pic_original.size)
    print("Формат:", pic_original.format)
    print("Тип:", pic_original.mode)
    pic_original.show()

#открой файл с оригиналом картинки

#сделай оригинал изображения чёрно-белым
from PIL import Image
from PIL import ImageFilter

with Image.open("original.jpg") as pic_original:
    pic_original.show()
    
    pic_gray = pic_original.convent("L")
    pic_gray.save("original.jpg")
    pic_gray.show()
    
    pic_up = pic_gray.transpone(Image.ROTATE_90)
    pic_up.save("original2.jpg")
    pic_up.show()
    


#сделай оригинал изображения размытым

#поверни оригинал изображения на 180 градусов